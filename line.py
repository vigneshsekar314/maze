from tkinter import Canvas
from point import Point

class Line:

    def __init__(self, pointA: Point, pointB: Point) -> None:
        self.__pointA = pointA
        self.__pointB = pointB

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        """
        creates a line using canvas.create_line method
        """
        canvas.create_line(self.__pointA.get_x(), self.__pointA.get_y(), self.__pointB.get_x(), self.__pointB.get_y(), fill=fill_color, width=2)
