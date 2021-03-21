import collections
import tkinter as tk
from tkinter import font
from tkinter.constants import UNDERLINE
from tkinter.font import Font
from typing import Sized, SupportsIndex
from war import *
import random
from tkinter.constants import BOTH, CENTER, E, LEFT

class StartWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        master.geometry("600x400")
        master.title("Pytrump")
        self.default_font = tk.font.Font(family="System",size=48)
        self.button_font = tk.font.Font(family="System",size=36)

        self.window = []
        self.game = []
        self.result =[]

        self.label = tk.Label(master,text="Pytrump",font=(self.default_font))
        #self.label.place(x=200,y=100)
        self.label.pack()
        self.game_start_button = tk.Button(master,text="game start",font=(self.button_font),width=10,command=self.buttonClickGame)
        self.quit_button = tk.Button(master,text="quit",font=(self.button_font),width=10,command=exit)
        #self.game_start_button.place(x=20,y=300)
        #self.quit_button.place(x=300,y=300)
        self.game_start_button.pack()
        self.quit_button.pack()

    def buttonClickResult(self):
        self.window.append(tk.Toplevel())

        if len(self.result) == 1:
            r = self.result.pop()
            r.master.destroy()
        self.result.append(ResultWindow(self.window[len(self.window)-1]))

    def buttonClickNext(self):
        self.window.append(tk.Toplevel())

        if len(self.game) == 1:
            g = self.game.pop()
            g.master.destroy()
        self.game.append(NextWindow(self.window[len(self.window)-1]))

    def buttonClickGame(self):
        self.window.append(tk.Toplevel())

        if len(self.game) == 1:
            g = self.game.pop()
            g.master.destroy()
        self.game.append(GameWindow(self.window[len(self.window)-1]))

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
        self.restart_button = tk.Button(master,text="restart",font=(self.button_font),width=10,command=self.buttonClick)
        self.quit_button = tk.Button(master,text="quit",font=(self.button_font),width=10,command=exit)
        self.restart_button.place(x=20,y=300)
        self.quit_button.place(x=300,y=300)


    def buttonClick(self):
        start.buttonClickGame()

