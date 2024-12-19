from window import Window
from cell import Cell

win = Window(800, 600)

# cell = Cell(100, 300, 500, 600, win, has_right_wall=False)
# cell.draw()

# cell = Cell(150, 200, 225, 300, win, has_top_wall=False)
# cell.draw()

cell = Cell(250, 200, 350, 300, win, has_left_wall= False)
cell.draw()
win.wait_for_close()