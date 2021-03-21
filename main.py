import collections
import tkinter as tk
from tkinter import font
from tkinter.constants import UNDERLINE
from tkinter.font import Font
from typing import Sized

class StartWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("600x400")
        master.title("Pytrump")
        self.default_font = tk.font.Font(family="System",size=48)
        self.button_font = tk.font.Font(family="System",size=36)

        self.window = []

        self.label = tk.Label(master,text="Pytrump",font=(self.default_font))
        self.label.place(x=220,y=100)
        self.button = tk.Button(master,text="result",font=(self.button_font),width=20,command=self.buttonClickNext)
        self.button.place(x=80,y=300)

    def buttonClickResult(self):
        self.window.append(tk.Toplevel())
        ResultWindow(self.window[len(self.window)-1])

    def buttonClickNext(self):
        self.window.append(tk.Toplevel())
        NextWindow(self.window[len(self.window)-1])

class ResultWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("600x400")
        master.title("Result")
        self.default_font = tk.font.Font(family="System",size=48)
        self.button_font = tk.font.Font(family="System",size=36)

        self.label = tk.Label(master,text="Result",font=(self.default_font))
        self.label.place(x=220,y=100)
        self.button = tk.Button(master,text="next",font=(self.button_font),width=20,command=self.buttonClick)
        self.button.place(x=80,y=300)

    def buttonClick(self):
        start.buttonClickNext()

class NextWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("600x400")
        master.title("Next")
        self.default_font = tk.font.Font(family="System",size=48)
        self.button_font = tk.font.Font(family="System",size=36)

        self.label = tk.Label(master,text="Next",font=(self.default_font))
        self.label.place(x=220,y=100)
        self.button = tk.Button(master,text="result",font=(self.button_font),width=20,command=self.buttonClick)
        self.button.place(x=80,y=300)


    def buttonClick(self):
        start.buttonClickResult()
    


win = tk.Tk()
start = StartWindow(win)
start.mainloop()