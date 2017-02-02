class Sudoko(object):
    def __init__(self, board):
        self.board = board
        self.test_board = board
        self.empty = []
        self.blank_spaces()
        self.checking = []
        self.value = 0
        self.moves = []
        self.hail_mary = lambda: False

    def getValue(self):
        self.value = 0
        for i in range(9):
            for j in range(9):
                v = self.board[i][j]
                self.value += (j*v*10**i)
        return self.value

    def checkNumbers(self, given):
        array = given[::]
        array.sort()
        end = True
        for i in range(len(array)-1):
            if type(array[i]) != int: return False
            end = end and not (array[i] == array[i+1])
        return end and array[0] == 1 and array[-1] == 9

    def checkRow(self, num):
        if len(self.available_moves(self.board[num])) != 0:
            self.checking = self.available_moves(self.board[num])
            return False
        return self.checkNumbers(self.board[num])

    def checkCol(self, num):
        check = []
        for i in range(9):
            check.append(self.board[i][num])
        if len(self.available_moves(check)) != 0:
            self.checking = self.available_moves(check)
            return False
        return self.checkNumbers(check)

    def checkBlock(self, num):
        row = (num//3)*3
        col = (num - (row))*3
        check = []
        for i in range(3):
            for j in range(3):
                check.append(self.board[row+i][col+j])
        if len(self.available_moves(check)) != 0:
            self.checking = self.available_moves(check)
            return False
        return self.checkNumbers(check)

    def checkBoard(self):
        end = True
        for i in range(9):
            r = self.checkRow(i)
            c = self.checkCol(i)
            b = self.checkBlock(i)
            end = end and r and c and b
        return end

    def blank_spaces(self):
        self.empty = []
        for i in range(9):
            for j in range(9):
                if type(self.board[i][j]) != int:
                    self.empty.append((i,j))
                    self.board[i][j] = 0
                elif self.board[i][j] < 1 or self.board[i][j] > 9:
                    self.empty.append((i,j))
                    self.board[i][j] = 0

    def available_moves(self, check):
        end = []
        for i in range(9):
            if i+1 not in check:
                end.append(i+1)
        return end

    def __repr__(self):
        end = ""
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        v = str(self.board[j+3*i][l+3*k])
                        if v == "0": v = " "
                        end += v + " "
                    end += "| "
                end = end[:-2] + "\n"
            end += "-"*22 + "\n"
        end = end[:-23]
        return end

    def at_point(self, loc):
        possibilities = []
        self.checking = []
        self.checkRow(loc[0])
        possibilities = self.checking
        self.checking = []
        self.checkCol(loc[1])
        possibilities = [p for p in possibilities if p in self.checking]
        self.checking = []
        self.checkBlock((loc[1]//3)+3*(loc[0]//3))
        possibilities = [p for p in possibilities if p in self.checking]
        end = []
        for p in possibilities:
            if p in end: continue
            end.append(p)
        return end

    def play_round(self):
        for p in self.empty:
            result = self.at_point(p)
            if len(result) == 1:
                self.board[p[0]][p[1]] = result[0]
        for i in self.moves:
            self.board[i[0][0]][i[0][1]] = i[1]
        self.moves = []
        self.blank_spaces()

    def play_game(self):
        count = 0
        while not self.checkBoard():
            p = self.getValue()
            count += 1
            self.play_round()
            if p == self.getValue():
                if not self.hail_mary(): break
        print()
        return self.checkBoard()

"""
x = [[5,3,4,6,7,8,9,1,2], \
    [6,7,2,1,9,5,3,4,8], \
    [1,9,8,3,4,2,5,6,7], \
    [8,5,9,7,6,1,4,2,3], \
    [4,2,6,8,5,3,7,9,1], \
    [7,1,3,9,2,4,8,5,6], \
    [9,6,1,5,3,7,2,8,4], \
    [2,8,7,4,1,9,6,3,5], \
    [3,4,5,2,8,6,1,7,9]]

x1 = [[5,0,0,6,0,8,0,0,0], \
    [0,0,0,1,0,5,3,4,0], \
    [1,9,0,3,0,2,0,6,7], \
    [0,5,0,0,0,0,0,2,3], \
    [4,0,0,8,0,0,0,9,1], \
    [0,1,3,9,0,4,8,0,0], \
    [0,0,1,0,3,0,0,8,4], \
    [2,8,7,4,0,0,6,0,5], \
    [0,0,0,2,8,0,1,7,0]]

y = [[0,7,5,6,0,0,0,0,0], \
    [0,8,9,0,0,7,3,0,0], \
    [0,0,3,4,0,0,0,0,0], \
    [0,0,0,0,0,6,0,7,0], \
    [5,0,1,0,7,0,8,0,3], \
    [0,2,0,8,0,0,0,0,0], \
    [0,0,0,0,0,4,1,0,0], \
    [0,0,4,9,0,0,5,2,0], \
    [0,0,0,0,0,8,7,9,0]]

X = Sudoko(x)
print(X.checkBoard())
print(X.empty)
print(X)
Y = Sudoko(y)
print(Y.checkBoard())
print(Y)
print(X)
X.play_round()
X1 = Sudoko(y)
print(X1)
X1.play_game()
print(X1)
print("END\n")
"""
