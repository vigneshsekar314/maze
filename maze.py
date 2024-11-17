from window import TWindow
from point import Point
from cell import Cell
from time import sleep
from random import randint


class Maze:


    def __init__(self, rows: int, cols: int, start_pt: Point, cell_width: int, cell_height:int, win: TWindow | None = None) -> None:
        """
        creates a maze box with provided row and column count. It takes a start_pt argument to specify the starting x,y co-ordinate of the maze.
        cell_width and cell_height specifies the width and height dimensions of the cell.
        """
        self.__rows: int = rows
        self.__cols: int = cols
        self.__start_pt: Point = start_pt
        self.__cell_width: int = cell_width
        self.__cell_height: int = cell_height
        self.__win: TWindow | None = win
        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        """
        creates cells in the window provided to the Maze class
        """
        for col in range(self.__cols):
            col_items = []
            for row in range(self.__rows):
                col_items.append(self._draw_cell(row, col))
            self._cells.append(col_items)

    def _break_entrance_and_exit(self):
        if len(self._cells) != 0 and len(self._cells[0]) != 0:
            self._cells[0][0] = self._draw_cell(0, 0, top_wall = False)
            end_x = self.__rows - 1
            end_y = self.__cols - 1
            if len(self._cells) == self.__rows and len(self._cells[end_x]) == self.__cols:
                self._cells[end_x][end_y] = self._draw_cell(end_x, end_y, bottom_wall = False)
                self._animate()

    def _draw_cell(self, i: int, j: int, top_wall: bool = True, left_wall: bool = True, bottom_wall: bool = True, right_wall: bool = True, fill_color: str = "blue") -> Cell:
        """
        draws each cell corresponding to the index position i and j. i represents the row index and j represents the column index.
        """
        start_point: Point = Point(self.__start_pt.get_x() + (i * self.__cell_width), self.__start_pt.get_y() + (j * self.__cell_height))
        end_point: Point = Point(start_point.get_x() + self.__cell_width, start_point.get_y() + self.__cell_height)
        cell = Cell(start_point, end_point, top_wall, left_wall, bottom_wall, right_wall, self.__win)
        cell.draw(fill_color)
        self._animate()
        return cell

    def _animate(self, ani_speed = 0.05) -> None:
        """
        animates the drawing of each cell
        """
        if self.__win is not None:
            self.__win.redraw()
            sleep(ani_speed)

    def _break_walls_r(self, i, j) -> None:
        curr_cell: Cell = self._cells[i][j]
        if curr_cell.visited:
            return
        top_cell: Cell | None = self._cells[i][j-1] if j !=0 else None
        bottom_cell: Cell | None = self._cells[i][j+1] if j < len(self._cells) - 1 else None
        left_cell: Cell | None = self._cells[i-1][j] if i != 0 else None
        right_cell: Cell | None = self._cells[i+1][j] if i < len(self._cells) - 1 else None
        wall_info = []
        neighbors = [top_cell, bottom_cell, left_cell, right_cell]
        final_cell = self._cells[len(self._cells)-1][len(self._cells[0])-1]
        if final_cell in neighbors:
            print("final cell reached")
            return
        curr_cell.visited = True
        # --TODO: open some random walls on the cell
        if self._cells[i][j].has_top_wall:
            wall_info.append("top")
        if self._cells[i][j].has_left_wall:
            wall_info.append("left")
        if self._cells[i][j].has_bottom_wall:
            wall_info.append("bottom")
        if self._cells[i][j].has_right_wall:
            wall_info.append("right")
        rand_sel = randint(0, len(wall_info))
        self.__decide_wall(self._cells[i][j], wall_info[rand_sel], False)
        if top_cell is not None and not top_cell.visited:
            self._break_walls_r(i, j-1)
        if left_cell is not None and not left_cell.visited:
            self._break_walls_r(i-1, j)
        if bottom_cell is not None and not bottom_cell.visited:
            self._break_walls_r(i, j+1)
        if right_cell is not None and not right_cell.visited:
            self._break_walls_r(i+1, j)



    def __decide_wall(self, cell: Cell, wallname: str, has_wall: bool) -> None:
        """
        helper function to set wall property based on its name
        """
        match wallname:
            case "top":
                cell.has_top_wall = has_wall
            case "bottom":
                cell.has_bottom_wall = has_wall
            case "left":
                cell.has_left_wall = has_wall
            case "right":
                cell.has_right_wall = has_wall



def main():
    win = TWindow(1900, 900)
    Maze(5, 5, Point(100,100), 150, 150, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
