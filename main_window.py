import tkinter
from tkinter.font import Font

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
        """
        #現在のゲーム数
        game_count_label=tkinter.Label(self,
            text="{}ゲーム目".format(self.game_count()),font=(self.label_font))
        game_count_label.grid(row=0,column=0,sticky=tkinter.NW)
        """
        #相手プレイヤーのデッキ
        player2_deck_list=[]
        for _ in range(14):
            player2_deck_list.append(tkinter.Button(self,text="{}".format(_),
                font=(self.label_font),width=2 ,command=lambda:self.callback(_)))
            player2_deck_list[_].grid(row=2,column=_,padx=1,pady=10)

        """ここから1行に含める
        #相手の獲得ゲーム数
        player2_game_count_label=tkinter.Label(self,
            text="勝利数 {}".format(self.player2_game_count()),font=(self.label_font))
        player2_game_count_label.grid(row=4,column=1,sticky=tkinter.NW)
        
        #相手のカードの画像表示
        ##player2_card=tkinter.PhotoImage(file="img\sample1.png")
        canvas=tkinter.Canvas(bg="white",width=200,height=200)
        canvas.pack() 
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        canvas.create_image(0,0,image=player2_card)
        #自分のカードの画像表示
        ##player1_card=tkinter.PhotoImage(file="img\sample{}.png".format(1))
        #canvas=tkinter.Canvas(bg="white",width=100,height=200)
        #canvas.pack()
        #pack()でないとcanvasは配置できない?1行に収められるように工夫が必要
        ##canvas.create_image(0,0,image=player1_card)
        #自分の獲得ゲーム数
        player1_game_count_label=tkinter.Label(self,
            text="勝利数 {}".format(self.player2_game_count()),font=(self.label_font))
        player1_game_count_label.grid(row=6,column=4,sticky=tkinter.SE)

        canvas.create_line(100,0,100,200,fill="black",width=1)

        ここまで1行に含める"""
        
        #自分のデッキ
        player1_deck_list=[]
        for _ in range(14):
            player1_deck_list.append(tkinter.Button(self,text="{}".format(_),
                font=(self.label_font),width=2 ,command=lambda:self.callback(_)))
            player1_deck_list[_].grid(row=3,column=_,padx=1,pady=10)

    #テスト用
    def game_count(self):
        GAME_COUNT=10
        return GAME_COUNT
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
    
        
#テスト用
window=tkinter.Tk()
test=GameWindow(window)
test.mainloop()