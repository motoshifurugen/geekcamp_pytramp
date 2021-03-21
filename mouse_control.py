import tkinter

root = tkinter.Tk()
#画面のサイズは変更可能にするか決める
cvs = tkinter.Canvas(root,width=1000,height=700)
#画面を固定
root.resizable(False,False)

#マウスポインタのx座標
mouse_x = 0
#マウスポインタのy座標
mouse_y = 0
#マウスをクリックした時の変数
mouse_c = 0

#マウスを動かした時に実行する関数
def mouse_move(e):
  # mouse_xとmouse_yを変数として扱うと宣言
  global mouse_x, mouse_y
  #それぞれの変数にマウスポインタの座標を代入
  mouse_x = e.x
  mouse_y = e.y

#マウスボタンをクリックした時に実行する関数
def mouse_press(e):
  global mouse_c
  mouse_c = 1

#マウスボタンを離した時に実行する関数
def mouse_release(e):
  global mouse_c
  mouse_c = 0


#リアルタイム処理を行う関数
def game_main():
  #フォント指定
  fnt = ("Times New Roman", 30)
  #マウスの変数表示（カード選択範囲が決定した消すかも）
  txt ="mouse({},{}){}".format(mouse_x,mouse_y,mouse_c)
  #文字削除
  cvs.delete("TEST")
  #表示
  cvs.create_text(456,384,text=txt,fill="black",font=fnt, tag="TEST")
  #0.1秒ごとに関数を実行（なめらかさは重要じゃないから200とかでもＯＫ）
  root.after(100,game_main)

root.title("マウス入力")
#マウスが動いた時に実行する関数を指定
root.bind("<Motion>",mouse_move)
#クリックした時に実行する関数を指定
root.bind("<ButtonPress>",mouse_press)
#離した時に実行する関数を指定
root.bind("<ButtonRelease>",mouse_release)

root = tkinter.Tk()
#タイトル表示
root.title("画像表示したい")
#サイズ固定
root.resizable(False,False)
canvas = tkinter.Canvas(root,width=1000,height=700)
canvas.pack()
gazou0 = tkinter.PhotoImage(file="Splitted-Image-0-0.png")
canvas.create_image(100,500,image=gazou0)
gazou1 = tkinter.PhotoImage(file="Splitted-Image-1-0.png")
canvas.create_image(150,500,image=gazou1)
gazou2 = tkinter.PhotoImage(file="Splitted-Image-2-0.png")
canvas.create_image(200,500,image=gazou2)
gazou3 = tkinter.PhotoImage(file="Splitted-Image-3-0.png")
canvas.create_image(250,500,image=gazou3)
gazou4 = tkinter.PhotoImage(file="Splitted-Image-4-0.png")
canvas.create_image(300,500,image=gazou4)
gazou5 = tkinter.PhotoImage(file="Splitted-Image-5-0.png")
canvas.create_image(350,500,image=gazou5)
gazou6 = tkinter.PhotoImage(file="Splitted-Image-6-0.png")
canvas.create_image(400,500,image=gazou6)
gazou7 = tkinter.PhotoImage(file="Splitted-Image-7-0.png")
canvas.create_image(450,500,image=gazou7)
gazou8 = tkinter.PhotoImage(file="Splitted-Image-8-0.png")
canvas.create_image(500,500,image=gazou8)
gazou9 = tkinter.PhotoImage(file="Splitted-Image-9-0.png")
canvas.create_image(550,500,image=gazou9)
gazou10 = tkinter.PhotoImage(file="Splitted-Image-10-0.png")
canvas.create_image(600,500,image=gazou10)
gazou11 = tkinter.PhotoImage(file="Splitted-Image-11-0.png")
canvas.create_image(650,500,image=gazou11)
gazou12 = tkinter.PhotoImage(file="Splitted-Image-12-0.png")
canvas.create_image(700,500,image=gazou12)

root.title("画像表示したい")
root.geometry("1000x800")

cvs.pack()
game_main()
root.mainloop()