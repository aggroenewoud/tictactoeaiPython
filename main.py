import board as b
import player as p
import ai as a

class main:

    def __init__(self):
        board = b.board(3, 3)
        players = [p.player(), p.player()]
        self.startGame(board, players)

    def startGame(self, board, players):
        print("Make move by inputting in the following format: x,y")
        while board.checkIfFilled():
            for i in range(len(players)):
                if i == 1:
                    break
                print(players[i].name + "'s turn")
                move = players[i].makeMove()
                board.setMove(move[0], move[1], "x")
                board.printBoard()
                board.checkForWin()

main()