from point import Point
from line import Line
from window import TWindow


class Cell:

    """
    Represents a cell in a maze.
    """

    def __init__(self, win: TWindow, top_left: Point, bottom_right: Point, has_left_wall: bool, has_right_wall: bool, has_top_wall: bool, has_bottom_wall: bool) -> None:
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

    def draw(self) -> None:
        """
        draws a cell in the maze.
        """
        if self.has_top_wall:
            self._win.draw_line(Line(self._top_left, self._top_right))
        if self.has_left_wall:
            self._win.draw_line(Line(self._top_left, self._bottom_left))
        if self.has_bottom_wall:
            self._win.draw_line(Line(self._bottom_left, self._bottom_right))
        if self.has_right_wall:
            self._win.draw_line(Line(self._top_right, self._bottom_right))






