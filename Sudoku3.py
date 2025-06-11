import copy
from datetime import datetime


class Sudoku:
    def __init__(self, x):
        self.SUDOKU = x
        self.A = [[] for x in range(9)]
        for i in range(len(self.SUDOKU)):
            self.A[i] = list(self.SUDOKU[i])
            for j in range(len(self.A[i])):
                self.A[i][j] = int(self.A[i][j])
        self.S = [[[0] + [1] * 9 for x in range(9)] for y in range(9)]
        for i in range(9):
            for j in range(9):
                self.S[i][j][self.A[i][j]] = 0
                for k in range(9):
                    self.S[i][k][self.A[i][j]] = 0
                    self.S[k][j][self.A[i][j]] = 0
                for k in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                    for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                        self.S[k][ll][self.A[i][j]] = 0
        self.trace = []
        self.traSe = []
        self.q = []
        self.v = 0
        self.endflag = 0
        self.COMP = ""
        self.count = 0
        self.start = datetime.now()

    def nextcell(self):
        for i in range(9):
            for j in range(9):
                if self.A[i][j] == 0:
                    for k in range(1, 10):
                        if self.S[i][j][k] == 1:
                            self.trace.append([])
                            self.q.append([])
                            self.traSe.append([])
                            self.trace[self.v] = list(map(list, self.A))
                            self.q[self.v] = [i, j, k]
                            self.traSe[self.v] = copy.deepcopy(self.S)
                            self.v += 1
                            self.A[i][j] = k
                            self.S[i][j][self.A[i][j]] = 0
                            for kk in range(9):
                                self.S[i][kk][self.A[i][j]] = 0
                                self.S[kk][j][self.A[i][j]] = 0
                            for kk in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                                for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                                    self.S[kk][ll][self.A[i][j]] = 0
                            return
        self.count += 1
        print("No. ", self.count, " Time elapse : ", datetime.now() - self.start)
        for i in range(9):
            print(" ".join([str(x) for x in self.A[i]]))
        print()
        self.bs()

    def bs(self):
        if self.v < 1:
            print("END")
            self.endflag = 1
            return
        self.S = copy.deepcopy(self.traSe[self.v - 1])
        self.A = list(map(list, self.trace[self.v - 1]))

        for k in range(self.q[self.v - 1][2] + 1, 10):
            if self.S[self.q[self.v - 1][0]][self.q[self.v - 1][1]][k] == 1:
                self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]] = k
                self.q[self.v - 1][2] = k
                self.S[self.q[self.v - 1][0]][self.q[self.v - 1][1]][
                    self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                ] = 0
                for kk in range(9):
                    self.S[self.q[self.v - 1][0]][kk][
                        self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                    ] = 0
                    self.S[kk][self.q[self.v - 1][1]][
                        self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                    ] = 0
                for kk in range(
                    int(self.q[self.v - 1][0] / 3) * 3,
                    int(self.q[self.v - 1][0] / 3) * 3 + 3,
                ):
                    for ll in range(
                        int(self.q[self.v - 1][1] / 3) * 3,
                        int(self.q[self.v - 1][1] / 3) * 3 + 3,
                    ):
                        self.S[kk][ll][
                            self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                        ] = 0
                return
        self.v -= 1
        if self.v < 1:
            print("END")
            self.endflag = 1
            return
        self.S = copy.deepcopy(self.traSe[self.v - 1])
        self.A = list(map(list, self.trace[self.v - 1]))
        while True:
            for k in range(self.q[self.v - 1][2] + 1, 10):
                if self.S[self.q[self.v - 1][0]][self.q[self.v - 1][1]][k] == 1:
                    self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]] = k
                    self.q[self.v - 1][2] = k
                    self.S[self.q[self.v - 1][0]][self.q[self.v - 1][1]][
                        self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                    ] = 0
                    for kk in range(9):
                        self.S[self.q[self.v - 1][0]][kk][
                            self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                        ] = 0
                        self.S[kk][self.q[self.v - 1][1]][
                            self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                        ] = 0
                    for kk in range(
                        int(self.q[self.v - 1][0] / 3) * 3,
                        int(self.q[self.v - 1][0] / 3) * 3 + 3,
                    ):
                        for ll in range(
                            int(self.q[self.v - 1][1] / 3) * 3,
                            int(self.q[self.v - 1][1] / 3) * 3 + 3,
                        ):
                            self.S[kk][ll][
                                self.A[self.q[self.v - 1][0]][self.q[self.v - 1][1]]
                            ] = 0
                    return
            self.v -= 1
            if self.v < 1:
                print("END")
                self.endflag = 1
                return
            self.S = copy.deepcopy(self.traSe[self.v - 1])
            self.A = list(map(list, self.trace[self.v - 1]))

    def solve(self):
        def m3(x):
            return int(x / 3) * 3

        def testvalid(A, S):
            for i in range(9):
                for j in range(9):
                    if (A[i][j] == 0) and (sum(S[i][j]) == 0):
                        return False
            return True

        while self.endflag == 0:
            while self.COMP != str(self.A):
                self.COMP = str(self.A)
                for i in range(9):  # single value in 1 - cell
                    for j in range(9):
                        if sum(self.S[i][j]) == 1:
                            for k in range(1, 10):
                                if self.A[i][j] == 0 and self.S[i][j][k] == 1:
                                    self.A[i][j] = k
                                    self.S[i][j][self.A[i][j]] = 0
                                    for kk in range(9):
                                        self.S[i][kk][self.A[i][j]] = 0
                                        self.S[kk][j][self.A[i][j]] = 0
                                    for kk in range(m3(i), m3(i) + 3):
                                        for ll in range(m3(j), m3(j) + 3):
                                            self.S[kk][ll][self.A[i][j]] = 0
                for k in range(1, 10):
                    for i in range(9):  # single value in row
                        s = 0
                        for j in range(9):
                            if (self.A[i][j] == 0) and (self.S[i][j][k] == 1):
                                s += 1
                                t = j
                        if s == 1:
                            self.A[i][t] = k
                            self.S[i][t][self.A[i][t]] = 0
                            for kk in range(9):
                                self.S[i][kk][self.A[i][t]] = 0
                                self.S[kk][t][self.A[i][t]] = 0
                            for kk in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                                for ll in range(int(t / 3) * 3, int(t / 3) * 3 + 3):
                                    self.S[kk][ll][self.A[i][t]] = 0
                    for j in range(9):  # single value in column
                        s = 0
                        for i in range(9):
                            if (self.A[i][j] == 0) and (self.S[i][j][k] == 1):
                                s += 1
                                t = i
                        if s == 1:
                            self.A[t][j] = k
                            self.S[t][j][self.A[t][j]] = 0
                            for kk in range(9):
                                self.S[t][kk][self.A[t][j]] = 0
                                self.S[kk][j][self.A[t][j]] = 0
                            for kk in range(int(t / 3) * 3, int(t / 3) * 3 + 3):
                                for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                                    self.S[kk][ll][self.A[t][j]] = 0
            if testvalid(self.A, self.S):
                self.nextcell()
            else:
                self.bs()
        print("Total time elapse : ", datetime.now() - self.start)


x = (
    "060030780",
    "800009050",
    "005000104",
    "009004810",
    "501080960",
    "006700400",
    "008000070",
    "000000500",
    "100400000",
)
Sudoku(x).solve()
