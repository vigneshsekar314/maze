from point import Point
from line import Line
from window import TWindow
from typing import Type, Tuple


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

    def draw_move(self, to_cell, undo: bool = False) -> None:
        """
        Draws a line from the center of this cell to the center of the other cell in the argument.
        If undo is True, draws a gray line, else it draws a red line.
        """
        filcol = "gray" if undo else "red"
        from_center = self.get_center(self)
        to_center = self.get_center(to_cell)
        # print(f"self.topleft: {self._top_left}")
        # print(f"self.topright: {self._top_right}")
        # print(f"self.bottomleft: {self._bottom_left}")
        # print(f"self.bottomright: {self._bottom_right}")
        # print(f"to_cell.topleft: {to_cell._top_left}")
        # print(f"to_cell.topright: {to_cell._top_right}")
        # print(f"to_cell.bottomleft: {to_cell._bottom_left}")
        # print(f"to_cell.bottomright: {to_cell._bottom_right}")
        # print(f"self.has_left: {self.has_left_wall}")
        # print(f"self.has_right: {self.has_right_wall}")
        # print(f"self.has_bottom: {self.has_bottom_wall}")
        # print(f"self.has_top: {self.has_top_wall}")

        # print(f"to_cell.has_left: {to_cell.has_left_wall}")
        # print(f"to_cell.has_right: {to_cell.has_right_wall}")
        # print(f"to_cell.has_bottom: {to_cell.has_bottom_wall}")
        # print(f"to_cell.has_top: {to_cell.has_top_wall}")

        is_right = (not (self.has_right_wall or to_cell.has_left_wall)) and (self._top_left.get_x() <= to_cell._top_left.get_x())
        is_top = (not (self.has_top_wall or to_cell.has_bottom_wall)) and (self._top_left.get_y() >= to_cell._bottom_left.get_y())
        is_bottom = (not (self.has_bottom_wall or to_cell.has_top_wall)) and (self._bottom_left.get_y() <= to_cell._top_left.get_y())
        is_left = (not (self.has_left_wall or to_cell.has_right_wall)) and (self._top_left.get_x() >= to_cell._top_left.get_x())
        # print(f"is_right: {is_right}")
        # print(f"is_left: {is_left}")
        # print(f"is_top: {is_top}")
        # print(f"is_bottom: {is_bottom}")

        # print(f"is_right2: {self._top_left.get_x() >= to_cell._top_left.get_x()} and self.topleft: {self._top_left.get_x()} and to_cell.topleft: {to_cell._top_left.get_x()}")
        # print(f"is_left2: {self._top_left.get_x() >= to_cell._top_right.get_x()} and self.topleft: {self._top_left.get_x()} and to_cell.topright: {to_cell._top_right.get_x()}")
        # print(f"is_top2: {self._top_left.get_y() >= to_cell._bottom_left.get_y()} and self.topleft: {self._top_left.get_y()} and to_cell.bottomleft: {to_cell._bottom_right.get_y()}")
        # print(f"is_bottom2: {self._bottom_left.get_y() <= to_cell._top_left.get_y()} and self.bottomleft: {self._bottom_left.get_y()} and to_cell.topleft: {to_cell._top_left.get_y()}")
        if is_right or is_top or is_bottom or is_left:
            self._win.draw_line(Line(from_center, to_center), fill_color=filcol)

    def get_center(self, cell):
        """
        refactor this method to make it static
        """
        center_point_x = (cell._top_left.get_x() + cell._top_right.get_x()) // 2
        center_point_y = (cell._top_left.get_y() + cell._bottom_left.get_y()) // 2
        return Point(center_point_x, center_point_y)

