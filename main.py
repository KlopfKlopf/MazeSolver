from window import Window
from cell import Cell

win = Window(800, 600)

# cell = Cell(100, 300, 500, 600, win, has_right_wall=False)
# cell.draw()

cell1 = Cell(150, 200, 200, 250, win)
cell1.draw()

cell2 = Cell(250, 200, 300, 250, win)
cell2.draw()

cell1.draw_move(cell2)
win.wait_for_close()