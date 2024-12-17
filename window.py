from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "MazeSolver"
        self.__canvas = Canvas()
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
