import tkinter

root = tkinter.Tk()
#画面のサイズは変更可能にするか決める
cvs = tkinter.Canvas(root,width=912,height=765)

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


cvs.pack()
game_main()
root.mainloop()