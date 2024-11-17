from window import TWindow
from point import Point
from cell import Cell
from random import randint
from maze import Maze


def main():
    win = TWindow(800, 600)
    # topleft_corner = (20,20)
    # bottomright_corner = (1900,980)
    # total_width = bottomright_corner[0] - topleft_corner[0]
    # total_height = bottomright_corner[1] - topleft_corner[1]
    # rows = 3
    # columns = 3
    # cell_width = total_width / rows
    # cell_height = total_height / columns
    # # total_cells = rows * columns
    # cell_list: dict[str, Cell] = {}
    # for col in range(columns):
    #     for row in range(rows):
    #         start_point = (int(topleft_corner[0] + (row * cell_width)), int(topleft_corner[1] + (col * cell_height)))
    #         end_point = (int(start_point[0] + cell_width), int(start_point[1] + cell_height))
    #         c = get_cell(win, [start_point, end_point, rand_walls(0.33)])
    #         c.draw()
    #         cell_list[str(row) + str(col)] = c

    # for col in range(columns):
    #     for row in range(rows):
    #             cur_cell = cell_list[str(row) + str(col)]
    #             topkey = str(row-1) + str(col) 
    #             bottomkey = str(row+1) + str(col) 
    #             rightkey = str(row) + str(col+1) 
    #             leftkey = str(row) + str(col-1) 
    #             # print(f"current cell index: {str(row) + str(col)}")
    #             if topkey in cell_list:
    #                 # print(f"topkey: {topkey}")
    #                 cur_cell.draw_move(cell_list[topkey])
    #             if bottomkey in cell_list:
    #                 # print(f"bottomkey: {bottomkey}")
    #                 cur_cell.draw_move(cell_list[bottomkey])
    #             if rightkey in cell_list:
    #                 # print(f"rightkey: {rightkey}")
    #                 cur_cell.draw_move(cell_list[rightkey])
    #             if leftkey in cell_list:
    #                 # print(f"leftkey: {leftkey}")
    #                 cur_cell.draw_move(cell_list[leftkey])
    Maze(10,10, Point(10,10), 20, 20, win)

    # outerbox = get_cell(win, [topleft_corner, bottomright_corner,[True,True,True,True]])
    # outerbox.draw()

    win.wait_for_close()

def get_cell(win, cell) -> Cell:
    return Cell(win=win, top_left=Point(cell[0][0],cell[0][1]), bottom_right=Point(cell[1][0],cell[1][1]), has_top_wall=cell[2][0], has_left_wall=cell[2][1], has_bottom_wall=cell[2][2], has_right_wall=cell[2][3])

def rand_bool(true_prob = 0.5) -> bool:
    """
    returns a random boolean. If true_prob is passed, then returns True based on probability passed
    """
    if true_prob != 0.5:
        return randint(1,100) <= (100 * true_prob)
    return randint(0,1) == 0

def rand_walls(true_prob = 0.5) -> list[bool]:
    """
    get randomized walls in a cell. If true_prob is passed, then returns walls based on probability passed
    """
    if true_prob != 0.5:
        return [rand_bool(true_prob), rand_bool(true_prob), rand_bool(true_prob), rand_bool(true_prob)]
    return [rand_bool(), rand_bool(), rand_bool(), rand_bool()]

if __name__ == "__main__":
    main()