class GameWindow(tk.Frame):
    def __init__(self,master=None):
        #tk.Frame.__init__(self,master)
        super().__init__(master)
        master.title("PyTrump")
        master.geometry("900x700")
        master.resizable(False,False)
        
        self.img_sample1="img\sample1.png"

        # game variables
        self.player = Player("player")
        self.cpu = Player("cpu")
        # 1:player win  2:cpu win 0:draw
        self.winFlag = 0
        # turn
        self.turn = 1

        self.pack()
        self.create_widget()


    def create_widget(self):
        #フォント
        self.default_font=tk.font.Font(family="System",size=48)
        self.button_font=tk.font.Font(family="System",size=36)
        self.label_font=tk.font.Font(family="System",size=24)
        
        #ゲームカウントフレーム
        game_count_frame=tk.Frame(self.master)
        game_count_label=tk.Label(game_count_frame,
            text="{}ゲーム目".format(self.turn),font=(self.label_font),
            anchor=tk.W)
        space_fill_label=tk.Label(game_count_frame,text="　　　　　　    ")
        game_result_label=tk.Label(game_count_frame,
            text="直前のゲーム結果:{}".format(self.game_result()),font=(self.label_font)
            ,anchor=tk.E)
        game_count_label.pack(side=tk.LEFT)
        space_fill_label.pack(side=tk.LEFT)
        game_result_label.pack(side=tk.RIGHT)
        #ゲームカウントフレームをパック
        game_count_frame.pack(side=tk.TOP)

        #相手プレイヤーのデッキフレーム
        player2_deck_frame=tk.Frame(self.master)
        player2_deck_list=[]
        #for _ in range(13):
        #    player2_deck_list.append(tk.Button(player2_deck_frame,text="{}".format(_+1),
        #        font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4))
        self.trump_1_button = tk.Button(player2_deck_frame,text="1",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_2_button = tk.Button(player2_deck_frame,text="2",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_3_button = tk.Button(player2_deck_frame,text="3",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_4_button = tk.Button(player2_deck_frame,text="4",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_5_button = tk.Button(player2_deck_frame,text="5",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_6_button = tk.Button(player2_deck_frame,text="6",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_7_button = tk.Button(player2_deck_frame,text="7",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_8_button = tk.Button(player2_deck_frame,text="8",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_9_button = tk.Button(player2_deck_frame,text="9",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_10_button = tk.Button(player2_deck_frame,text="10",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_11_button = tk.Button(player2_deck_frame,text="11",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_12_button = tk.Button(player2_deck_frame,text="12",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_13_button = tk.Button(player2_deck_frame,text="13",font=(self.label_font),width=2).pack(side=tk.LEFT,padx=4,pady=4)
        #相手プレイヤーのデッキフレームをパック
        player2_deck_frame.pack()
        
        #複合フレーム
        multi_frame=tk.Frame(self.master)
        #相手の獲得ゲーム数
        player2_game_count_label=tk.Label(multi_frame,
            text="勝利数 {}".format(self.cpu.numWins),font=(self.label_font))
        player2_game_count_label.pack(side=LEFT)
        
        #相手のカードの画像表示
        player2_card=tk.PhotoImage(file="")
        canvas=tk.Canvas(bg="white",width=100,height=200)
        canvas.pack() 
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        canvas.create_image(0,0,image=player2_card)
        
        #自分のカードの画像表示
        player1_card=tk.PhotoImage(file="")
        canvas=tk.Canvas(bg="white",width=100,height=200)
        canvas.pack()
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        canvas.create_image(0,0,image=player1_card)
        
         #自分の獲得ゲーム数
        player1_game_count_label=tk.Label(multi_frame,
            text="勝利数 {}".format(self.player.numWins),font=(self.label_font))
        player1_game_count_label.pack(side=LEFT)
        #複合フレームのパック
        multi_frame.pack()
        
        
        #自分プレイヤーのデッキフレーム
        player1_deck_frame=tk.Frame(self.master)
        player1_deck_list=[]
        #for i in range(0,13):
        #    player1_deck_list.append(tk.Button(player1_deck_frame,text="{}".format(i+1),
        #        font=(self.label_font),width=2 ,command=lambda:self.func(i+1,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4))
        self.trump_1_button = tk.Button(player1_deck_frame,text="1",font=(self.label_font),width=2,command=lambda: self.func(14,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_2_button = tk.Button(player1_deck_frame,text="2",font=(self.label_font),width=2,command=lambda: self.func(2,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_3_button = tk.Button(player1_deck_frame,text="3",font=(self.label_font),width=2,command=lambda: self.func(3,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_4_button = tk.Button(player1_deck_frame,text="4",font=(self.label_font),width=2,command=lambda: self.func(4,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_5_button = tk.Button(player1_deck_frame,text="5",font=(self.label_font),width=2,command=lambda: self.func(5,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_6_button = tk.Button(player1_deck_frame,text="6",font=(self.label_font),width=2,command=lambda: self.func(6,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_7_button = tk.Button(player1_deck_frame,text="7",font=(self.label_font),width=2,command=lambda: self.func(7,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_8_button = tk.Button(player1_deck_frame,text="8",font=(self.label_font),width=2,command=lambda: self.func(8,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_9_button = tk.Button(player1_deck_frame,text="9",font=(self.label_font),width=2,command=lambda: self.func(9,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_10_button = tk.Button(player1_deck_frame,text="10",font=(self.label_font),width=2,command=lambda: self.func(10,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_11_button = tk.Button(player1_deck_frame,text="11",font=(self.label_font),width=2,command=lambda: self.func(11,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_12_button = tk.Button(player1_deck_frame,text="12",font=(self.label_font),width=2,command=lambda: self.func(12,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        self.trump_13_button = tk.Button(player1_deck_frame,text="13",font=(self.label_font),width=2,command=lambda: self.func(13,self.winFlag)).pack(side=tk.LEFT,padx=4,pady=4)
        
        #自分プレイヤーのデッキフレームをパック
        player1_deck_frame.pack()

    #テスト用
    def game_count(self):
        GAME_COUNT=10
        return GAME_COUNT
    #テスト用
    def game_result(self):
        GAME_RESULT="WIN"
        return GAME_RESULT
    #テスト用
    def callback(self,x):
        print("ボタン{}".format(x))
    #テスト用
    def player2_game_count(self):
        GAME_COUNT=5
        return GAME_COUNT
    #テスト用
    def player1_game_count(self):
        GAME_COUNT=8
        return GAME_COUNT



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

        # GUI処理呼び出し

        if self.turn == 13:
            self.buttonClick()

        # turnを1増やす
        self.turn += 1

        return flagResult
    
    def buttonClick(self):
        start.buttonClickResult()


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

        # game variables
        self.player = Player("player")
        self.cpu = Player("cpu")
        # 1:player win  2:cpu win 0:draw
        self.winFlag = 0
        # turn
        self.turn = 1


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

        # GUI処理呼び出し

        if self.turn == 13:
            self.buttonClick()

        # turnを1増やす
        self.turn += 1

        return flagResult


win = tk.Tk()
start = StartWindow(win)
start.mainloop()