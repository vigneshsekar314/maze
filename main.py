from window import TWindow
from line import Line
from point import Point
from cell import Cell

def main():
    win = TWindow(800, 600)
    cell_to_draw = [
        [(100,100),(500,500), [True, True,True,True]],
        [(600,200),(900,500), [True, True,True,True]],
        [(1200,200),(1300,500), [True, True,True,True]],

    ]

    for cell in cell_to_draw:
        c = Cell(win=win, top_left=Point(cell[0][0],cell[0][1]), bottom_right=Point(cell[1][0],cell[1][1]), has_top_wall=cell[2][0], has_left_wall=cell[2][1], has_bottom_wall=cell[2][2], has_right_wall=cell[2][3])
        c.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
