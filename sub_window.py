import tkinter
from tkinter.constants import UNDERLINE
from tkinter.font import Font
from typing import Sized
class WindowTemplate(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyTrump")
        self.geometry("400x300")
        self.default_font=tkinter.font.Font(family="System",size=48)

class StartWindow(WindowTemplate):
    def __init__(self):
        super().__init__()
        title_label=tkinter.Label(
            text="PyTrump",font=(self.default_font))
        title_label.place(x=100,y=60)
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

class ResultWindow(WindowTemplate):
    def __init__(self):
        super().__init__()
        result_label=tkinter.Label(
            text="Result",font=(self.default_font))
        result_label.pack()
        self.result_font=tkinter.font.Font(family="System",size=40,underline=True,weight="bold")
        self.win_label=tkinter.Label(
            text="Win",font=(self.result_font))
        self.lose_label=tkinter.Label(
            text="Lose",font=(self.result_font))
        replay_button=tkinter.Button(text="Replay",command=lambda:self.replay())
        quit_button=tkinter.Button(text="Quit",command=lambda:self.quit())
        replay_button.place(x=100,y=200)
        quit_button.place(x=250,y=200)

    def display_result(self,result_flag):
        if result_flag==True:
            self.win_label.pack()
        else:
            self.lose_label.pack()
        #テスト用
        self.mainloop()

    #テスト用
    def replay(self):
        print("replay")
    
    #テスト用
    def quit(self):
        exit()
    

#テスト用
test=ResultWindow()
test.display_result(False)