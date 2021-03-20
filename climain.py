from war import *

def isvalidnumber(val,player):
    # 数字であるか
    if val.isdigit():
        # 手札に数字が含まれているか
        if int(val) in player.deck.inHandCards:
            return int(val)
        else:
            print("your input doesn't match any card in your deck!!")
            exit()
    else:
        print("your input isn't number!!")
        exit()
    

print("Game Start!!\n\n")
while True:
    # 先攻(player)
    namePlayer1 = input("input player1 name: ")
    # 後攻(CPU)
    namePlayer2 = input("input player2 name: ")
    player1 = Player(namePlayer1)
    player2 = Player(namePlayer2)

    for i in range(13):

        # 現在の手札表示(player1)
        print(",".join(map(str,player1.deck.inHandCards)))
        rawCardPlayer1 = input(player1.name + ": choose card: ")
        # 入力値が有効かどうか判定
        cardPlayer1 = isvalidnumber(rawCardPlayer1,player1)
        print("\n")

        # 現在の手札表示(player2)
        print(",".join(map(str,player2.deck.inHandCards)))
        rawCardPlayer2 = input(player2.name + ": choose card: ")
        # 入力値が有効かどうか判定
        cardPlayer2 = isvalidnumber(rawCardPlayer2,player2)
        print("\n")

        # デッキからカードを取り出す
        player1.deck.removeCard(cardPlayer1)
        player2.deck.removeCard(cardPlayer2)

        # カード比較&勝敗
        if cardPlayer1 == cardPlayer2:
            print("draw\n")
        elif cardPlayer1 > cardPlayer2:
            print("player1 win!\n")
            player1.numWins += 1
        else:
            print("player2 win!\n")
            player2.numWins += 1

        print("next turn\n")

    # 最終結果
    print("the result...")
    if player1.numWins == player2.numWins:
        print("draw!")
    elif player1.numWins > player2.numWins:
        print("player1 win!\n")
    else:
        print("player2 win!\n")

    # 再戦するかどうか
    print("Do you want to continue? input a number")
    cont = input("1:Yes 2:No\n")
    if cont == 2:
        break
