class board:

    def __init__(self, x, y):
        self.grid = self.createBoard(x, y)

    def setMove(self, x, y, player):
        self.grid[y][x] = player

    def checkIfFilled(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == " ":
                    return True
        return False

    def createBoard(self, x, y):
        rows = []
        for i in range(y):
            columns = []
            for e in range(x):
                columns.append(" ")
            rows.append(columns)
        return rows

    def checkLine(self, line):
        if line == "xxx":
            return [True, "x"]
        elif line == "ooo":
            return [True, "o"]
        return [False, " "]

    def checkHorizontal(self):
        for y in range(len(self.grid)):
            line = "".join(self.grid[y])
            return self.checkLine(line)

    def checkVertical(self):
        for x in range(len(self.grid[0])):
            line = ""
            for y in range(len(self.grid)):
                line += line + self.grid[y][x]
            return self.checkLine(line)

    def checkForWin(self):
        if self.checkHorizontal()[0]:
            print(self.checkHorizontal()[1] + " wins!")
            return
        elif self.checkVertical()[0]:
            print(self.checkVertical()[1] + " wins!")