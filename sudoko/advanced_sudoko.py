from sudoko import Sudoko

class Advanced_Sudoko(Sudoko):
    def __init__(self, board):
        super().__init__(board)
        self.hail_mary = self.exCheckBoard

    def exGenericCheck(self, input_dict):
        for r in input_dict:
            temp = []
            pt = []
            for j in input_dict[r]:
                pt.append(j)
                temp.append(self.at_point(j))
            for k in range(len(temp)):
                for l in range(len(temp[k])):
                    match = True
                    for m in range(len(temp)):
                        if m == k: continue
                        match = match and temp[k][l] not in temp[m]
                    if match: return (pt[k], temp[k][l])
        return (-1, -1)

    def exCheckRows(self):
        row_dict = {}
        for i in self.empty:
            row_dict[i[0]] = row_dict.get(i[0], []) + [i]
        return self.exGenericCheck(row_dict)

    def exCheckCols(self):
        col_dict = {}
        for i in self.empty:
            col_dict[i[1]] = col_dict.get(i[1], []) + [i]
        return self.exGenericCheck(col_dict)

    def exCheckBlocks(self):
        block_dict = {}
        for i in self.empty:
            block_dict[3*(i[0]//3)+(i[1]//3)] = block_dict.get(3*(i[0]//3)+i[1], []) + [i]
        return self.exGenericCheck(block_dict)

    def exCheckBoard(self):
        r = self.exCheckRows()
        c = self.exCheckCols()
        b = self.exCheckBlocks()
        move_found = False
        if r[0] != -1:
            self.moves.append(r)
            move_found = True
        elif c[0] != -1:
            self.moves.append(c)
            move_found = True
        elif b[0] != -1:
            self.moves.append(b)
            move_found = True
        return move_found


"""

y = [[0,7,5,6,0,0,0,0,0], \
    [0,8,9,0,0,7,3,0,0], \
    [0,0,3,4,0,0,0,0,0], \
    [0,0,0,0,0,6,0,7,0], \
    [5,0,1,0,7,0,8,0,3], \
    [0,2,0,8,0,0,0,0,0], \
    [0,0,0,0,0,4,1,0,0], \
    [0,0,4,9,0,0,5,2,0], \
    [0,0,0,0,0,8,7,9,0]]

z = [[0, 0, 0, 6, 0, 0, 0, 2, 5], \
    [0, 0, 0, 0, 2, 4, 0, 8, 0], \
    [0, 0, 0, 3, 1, 0, 6, 9, 0], \
    [6, 8, 0, 0, 0, 2, 0, 0, 0], \
    [0,0,0,0,5,0,0,0,0], \
    [0,0,0,4,0,0,0,6,1], \
    [0,2,6,0,9,3,0,0,0], \
    [0,7,0,2,6,0,0,0,0], \
    [3,5,0,0,0,8,0,0,0]]

a = [[6,2,0,8,0,0,0,0,0], \
    [0,0,0,0,0,3,0,0,0], \
    [4,0,1,0,0,0,0,0,9], \
    [0,0,0,0,9,7,1,0,0], \
    [0,1,0,6,0,5,0,4,0], \
    [0,0,5,1,2,0,0,0,0], \
    [9,0,0,0,0,0,7,0,8], \
    [0,0,0,3,0,0,0,0,0], \
    [0,0,0,0,0,1,0,6,2]]
X1 = Advanced_Sudoko(a)
print(X1)
X1.play_game()
print(X1)
print("END\n")












def get_double(self):
    doubles = {}
    back_up = [0]
    for i in self.empty:
        if len(self.at_point(i)) == 2:
            doubles[i] = self.at_point(i)
    for i in doubles:
        for j in doubles:
            if i == j: continue
            if doubles[i] == doubles[j]:
                back_up = (i, j, doubles[i])
                if i[0] == j[0] or i[1] == j[1]:
                    return (i, j, doubles[i])
    if len(back_up) == 3: return back_up
    return (-1, -1, -1)

def new_board(self, p1, p2, v1, v2):
    end = []
    for i in range(9):
        row = []
        for j in range(9):
            if p1[0] == i and p1[1] == j: row.append(v1)
            elif p2[0] == i and p2[1] == j: row.append(v2)
            else: row.append(self.board[i][j])
        end.append(row)
    return end

def guess(self):
    p1, p2, vals = self.get_double()
    if p1 == -1: return self
    board1 = self.new_board(p1, p2, vals[0], vals[1])
    A = Sudoko(board1)
    if A.play_game(): return A
    board2 = self.new_board(p1, p2, vals[1], vals[0])
    B = Sudoko(board2)
    if B.play_game(): return B
    return self
"""
