class player:

    def __init__(self):
        self.name = input("Enter name: ")

    def makeMove(self):
        move = input("Move: ")
        cords = move.split(",")
        if len(cords) > 2:
            print("Invalid move")
            return
        else:
            return [int(cords[0]), int(cords[1])]
