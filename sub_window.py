import collections
import tkinter
from tkinter import font
from tkinter.constants import UNDERLINE
from tkinter.font import Font
from typing import Sized

class WindowTemplate(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyTrump")
        self.geometry("600x400")
        self.default_font=tkinter.font.Font(family="System",size=48)
        self.button_font=tkinter.font.Font(family="System",size=36)
        self.resizable(False,False)

class StartWindow(WindowTemplate):
    def __init__(self):
        super().__init__()
        title_label=tkinter.Label(
            text="PyTrump",font=(self.default_font))
        title_label.grid(row=0,column=1,columnspan=3,padx=210,pady=50)
        game_start_button=tkinter.Button(text="Game Start",
            font=(self.button_font),command=lambda:self.gamestart())
        quit_button=tkinter.Button(text="Quit",
            font=(self.button_font) ,command=lambda:self.quit())
        game_start_button.grid(row=2,column=1,padx=60,pady=40)
        quit_button.grid(row=2,column=2,padx=60,pady=40)
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
        result_label.grid(row=0,column=1,columnspan=3,padx=230,pady=10)
        self.result_font=tkinter.font.Font(family="System",size=40,
            underline=True,weight="bold")
        replay_button=tkinter.Button(text="Replay",
            font=(self.button_font),command=lambda:self.replay())
        quit_button=tkinter.Button(text="Quit",
            font=(self.button_font),command=lambda:self.quit())
        replay_button.grid(row=2,column=1,padx=50,pady=50)
        quit_button.grid(row=2,column=2,padx=0,pady=50)

    def display_result(self,result_flag):
        win_label=tkinter.Label(
            text="Win",font=(self.result_font))
        lose_label=tkinter.Label(
            text="Lose",font=(self.result_font))
        if result_flag==True:
            win_label.grid(row=1,column=1,columnspan=3,padx=100)
        else:
            lose_label.grid(row=1,column=1,columnspan=3,padx=100)
        #テスト用
        self.mainloop()

    #テスト用
    def replay(self):
        print("replay")
    
    #テスト用
    def quit(self):
        exit()
    

#テスト用
#test=ResultWindow()
#test.display_result(False)
test=StartWindow()
test.mainloop()