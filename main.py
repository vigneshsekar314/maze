from window import TWindow
from line import Line
from point import Point

def main():
    win = TWindow(800, 600)
    aline = Line(Point(100,100), Point(550,550))
    bline = Line(Point(100,100), Point(100,550))
    cline = Line(Point(100,550), Point(550,550))
    win.draw_line(aline,"red")
    win.draw_line(bline,"red")
    win.draw_line(cline,"red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
