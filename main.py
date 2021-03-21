import collections
import tkinter as tk
from tkinter import font
from tkinter.constants import UNDERLINE
from tkinter.font import Font
from typing import Sized
from war import *
import random

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
        self.label.place(x=200,y=100)
        #self.label.grid(row=0,column=1,columnspan=3,padx=210,pady=50)
        self.game_start_button = tk.Button(master,text="game start",font=(self.button_font),width=10,command=self.buttonClickNext)
        self.quit_button = tk.Button(master,text="quit",font=(self.button_font),width=10,command=exit)
        self.game_start_button.place(x=20,y=300)
        self.quit_button.place(x=300,y=300)
        #self.game_start_button.grid(row=2,column=1,padx=60,pady=40)
        #self.quit_button.grid(row=2,column=2,padx=60,pady=40)

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
        #self.label.grid(row=0,column=1,columnspan=3,padx=210,pady=50)
        self.restart_button = tk.Button(master,text="restart",font=(self.button_font),width=10,command=self.buttonClick)
        self.quit_button = tk.Button(master,text="quit",font=(self.button_font),width=10,command=exit)
        self.restart_button.place(x=20,y=300)
        self.quit_button.place(x=300,y=300)
        #self.restart_button.grid(row=2,column=1,padx=60,pady=40)
        #self.quit_button.grid(row=2,column=2,padx=60,pady=40)


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
        self.label.place(x=250,y=100)
        #self.label.grid(row=0,column=1,columnspan=3,padx=210,pady=50)
        self.result_button = tk.Button(master,text="result",font=(self.button_font),width=10,command=self.buttonClick)
        self.trump_1_button = tk.Button(master,text="Ace",font=(self.button_font),width=1,command=lambda: self.func(14,self.winFlag))
        self.trump_2_button = tk.Button(master,text="2",font=(self.button_font),width=1,command=lambda: self.func(2,self.winFlag))
        self.trump_3_button = tk.Button(master,text="3",font=(self.button_font),width=1,command=lambda: self.func(3,self.winFlag))
        self.trump_4_button = tk.Button(master,text="4",font=(self.button_font),width=1,command=lambda: self.func(4,self.winFlag))
        self.trump_5_button = tk.Button(master,text="5",font=(self.button_font),width=1,command=lambda: self.func(5,self.winFlag))
        self.trump_6_button = tk.Button(master,text="6",font=(self.button_font),width=1,command=lambda: self.func(6,self.winFlag))
        self.trump_7_button = tk.Button(master,text="7",font=(self.button_font),width=1,command=lambda: self.func(7,self.winFlag))
        self.trump_8_button = tk.Button(master,text="8",font=(self.button_font),width=1,command=lambda: self.func(8,self.winFlag))
        self.trump_9_button = tk.Button(master,text="9",font=(self.button_font),width=1,command=lambda: self.func(9,self.winFlag))
        self.trump_10_button = tk.Button(master,text="10",font=(self.button_font),width=1,command=lambda: self.func(10,self.winFlag))
        self.trump_11_button = tk.Button(master,text="11",font=(self.button_font),width=1,command=lambda: self.func(11,self.winFlag))
        self.trump_12_button = tk.Button(master,text="12",font=(self.button_font),width=1,command=lambda: self.func(12,self.winFlag))
        self.trump_13_button = tk.Button(master,text="13",font=(self.button_font),width=1,command=lambda: self.func(13,self.winFlag))
        self.result_button.place(x=0,y=300)
        self.trump_1_button.place(x=40,y=350)
        self.trump_2_button.place(x=80,y=350)
        self.trump_3_button.place(x=120,y=350)
        self.trump_4_button.place(x=160,y=350)
        self.trump_5_button.place(x=200,y=350)
        self.trump_6_button.place(x=240,y=350)
        self.trump_7_button.place(x=280,y=350)
        self.trump_8_button.place(x=320,y=350)
        self.trump_9_button.place(x=360,y=350)
        self.trump_10_button.place(x=400,y=350)
        self.trump_11_button.place(x=440,y=350)
        self.trump_12_button.place(x=480,y=350)
        self.trump_13_button.place(x=500,y=350)
        #self.result_button.grid(row=2,column=1,padx=60,pady=40)
        #self.trump_1_button.grid(row=3,column=1,padx=60,pady=40)
        #self.trump_2_button.grid(row=3,column=2,padx=60,pady=40)
        #self.trump_2_button.grid(row=3,column=3,padx=60,pady=40)

        # game variables
        self.player = Player("player")
        self.cpu = Player("cpu")
        # 1:player win  2:cpu win 0:draw
        self.winFlag = 0



    def buttonClick(self):
        start.buttonClickResult()
    
    # カード選択&デッキから取り出し
    def pickCard(self,card,player):
        player.deck.removeCard(card)

    # カード比較
    def cardComparison(self,playerCard,cpuCard,flag):
        if playerCard == cpuCard:
            flag = 0
        elif playerCard > cpuCard:
            flag = 1
        else:
            flag = 2
        return flag

    def func(self,playerCard,flag):
        # 手札からカード取り出し
        cpuCard = random.choice(self.cpu.deck.inHandCards[2:15])
        self.pickCard(playerCard,self.player)
        self.pickCard(cpuCard,self.cpu)

        # カード比較
        flagResult = self.cardComparison(playerCard=playerCard,cpuCard=cpuCard,flag=flag)
        if flagResult == 1:
            print("player win!")
            self.player.numWins += 1
        elif flagResult == 2:
            print("cpu win!")
            self.cpu.numWins += 1

        return flagResult


win = tk.Tk()
start = StartWindow(win)
start.mainloop()