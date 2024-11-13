class Point:

    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __repr__(self) -> str:
        return f"({self.__x},{self.__y})"
