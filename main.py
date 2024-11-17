from window import TWindow
from point import Point
from cell import Cell
from random import randint
from maze import Maze
from sys import argv


def main():
    win = TWindow(800, 600)
    seed = 1
    if len(argv) > 1:
        seed = int(argv[1])
    Maze(10,10, Point(10,10), 50, 50, win, 0.01, seed)

    win.wait_for_close()

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
