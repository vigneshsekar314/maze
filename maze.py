from enum import unique
from window import TWindow
from point import Point
from cell import Cell
from time import sleep
from random import randint


class Maze:


    def __init__(self, rows: int, cols: int, start_pt: Point, cell_width: int, cell_height:int, win: TWindow | None = None, ani_speed: float | None = None, seed: int = 1) -> None:
        """
        creates a maze box with provided row and column count. It takes a start_pt argument to specify the starting x,y co-ordinate of the maze.
        cell_width and cell_height specifies the width and height dimensions of the cell.
        """
        self.__rows: int = rows
        self.__cols: int = cols
        print(f"rows: {rows}")
        print(f"cols: {cols}")
        self.__start_pt: Point = start_pt
        self.__cell_width: int = cell_width
        self.__cell_height: int = cell_height
        self.__win: TWindow | None = win
        self.ani_speed = ani_speed
        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        if rows !=0 and cols!=0:
            # self._cells[0][0].has_bottom_wall = False
            # self._cells[0][0].draw()
            # self._break_walls_r(0,0)
            print(f"seed: {seed}")
            self._generate_valid_path(seed,0,0,0)
            self.wall_randomize()
            # self._break_walls_r(0,0)
            self._animate()
            # self.__print_not_visited()

    def _create_cells(self) -> None:
        """
        creates cells in the window provided to the Maze class
        """
        for col in range(self.__cols):
            col_items = []
            for row in range(self.__rows):
                col_items.append(self._draw_cell(row, col))
            self._cells.append(col_items)

    def _break_entrance_and_exit(self):
        if len(self._cells) != 0 and len(self._cells[0]) != 0:
            self._cells[0][0] = self._draw_cell(0, 0, top_wall = False)
            end_x = self.__rows - 1
            end_y = self.__cols - 1
            if len(self._cells) == self.__rows and len(self._cells[end_x]) == self.__cols:
                self._cells[end_x][end_y] = self._draw_cell(end_x, end_y, bottom_wall = False)
                self._animate()

    def _draw_cell(self, i: int, j: int, top_wall: bool = True, left_wall: bool = True, bottom_wall: bool = True, right_wall: bool = True, fill_color: str = "blue") -> Cell:
        """
        draws each cell corresponding to the index position i and j. i represents the row index and j represents the column index.
        """
        start_point: Point = Point(self.__start_pt.get_x() + (i * self.__cell_width), self.__start_pt.get_y() + (j * self.__cell_height))
        end_point: Point = Point(start_point.get_x() + self.__cell_width, start_point.get_y() + self.__cell_height)
        cell = Cell(start_point, end_point, top_wall, left_wall, bottom_wall, right_wall, self.__win)
        cell.draw(fill_color)
        self._animate()
        return cell

    def _animate(self) -> None:
        """
        animates the drawing of each cell
        """
        if self.__win is not None:
            self.__win.redraw()
            sleep(self.ani_speed if self.ani_speed is not None else 0.05)

    def _break_walls_r(self, i, j, seed:int = 1, is_final_reached: bool = False) -> bool:
        sequence_nbr = 7745698 * seed

        curr_cell: Cell = self._cells[i][j]
        final_cell = self._cells[len(self._cells) - 1][len(self._cells[0])-1]
        if curr_cell.visited:
            return False
        curr_cell.visited = True
        top_cell: Cell | None = self._cells[i-1][j] if i !=0 else None
        bottom_cell: Cell | None = self._cells[i+1][j] if i < (self.__rows - 1) else None
        left_cell: Cell | None = self._cells[i][j-1] if j != 0 else None
        right_cell: Cell | None = self._cells[i][j+1] if j < (self.__cols - 1) else None
        wall_info = []
        if curr_cell.has_top_wall and i!=0:
            wall_info.append("top")
        if curr_cell.has_left_wall and j!=0:
            wall_info.append("left")
        if curr_cell.has_bottom_wall and i != (self.__rows - 1):
            wall_info.append("bottom")
        if curr_cell.has_right_wall and j != (self.__cols - 1):
            wall_info.append("right")
        if curr_cell.has_top_wall and top_cell is not None and not top_cell.has_bottom_wall:
            curr_cell.has_top_wall = False
        if curr_cell.has_left_wall and left_cell is not None and not left_cell.has_right_wall:
            curr_cell.has_left_wall = False
        if curr_cell.has_bottom_wall and bottom_cell is not None and not bottom_cell.has_top_wall:
            curr_cell.has_bottom_wall = False
        if curr_cell.has_right_wall and right_cell is not None and not right_cell.has_left_wall:
            curr_cell.has_right_wall = False
        if len(wall_info) != 0:
            rand_sel = randint(0, len(wall_info)-1)
            self.__decide_wall(i, j, wall_info[rand_sel])
        if top_cell is not None and not top_cell.visited:
            self._break_walls_r(i-1, j)
        if left_cell is not None and not left_cell.visited:
            self._break_walls_r(i, j-1)
        if bottom_cell is not None and not bottom_cell.visited:
            self._break_walls_r(i+1, j)
        if right_cell is not None and not right_cell.visited:
            self._break_walls_r(i, j+1)
        curr_cell.draw()
        return False

    def wall_randomize(self):
        for col in range(self.__cols):
            for row in range(self.__rows):
                cell = self._cells[row][col]
                if not cell.visited:
                    count = int(cell.has_right_wall) + int(cell.has_left_wall) + int(cell.has_top_wall) + int(cell.has_bottom_wall)
                    if count == 4:
                        # break some walls!
                        if row != 0:
                            cell.has_top_wall = False
                        elif row != self.__rows -1:
                            cell.has_bottom_wall = False
                        elif col != self.__cols -1:
                            cell.has_right_wall = False
                        elif col != 0:
                            cell.has_left_wall = False
                        cell.draw()



    def _generate_valid_path(self, seed: int = 1, row:int = 0, col:int = 0, digit_selector:int = 0, invalid_direction = "top", recursion_depth = 0) -> None:
        if row == self.__rows - 1 and col == self.__cols -1:
            print("destination reached")
            return
        unique_id = 772394268 * seed
        if recursion_depth >= (self.__rows * self.__cols):
            print("taking a lot of chances to reach destination")
        unique_directions = ["top", "left", "bottom", "right"] if recursion_depth < (self.__rows * self.__cols) else ["bottom", "right"]
        print(f"unique directions: {unique_directions}")
        self._cells[row][col].visited = True
        print(f"visited cell[{row}][{col}]")
        digit_selector = digit_selector + 1 if digit_selector < len(str(unique_id)) - 1 else 0
        recursion_depth += 1
        # pick a direction based on first number, then steps based on second number, go in that direction untill the end of maze or a visited cell. Keep repeating until you hit the final cell
        direction_num = self.get_digit(unique_id, digit_selector)
        valid_directions = unique_directions
        if invalid_direction in valid_directions:
            valid_directions.remove(invalid_direction)
        if row == 0 and "top" in valid_directions:
            valid_directions.remove("top")
        if row == self.__rows -1 and "bottom" in valid_directions:
            valid_directions.remove("bottom")
        if col == 0 and "left" in valid_directions:
            valid_directions.remove("left")
        if col == self.__cols - 1 and "right" in valid_directions:
            valid_directions.remove("right")
        if len(valid_directions) == 0:
            raise Exception("something went wrong with the logic")
        # adding a logic to prevent looping over the same direction
        if not row == self.__rows - 1  and not row == 0:
            wallcount = 0
            if self._cells[row][col].has_left_wall == False:
                wallcount += 1
            if self._cells[row][col].has_bottom_wall == False:
                wallcount += 1
            if self._cells[row][col].has_right_wall == False:
                wallcount += 1
            if self._cells[row][col].has_top_wall == False:
                wallcount += 1
            if wallcount >= 3 and "left" in valid_directions and len(valid_directions) != 1:
                valid_directions.remove("left")
            if wallcount >= 3 and "top" in valid_directions and len(valid_directions) != 1:
                valid_directions.remove("top")
            
        direction_num = direction_num % len(valid_directions)
        direction = valid_directions[direction_num]
        #update values in current and next cell and proceed to next cell
        cur = self._cells[row][col]
        match direction:
            case "top":
                next_cell = self._cells[row-1][col]
                cur.has_top_wall = False
                next_cell.has_bottom_wall = False
                cur.draw()
                next_cell.draw()
                self._generate_valid_path(seed, row-1, col, digit_selector, "bottom", recursion_depth)
            case "left":
                next_cell = self._cells[row][col-1]
                cur.has_left_wall = False
                next_cell.has_right_wall = False
                cur.draw()
                next_cell.draw()
                cur.draw()
                next_cell.draw()
                self._generate_valid_path(seed, row, col-1, digit_selector, "right", recursion_depth)
            case "bottom":
                next_cell = self._cells[row + 1][col]
                cur.has_bottom_wall = False
                next_cell.has_top_wall = False
                cur.draw()
                next_cell.draw()
                self._generate_valid_path(seed, row + 1, col, digit_selector, "top", recursion_depth) 
            case "right":
                next_cell = self._cells[row][col + 1]
                cur.has_right_wall = False
                next_cell.has_left_wall = False
                cur.draw()
                next_cell.draw()
                self._generate_valid_path(seed, row, col+1, digit_selector, "left", recursion_depth)
            case _:
                raise Exception("something went wrong with the direction logic")

    def get_digit(self, num: int, pos: int) -> int:
        return int(str(num)[pos])

    def __decide_wall(self, i: int, j: int, wallname: str) -> None:
        """
        helper function to set wall property based on its name
        """
        match wallname:
            case "top":
                self._cells[i][j].has_top_wall = False
            case "bottom":
                self._cells[i][j].has_bottom_wall = False
            case "left":
                self._cells[i][j].has_left_wall = False
            case "right":
                self._cells[i][j].has_right_wall = False
            case _:
                raise Exception("this case is not valid")


def main():
    win = TWindow(1900, 900)
    Maze(5, 5, Point(100,100), 150, 150, win)
    win.wait_for_close()
    # test1 = 1234567
    # m = Maze(10,10, Point(10,10), 50, 50)
    # print(m.get_digit(test1, 1))


if __name__ == "__main__":
    main()
