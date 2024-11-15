from unittest import TestCase, main
from maze import Maze
from point import Point
from random import randint

class MazeTest(TestCase):
    def test_maze_createmaze(self):
        for _ in range(10):
            rows = randint(0,10)
            cols = randint(0,10)
            m = Maze(rows, cols, Point(50,50), 50, 60)
            self.assertEqual(len(m._cells), cols)
            if len(m._cells) > 0:
                self.assertEqual(len(m._cells[0]), rows)

    def test_entrance_and_exit(self):
        rows = 10
        cols = 10
        ma = Maze(rows, cols, Point(50,50), 20, 20)
        self.assertEqual(ma._cells[0][0].has_left_wall, False)
        self.assertEqual(ma._cells[rows-1][cols-1].has_right_wall, False)

if __name__ == "__main__":
    main()
