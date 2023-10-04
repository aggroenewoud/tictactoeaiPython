import board as b
import player as p
import ai as a

class main:

    def __init__(self):
        board = b.board(3, 3)
        players = [p.player(board), p.player(board)]
        self.startGame(board, players)

    def startGame(self, board, players):
        print("Make move by inputting in the following format: x, y")
        while board.checkIfFilled():
            for i in range(len(players)):
                print(players[i].name + "'s turn")
                players[i].makeMove()

main()