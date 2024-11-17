from window import TWindow
from point import Point
from cell import Cell
from time import sleep
from random import randint


class Maze:


    def __init__(self, rows: int, cols: int, start_pt: Point, cell_width: int, cell_height:int, win: TWindow | None = None, ani_speed: float | None = None) -> None:
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
        self.ani_speed = ani_speed
        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        if rows !=0 and cols!=0:
            self._break_walls_r(0,0)
            self._animate()
            # self.__print_not_visited()

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

    def _animate(self) -> None:
        """
        animates the drawing of each cell
        """
        if self.__win is not None:
            self.__win.redraw()
            sleep(self.ani_speed if self.ani_speed is not None else 0.05)

    def _break_walls_r(self, i, j, seed:int = 1, is_final_reached: bool = False) -> bool:
        # if is_final_reached:
        #     return True
        start_cell = self._cells[0][0] if len(self._cells) != 0 and len(self._cells[0]) != 0 else None
        sequence_nbr = 7745698 * seed

        curr_cell: Cell = self._cells[i][j]
        final_cell = self._cells[len(self._cells) - 1][len(self._cells[0])-1]
        if curr_cell.visited:
            return False
        curr_cell.visited = True
        # if curr_cell == final_cell:
            # return True
        top_cell: Cell | None = self._cells[i][j-1] if j !=0 else None
        bottom_cell: Cell | None = self._cells[i][j+1] if j < len(self._cells) - 1 else None
        left_cell: Cell | None = self._cells[i-1][j] if i != 0 else None
        right_cell: Cell | None = self._cells[i+1][j] if i < len(self._cells) - 1 else None
        wall_info = []
        # neighbors = [top_cell, bottom_cell, left_cell, right_cell]
        # if final_cell in neighbors:
        #     print("final cell reached")
        #     return True
        # --TODO: open some random walls on the cell
        if curr_cell.has_top_wall and j!=0:
            wall_info.append("top")
        if curr_cell.has_left_wall and i!=0:
            wall_info.append("left")
        if curr_cell.has_bottom_wall and j != (len(self._cells[0]) - 1):
            wall_info.append("bottom")
        if curr_cell.has_right_wall and i != (len(self._cells) - 1):
            wall_info.append("right")
        if curr_cell.has_top_wall and top_cell is not None and top_cell.has_bottom_wall:
            curr_cell.has_top_wall = False
            curr_cell.draw()
        if curr_cell.has_left_wall and left_cell is not None and left_cell.has_right_wall:
            curr_cell.has_left_wall = False
            curr_cell.draw()
        if curr_cell.has_bottom_wall and bottom_cell is not None and bottom_cell.has_top_wall:
            curr_cell.has_bottom_wall = False
            curr_cell.draw()
        if curr_cell.has_right_wall and right_cell is not None and right_cell.has_left_wall:
            curr_cell.has_right_wall = False
            curr_cell.draw()
        if len(wall_info) != 0:
            rand_sel = randint(0, len(wall_info)-1)
            print(f"cell {i},{j} will remove wall {wall_info[rand_sel]}")
            self.__decide_wall(i, j, wall_info[rand_sel], False)
        if top_cell is not None and not top_cell.visited:
            self._break_walls_r(i, j-1)
            # if is_final_reached:
            #     return True
        if left_cell is not None and not left_cell.visited:
            self._break_walls_r(i-1, j)
            # if is_final_reached:
            #     return True
        if bottom_cell is not None and not bottom_cell.visited:
            self._break_walls_r(i, j+1)
            # if is_final_reached:
            #     return True
        if right_cell is not None and not right_cell.visited:
            self._break_walls_r(i+1, j)
            # if is_final_reached:
            #     return True
        if self.__win is not None:
            self.__win.redraw()
        return False

    def _break_walls_rcopy(self, i, j, seed:int = 1, is_final_reached: bool = False) -> bool:
        start_cell = self._cells[0][0] if len(self._cells) != 0 and len(self._cells[0]) != 0 else None
        sequence_nbr = 7745698 * seed

        curr_cell: Cell = self._cells[i][j]
        final_cell = self._cells[len(self._cells) - 1][len(self._cells[0])-1]
        if curr_cell.visited:
            return False
        curr_cell.visited = True
        top_cell: Cell | None = self._cells[i][j-1] if j !=0 else None
        bottom_cell: Cell | None = self._cells[i][j+1] if j < len(self._cells) - 1 else None
        left_cell: Cell | None = self._cells[i-1][j] if i != 0 else None
        right_cell: Cell | None = self._cells[i+1][j] if i < len(self._cells) - 1 else None
        wall_info = []
        if curr_cell.has_top_wall and j!=0:
            wall_info.append("top")
        if curr_cell.has_left_wall and i!=0:
            wall_info.append("left")
        if curr_cell.has_bottom_wall and j != (len(self._cells[0]) - 1):
            wall_info.append("bottom")
        if curr_cell.has_right_wall and i != (len(self._cells) - 1):
            wall_info.append("right")
        if curr_cell.has_top_wall and top_cell is not None and top_cell.has_bottom_wall:
            curr_cell.has_top_wall = False
            curr_cell.draw()
        if curr_cell.has_left_wall and left_cell is not None and left_cell.has_right_wall:
            curr_cell.has_left_wall = False
            curr_cell.draw()
        if curr_cell.has_bottom_wall and bottom_cell is not None and bottom_cell.has_top_wall:
            curr_cell.has_bottom_wall = False
            curr_cell.draw()
        if curr_cell.has_right_wall and right_cell is not None and right_cell.has_left_wall:
            curr_cell.has_right_wall = False
            curr_cell.draw()
        if len(wall_info) != 0:
            rand_sel = randint(0, len(wall_info)-1)
            print(f"cell {i},{j} will remove wall {wall_info[rand_sel]}")
            self.__decide_wall(i, j, wall_info[rand_sel], False)
        if top_cell is not None and not top_cell.visited:
            self._break_walls_r(i, j-1)
        if left_cell is not None and not left_cell.visited:
            self._break_walls_r(i-1, j)
        if bottom_cell is not None and not bottom_cell.visited:
            self._break_walls_r(i, j+1)
        if right_cell is not None and not right_cell.visited:
            self._break_walls_r(i+1, j)
        if self.__win is not None:
            self.__win.redraw()
        return False

    def __print_not_visited(self):
        if len(self._cells) != 0 and len(self._cells[0]) !=0:
            for col in range(len(self._cells)):
                for row in range(len(self._cells[0])):
                    if not self._cells[col][row].visited:
                        print(f"cell [{col}][{row}] is not visited")

    def __decide_wall(self, i: int, j: int, wallname: str, has_wall: bool) -> None:
        """
        helper function to set wall property based on its name
        """
        cell = self._cells[i][j]
        match wallname:
            case "top":
                cell.has_top_wall = has_wall
                # print(f"top cell broken for cell[{i}][{j}]")
            case "bottom":
                cell.has_bottom_wall = has_wall
                # print(f"bottom cell broken for cell[{i}][{j}]")
            case "left":
                cell.has_left_wall = has_wall
                # print(f"left cell broken for cell[{i}][{j}]")
            case "right":
                cell.has_right_wall = has_wall
                # print(f"right cell broken for cell[{i}][{j}]")
        cell.draw()



def main():
    win = TWindow(1900, 900)
    Maze(5, 5, Point(100,100), 150, 150, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
