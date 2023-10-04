class player:

    def __init__(self, board):
        self.board = board
        self.name = input("Enter name: ")

    def makeMove(self):
        print(self.name)
