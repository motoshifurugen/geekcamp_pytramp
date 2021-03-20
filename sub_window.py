import tkinter
from tkinter.font import Font
from typing import Sized
class WindowTemplate(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyTrump")
        self.geometry("400x300")
    
class StartWindow(WindowTemplate):
    def __init__(self):
        super().__init__()
        title_font=tkinter.font.Font(family="System",size=48)
        label=tkinter.Label(
            text="PyTrump",font=(title_font))
        label.place(x=100,y=60)
        game_start_button=tkinter.Button(text="Game Start",command=lambda:self.gamestart())
        quit_button=tkinter.Button(text="Quit",command=lambda:self.quit())
        game_start_button.place(x=100,y=170)
        quit_button.place(x=250,y=170)
    
    #テスト用
    def gamestart(self):
        print("gamestart test")
    #テスト用
    def quit(self):
        exit()

#テスト用
test=StartWindow()
test.mainloop()