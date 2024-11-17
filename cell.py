from point import Point
from line import Line
from window import TWindow


class Cell:

    """
    Represents a cell in a maze.
    """

    def __init__(self, top_left: Point, bottom_right: Point, has_top_wall: bool, has_left_wall: bool, has_bottom_wall: bool, has_right_wall: bool, win: TWindow | None = None) -> None:
        """
        Represents a cell in a maze. It takes a TWindow object in which it exists. Top_left is the top left (x,y) co-ordinate and bottom_right is the bottom-right (x,y) co-ordinate.
        Four other booleans indicate if there should be a wall in the cell.
        """
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._top_right = Point(x=self._bottom_right.get_x(), y=self._top_left.get_y())
        self._bottom_left = Point(x=self._top_left.get_x(), y=self._bottom_right.get_y())
        self.visited = False

    def draw(self, fill_color: str = "blue") -> None:
        """
        draws a cell in the maze.
        """
        if self._win is not None:
            self._win.draw_line(Line(self._top_left, self._top_right), fill_color=fill_color if self.has_top_wall else "white")
            self._win.draw_line(Line(self._top_left, self._bottom_left), fill_color=fill_color if self.has_left_wall else "white")
            self._win.draw_line(Line(self._bottom_left, self._bottom_right), fill_color=fill_color if self.has_bottom_wall else "white")
            self._win.draw_line(Line(self._top_right, self._bottom_right), fill_color=fill_color if self.has_right_wall else "white")

    def draw_move(self, to_cell, undo: bool = False) -> None:
        """
        Draws a line from the center of this cell to the center of the other cell in the argument.
        If undo is True, draws a gray line, else it draws a red line.
        """
        filcol = "gray" if undo else "red"
        from_center = self.get_center(self)
        to_center = self.get_center(to_cell)

        is_right = (not (self.has_right_wall or to_cell.has_left_wall)) and (self._top_left.get_x() < to_cell._top_left.get_x())
        is_top = (not (self.has_top_wall or to_cell.has_bottom_wall)) and (self._top_left.get_y() >= to_cell._bottom_left.get_y())
        is_bottom = (not (self.has_bottom_wall or to_cell.has_top_wall)) and (self._bottom_left.get_y() <= to_cell._top_left.get_y())
        is_left = (not (self.has_left_wall or to_cell.has_right_wall)) and (self._top_left.get_x() > to_cell._top_left.get_x())
        # print(f"isright, istop, isbottom, isleft: {is_right}, { is_top }, { is_bottom }, { is_left }")
        if is_right or is_top or is_bottom or is_left:
            if self._win is not None:
                self._win.draw_line(Line(from_center, to_center), fill_color=filcol)

    def get_center(self, cell):
        """
        refactor this method to make it static
        """
        center_point_x = (cell._top_left.get_x() + cell._top_right.get_x()) // 2
        center_point_y = (cell._top_left.get_y() + cell._bottom_left.get_y()) // 2
        return Point(center_point_x, center_point_y)

def main():
    # test client
    win = TWindow(1900,900)
    c = Cell(Point(50,100), Point(500,200), True, True, False, True, win)
    c1 = Cell(Point(50,200), Point(500,400), False, True, True, True, win)
    c.draw()
    c1.draw()
    c.draw_move(c1)

    #running the window
    win.wait_for_close()

if __name__ == "__main__":
    main()
