from window import TWindow
from point import Point
from cell import Cell
from time import sleep


class Maze:


    def __init__(self, rows: int, cols: int, start_pt: Point, cell_width: int, cell_height:int, win: TWindow) -> None:
        """
        creates a maze box with provided row and column count. It takes a start_pt argument to specify the starting x,y co-ordinate of the maze.
        cell_width and cell_height specifies the width and height dimensions of the cell.
        """
        self.__rows: int = rows
        self.__cols: int = cols
        self.__start_pt: Point = start_pt
        self.__cell_width: int = cell_width
        self.__cell_height: int = cell_height
        self.__win: TWindow = win
        self._cells = []
        self._create_cells()

    def _create_cells(self) -> None:
        """
        creates cells in the window provided to the Maze class
        """
        for col in range(self.__cols):
            col_items = []
            for row in range(self.__rows):
                col_items.append(self._draw_cell(row, col))
            self._cells.append(col_items)

    def _draw_cell(self, i: int, j: int) -> Cell:
        """
        draws each cell corresponding to the index position i and j. i represents the row index and j represents the column index.
        """
        start_point: Point = Point(self.__start_pt.get_x() + (i * self.__cell_width), self.__start_pt.get_y() + (j * self.__cell_height))
        end_point: Point = Point(start_point.get_x() + self.__cell_width, start_point.get_y() + self.__cell_height)
        cell = Cell(self.__win, start_point, end_point, True, True, True, True)
        cell.draw()
        self._animate()
        return cell

    def _animate(self, ani_speed = 0.05) -> None:
        """
        animates the drawing of each cell
        """
        self.__win.redraw()
        sleep(ani_speed)

def main():
    win = TWindow(1900, 900)
    Maze(5, 5, Point(100,100), 150, 150, win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
