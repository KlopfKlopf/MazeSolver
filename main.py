from window import Window, Line, Point
win = Window(800, 600)

line1 = Line(Point(0, 0), Point(800, 600))
line2 = Line(Point(500, 100), Point(100, 500))
win.draw_line(line1, "red")
win.draw_line(line2, "blue")
win.wait_for_close()