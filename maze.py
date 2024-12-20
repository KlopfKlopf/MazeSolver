from cell import Cell
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            inner_list = []
            for j in range(self._num_cols):
                inner_list.append(Cell(self._win))
            self._cells.append(inner_list)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        pos_x1 = self._x1 + (j * self._cell_size_x)
        pos_y1 = self._y1 + (i * self._cell_size_y)
        pos_x2 = pos_x1 + self._cell_size_x
        pos_y2 = pos_y1 + self._cell_size_y

        self._cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

