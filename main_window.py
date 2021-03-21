import tkinter
from tkinter.constants import BOTH, CENTER, E, LEFT
from tkinter.font import Font
from typing import Sized, SupportsIndex

class GameWindow(tkinter.Frame):
    def __init__(self,master = None):
        tkinter.Frame.__init__(self,master)
        self.master.title("PyTrump")
        master.geometry("900x700")
        master.resizable(False,False)
        
        self.img_sample1="img\sample1.png"

        self.pack()
        self.create_widget()

    def create_widget(self):
        #フォント
        self.default_font=tkinter.font.Font(family="System",size=48)
        self.button_font=tkinter.font.Font(family="System",size=36)
        self.label_font=tkinter.font.Font(family="System",size=24)
        
        #ゲームカウントフレーム
        game_count_frame=tkinter.Frame(self.master)
        game_count_label=tkinter.Label(game_count_frame,
            text="{}ゲーム目".format(self.game_count()),font=(self.label_font),
            anchor=tkinter.W)
        space_fill_label=tkinter.Label(game_count_frame,text="　　　　　　    ")
        game_result_label=tkinter.Label(game_count_frame,
            text="直前のゲーム結果:{}".format(self.game_result()),font=(self.label_font)
            ,anchor=tkinter.E)
        game_count_label.pack(side=tkinter.LEFT)
        space_fill_label.pack(side=tkinter.LEFT)
        game_result_label.pack(side=tkinter.RIGHT)
        #ゲームカウントフレームをパック
        game_count_frame.pack(side=tkinter.TOP)

        #相手プレイヤーのデッキフレーム
        player2_deck_frame=tkinter.Frame(self.master)
        player2_deck_list=[]
        for _ in range(14):
            player2_deck_list.append(tkinter.Button(player2_deck_frame,text="{}".format(_),
                font=(self.label_font),width=2 ,command=lambda:self.callback(_)).pack(side=tkinter.LEFT,padx=4,pady=4))
        #相手プレイヤーのデッキフレームをパック
        player2_deck_frame.pack()
        
        #複合フレーム
        multi_frame=tkinter.Frame(self.master)
        #相手の獲得ゲーム数
        player2_game_count_label=tkinter.Label(multi_frame,
            text="勝利数 {}".format(self.player2_game_count()),font=(self.label_font))
        player2_game_count_label.pack(side=LEFT)
        
        #相手のカードの画像表示
        player2_card=tkinter.PhotoImage(file="")
        canvas=tkinter.Canvas(bg="white",width=100,height=200)
        canvas.pack() 
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        canvas.create_image(0,0,image=player2_card)
        
        #自分のカードの画像表示
        player1_card=tkinter.PhotoImage(file="")
        canvas=tkinter.Canvas(bg="white",width=100,height=200)
        canvas.pack()
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        canvas.create_image(0,0,image=player1_card)
        
         #相手の獲得ゲーム数
        player1_game_count_label=tkinter.Label(multi_frame,
            text="勝利数 {}".format(self.player1_game_count()),font=(self.label_font))
        player1_game_count_label.pack(side=LEFT)
        #複合フレームのパック
        multi_frame.pack()
        
        
        #自分プレイヤーのデッキフレーム
        player1_deck_frame=tkinter.Frame(self.master)
        player1_deck_list=[]
        for _ in range(14):
            player1_deck_list.append(tkinter.Button(player1_deck_frame,text="{}".format(_),
                font=(self.label_font),width=2 ,command=lambda:self.callback(_)).pack(side=tkinter.LEFT,padx=4,pady=4))
        #自分プレイヤーのデッキフレームをパック
        player1_deck_frame.pack()

    #テスト用
    def game_count(self):
        GAME_COUNT=11
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
        GAME_COUNT=6
        return GAME_COUNT
    
        
#テスト用
window=tkinter.Tk()
test=GameWindow(window)
test.mainloop()