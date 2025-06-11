import copy
from tkinter import Button, E, Frame, Label, S, Tk, W


def init():
    global A, S
    SUDOKU = (
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

    A = [[] for x in range(9)]
    for i in range(len(SUDOKU)):
        A[i] = list(SUDOKU[i])
        for j in range(len(A[i])):
            A[i][j] = int(A[i][j])
    S = [[[0, 1, 1, 1, 1, 1, 1, 1, 1, 1] for x in range(9)] for y in range(9)]
    for ii in range(9):
        for jj in range(9):
            S[ii][jj][A[ii][jj]] = 0
            for kk in range(9):
                S[ii][kk][A[ii][jj]] = 0
                S[kk][jj][A[ii][jj]] = 0
            for kk in range(int(ii / 3) * 3, int(ii / 3) * 3 + 3):
                for ll in range(int(jj / 3) * 3, int(jj / 3) * 3 + 3):
                    S[kk][ll][A[ii][jj]] = 0
    draw_sudoku()


def draw_sudoku():
    global root
    root.destroy()
    root = Frame(master)
    root.grid()
    for i in range(9):
        for j in range(9):
            Label(root, text="  ", font=("Courier", 30)).grid(
                row=(i + 1) * 2, column=(j + 1) * 2, sticky=E + W
            )
            if A[i][j] != 0:
                Label(root, text=str(A[i][j]), font=("Courier", 15)).grid(
                    row=(i + 1) * 2, column=(j + 1) * 2, sticky=E + W
                )
            else:
                tmp = ""
                for k in range(1, 10):
                    if S[i][j][k] == 1:
                        if len(tmp) == 5:
                            tmp = tmp + "\n"
                        tmp = tmp + str(k)
                Label(root, text=tmp, font=("Courier", 8), bg="#999999").grid(
                    row=(i + 1) * 2, column=(j + 1) * 2, sticky=E + W
                )
    for i in range(2, 19, 2):
        Label(root, text="-----").grid(row=7, column=i, sticky=E + W)
        Label(root, text="-----").grid(row=13, column=i, sticky=E + W)
        Label(root, text="|").grid(row=i, column=7, sticky=E + W)
        Label(root, text="|").grid(row=i, column=13, sticky=E + W)
    Button(root, text="RESET", command=init).grid(row=0, column=0, sticky=E + W)
    Button(root, text="BASIC", command=runbasic).grid(row=6, column=0, sticky=E + W)
    Button(root, text="BS", command=bs).grid(row=4, column=0, sticky=E + W)


def testvalid():
    f = 1
    for i in range(9):
        for j in range(9):
            if (A[i][j] == 0) and (sum(S[i][j]) == 0):
                f = 0
    if f == 1:
        return True
    else:
        return False


def bs():
    global A
    global S
    global v
    global q
    if testvalid():
        nextcell()
    else:
        A = copy.deepcopy(trace[v - 1])
        S = copy.deepcopy(traSe[v - 1])
        t = q[v - 1]
        for k in range(t[2] + 1, 10):
            if S[t[0]][t[1]][k] == 1:
                A[t[0]][t[1]] = k
                t[2] = k
                S[t[0]][t[1]][A[t[0]][t[1]]] = 0
                for kk in range(9):
                    S[t[0]][kk][A[t[0]][t[1]]] = 0
                    S[kk][t[1]][A[t[0]][t[1]]] = 0
                for kk in range(int(t[0] / 3) * 3, int(t[0] / 3) * 3 + 3):
                    for ll in range(int(t[1] / 3) * 3, int(t[1] / 3) * 3 + 3):
                        S[kk][ll][A[t[0]][t[1]]] = 0
                draw_sudoku()
                return
        v = v - 1
        A = copy.deepcopy(trace[v - 1])
        S = copy.deepcopy(traSe[v - 1])
        t = q[v - 1]
        while True:
            for k in range(t[2] + 1, 10):
                if S[t[0]][t[1]][k] == 1:
                    A[t[0]][t[1]] = k
                    t[2] = k
                    S[t[0]][t[1]][A[t[0]][t[1]]] = 0
                    for kk in range(9):
                        S[t[0]][kk][A[t[0]][t[1]]] = 0
                        S[kk][t[1]][A[t[0]][t[1]]] = 0
                    for kk in range(int(t[0] / 3) * 3, int(t[0] / 3) * 3 + 3):
                        for ll in range(int(t[1] / 3) * 3, int(t[1] / 3) * 3 + 3):
                            S[kk][ll][A[t[0]][t[1]]] = 0
                    draw_sudoku()
                    return
            v = v - 1
            A = copy.deepcopy(trace[v - 1])
            S = copy.deepcopy(traSe[v - 1])


def nextcell():
    global v
    global endflag
    for i in range(9):
        for j in range(9):
            if A[i][j] == 0:
                for k in range(1, 10):
                    if S[i][j][k] == 1:
                        trace.append([])
                        q.append([])
                        traSe.append([])
                        trace[v] = copy.deepcopy(A)
                        q[v] = [i, j, k]
                        traSe[v] = copy.deepcopy(S)
                        v += 1
                        A[i][j] = k
                        S[i][j][A[i][j]] = 0
                        for kk in range(9):
                            S[i][kk][A[i][j]] = 0
                            S[kk][j][A[i][j]] = 0
                        for kk in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                            for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                                S[kk][ll][A[i][j]] = 0
                        draw_sudoku()
                        return
    endflag = 1


def runbasic():
    COMP = ""
    while COMP != str(A):
        COMP = str(A)
        basic()


def basic():

    for i in range(9):  # single value in 1-cell
        for j in range(9):
            if sum(S[i][j]) == 1:
                for k in range(1, 10):
                    if (A[i][j] == 0) and (S[i][j][k] == 1):
                        A[i][j] = k
                        S[i][j][A[i][j]] = 0
                        for kk in range(9):
                            S[i][kk][A[i][j]] = 0
                            S[kk][j][A[i][j]] = 0
                        for kk in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                            for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                                S[kk][ll][A[i][j]] = 0
    for k in range(1, 10):
        for i in range(9):  # single value in row
            s = 0
            for j in range(9):
                if (A[i][j] == 0) and (S[i][j][k] == 1):
                    s += 1
                    t = j
            if s == 1:
                A[i][t] = k
                S[i][t][A[i][t]] = 0
                for kk in range(9):
                    S[i][kk][A[i][t]] = 0
                    S[kk][t][A[i][t]] = 0
                for kk in range(int(i / 3) * 3, int(i / 3) * 3 + 3):
                    for ll in range(int(t / 3) * 3, int(t / 3) * 3 + 3):
                        S[kk][ll][A[i][t]] = 0
        for j in range(9):  # single value in column
            s = 0
            for i in range(9):
                if (A[i][j] == 0) and (S[i][j][k] == 1):
                    s += 1
                    t = i
            if s == 1:
                A[t][j] = k
                S[t][j][A[t][j]] = 0
                for kk in range(9):
                    S[t][kk][A[t][j]] = 0
                    S[kk][j][A[t][j]] = 0
                for kk in range(int(t / 3) * 3, int(t / 3) * 3 + 3):
                    for ll in range(int(j / 3) * 3, int(j / 3) * 3 + 3):
                        S[kk][ll][A[t][j]] = 0
        for m in range(9):  # single value in 9-cell
            s = 0
            for i in range(int(m / 3) * 3, int(m / 3) * 3 + 3):
                for j in range((m - int(m / 3) * 3) * 3, (m - int(m / 3) * 3) * 3 + 3):
                    if (A[i][j] == 0) and (S[i][j][k] == 1):
                        s += 1
                        ti = i
                        tj = j
            if s == 1:
                A[ti][tj] = k
                S[ti][tj][A[ti][tj]] = 0
                for kk in range(9):
                    S[ti][kk][A[ti][tj]] = 0
                    S[kk][tj][A[ti][tj]] = 0
                for kk in range(int(ti / 3) * 3, int(ti / 3) * 3 + 3):
                    for ll in range(int(tj / 3) * 3, int(tj / 3) * 3 + 3):
                        S[kk][ll][A[ti][tj]] = 0

    draw_sudoku()


master = Tk()
root = Frame(master)
root.grid()
init()
trace = []
traSe = []
q = []
v = 0
endflag = 0

master.title("SUDOKU (C) By AlanZhou 2017")
master.mainloop()
