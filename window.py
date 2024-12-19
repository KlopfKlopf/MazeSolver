from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("MazeSolver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__isrunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__isrunning = True
        while self.__isrunning:
            self.redraw()
    
    def close(self):
        self.__isrunning = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
            canvas.create_line(self.p1.x,  self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width = 2)

class Cell:

    def __init__(self, x1, y1 , x2, y2, win, has_left_wall = True, has_right_wall = True, has_top_wall = True, has_bottom_wall = True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def draw(self):
        if self.has_left_wall:
          line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
          self.__win.draw_line(line)
        if self.has_right_wall:
          line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
          self.__win.draw_line(line)
        if self.has_top_wall:
          line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
          self.__win.draw_line(line)
        if self.has_bottom_wall:
          line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
          self.__win.draw_line(line)

