from window import Line, Point

class Cell:

    def __init__(self, x1, y1 , x2, y2, win, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
          line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
          self._win.draw_line(line)
        if self.has_right_wall:
          line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
          self._win.draw_line(line)
        if self.has_top_wall:
          line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
          self._win.draw_line(line)
        if self.has_bottom_wall:
          line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
          self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
      center_x = self._x1 + ((self._x2 - self._x1) / 2)
      center_y = self._y1 + ((self._y2 - self._y1) / 2)

      to_center_x = to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2)
      to_center_y = to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2)

      line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))
      fill_color = "red"
      
      if undo:
        fill_color = "grey"
      
      self._win.draw_line(line, fill_color)
