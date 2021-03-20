import tkinter
from tkinter.font import Font

class GameWindow(tkinter.Frame):
    def __init__(self,main = None):
        super().__init__(main)
        main.title("PyTrump")
        main.geometry("900x700")
        main.resizable(False,False)
        self.default_font=tkinter.font.Font(family="System",size=48)
        self.button_font=tkinter.font.Font(family="System",size=36)
        self.game_count_label=tkinter.Label(main,
            text="{}ゲーム目".format(game_count),font=(self.default_font))
        self.game_count_label.grid(row=0,column=0)

    

#テスト用
window=tkinter.Tk()
test=GameWindow(main=window)
test.mainloop()