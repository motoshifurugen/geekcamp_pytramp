import collections
import tkinter
from tkinter import Button, Frame, font
from tkinter.constants import LEFT, UNDERLINE
from tkinter.font import Font
from typing import Sized

 

class StartWindow(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        master.geometry("600x400")
        master.resizable(False,False)
        self.master.title("PyTrump")
        #フォント
        self.default_font=tkinter.font.Font(family="System",size=48)
        self.button_font=tkinter.font.Font(family="System",size=36)

        #タイトルラベルフレーム
        title_label_frame=tkinter.Frame(self.master)
        title_label=tkinter.Label(title_label_frame,
            text="PyTrump",font=(self.default_font))
        title_label.pack(pady=50)
        #タイトルラベルフレームのパック
        title_label_frame.pack()
        
        #ボタンフレーム
        button_frame=tkinter.Frame(self.master)
        game_start_button=tkinter.Button(button_frame,text="Game Start",
            font=(self.button_font),command=lambda:self.gamestart())
        game_start_button.pack(side=LEFT,padx=50,pady=50)
        
        quit_button=tkinter.Button(button_frame,text="Quit",
            font=(self.button_font) ,command=lambda:self.quit())
        quit_button.pack(side=LEFT,padx=50,pady=50)
        #ボタンフレームのパック
        button_frame.pack()
        
    #テスト用
    def gamestart(self):
        print("gamestart test")
    #テスト用
    def quit(self):
        exit()

class ResultWindow(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        master.geometry("600x400")
        master.resizable(False,False)
        self.master.title("PyTrump")
        #フォント
        self.default_font=tkinter.font.Font(family="System",size=48)
        self.button_font=tkinter.font.Font(family="System",size=36)
        self.result_font=tkinter.font.Font(family="System",size=40,
            underline=True,weight="bold")

        #リザルトラベルフレーム
        result_label_frame=tkinter.Frame(self.master)
        result_label=tkinter.Label(result_label_frame,
            text="Result",font=(self.default_font))
        result_label.pack(pady=20)
        #リザルトラベルフレームのパック
        result_label_frame.pack()

        
        #win_loseラベルフレーム
        win_lose_frame=tkinter.Frame(self.master)
        win_label=tkinter.Label(win_lose_frame,
            text="Win",font=(self.result_font))
        lose_label=tkinter.Label(win_lose_frame,
            text="Lose",font=(self.result_font))
        flag=True    
        if flag==True:
            win_label.pack(pady=20)
        else:
            lose_label.pack(pady=20)
        win_lose_frame.pack()

        #ボタンフレーム
        button_frame=tkinter.Frame(self.master)
        replay_button=tkinter.Button(text="Replay",
            font=(self.button_font),command=lambda:self.replay())
        replay_button.pack(side=LEFT,padx=100,pady=50)
        
        quit_button=tkinter.Button(text="Quit",
            font=(self.button_font),command=lambda:self.quit())
        quit_button.pack(side=LEFT,padx=50,pady=50)
        #ボタンフレームのパック
        button_frame.pack()

    #テスト用
    def replay(self):
        print("replay")
    
    #テスト用
    def quit(self):
        exit()
    

#テスト用
window=tkinter.Tk()

test=ResultWindow(window)
test.mainloop()
"""
test=StartWindow(window)
test.mainloop()
"""