from window import TWindow
from point import Point
from cell import Cell
from random import randint


def main():
    win = TWindow(800, 600)
    # outerbox = get_cell(win, [(100,100), (1200,700),[True,True,True,True]])
    # outerbox.draw()



    cell_to_draw = [
        [(100,100),(500,500), [rand_bool(), rand_bool(),rand_bool(),rand_bool()]],
        [(600,200),(900,500), [rand_bool(), rand_bool(),rand_bool(),rand_bool()]],
        [(1200,200),(1300,500), [rand_bool(), rand_bool(),rand_bool(),rand_bool()]]
    ]
    # cell_to_draw = [
    #     [(100,100),(500,500), [True, True,True,False]],
    #     [(600,200),(900,500), [True, False,True,True]],
    #     [(1200,200),(1300,500), [True, True,True,True]]
    # ]

    for cell in cell_to_draw:
        c = get_cell(win, cell)
        c.draw()
    c1 = get_cell(win, cell_to_draw[0])
    c2 = get_cell(win, cell_to_draw[1])
    c1.draw_move(c2)
    win.wait_for_close()

def get_cell(win, cell) -> Cell:
    return Cell(win=win, top_left=Point(cell[0][0],cell[0][1]), bottom_right=Point(cell[1][0],cell[1][1]), has_top_wall=cell[2][0], has_left_wall=cell[2][1], has_bottom_wall=cell[2][2], has_right_wall=cell[2][3])

def rand_bool() -> bool:
    return randint(0,1) == 0

if __name__ == "__main__":
    main()
