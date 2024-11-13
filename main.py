from tkinter import Tk, BOTH, Canvas

class TWindow():

    """
    Window class used for building mazes in TKinter
    """

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("My Maze solver")
        self.__canvas = Canvas(self.__root, bg="white", height=self.__height, width=self.__width)
        self.__isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.pack(expand=1, fill=BOTH)

    def set_title(self, title: str) -> None:
        """
        Sets title
        """
        self.__root.title(title)

    def redraw(self) -> None:
        """
        To redraw the window. It calls update_idletasks() and update() methods
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()

    def close(self) -> None:
        self.__isrunning = False
        print("closing window")

def main():
    win = TWindow(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()
