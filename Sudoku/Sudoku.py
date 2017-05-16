import copy
from datetime import datetime

def init():
    global A,S
    #SUDOKU=('300460000','050000000','000090085','100000000','000000748','000003150','000078900','060310007','709600000')
    #SUDOKU=('006380000','080009000','300200000','090008500','002003001','630040009','000621000','000090080','910004000')
    #SUDOKU=('050000030','000610000','006007000','031000000','000890002','072300850','007185000','060070500','000006020')
    #SUDOKU=('000040008','000900600','002000030','004001000','030080020','000030074','927000060','068320040','000600009')
    SUDOKU=('800000000','003600000','070090200','050007000','000045700','000100030','001000068','008500010','090000400')
    SUDOKU=('800000000','003600000','070090200','050007000','000045700','000100030','001000068','008500010','090000400')
    A=[[]for x in range(9)]
    for i in range(len(SUDOKU)):
        A[i]=list(SUDOKU[i])
        for j in range(len(A[i])):
            A[i][j]=int(A[i][j])
    S=[[[0,1,1,1,1,1,1,1,1,1]for x in range(9)]for y in range(9)]
    for ii in range(9):
        for jj in range(9):
            S[ii][jj][A[ii][jj]]=0
            for kk in range(9):
                S[ii][kk][A[ii][jj]]=0
                S[kk][jj][A[ii][jj]]=0
            for kk in range(int(ii/3)*3,int(ii/3)*3+3):
                for ll in range(int(jj/3)*3,int(jj/3)*3+3):
                    S[kk][ll][A[ii][jj]]=0

def testvalid():
    f=1
    for i in range(9):
        for j in range(9):
            if (A[i][j]==0)and(sum(S[i][j])==0):
                f=0
    if f==1:
        return True
    else:
        return False

def bs():
    global A
    global S
    global pointer
    global ijk
    if testvalid():
        nextcell()
    else:

        S=copy.deepcopy(traSe[pointer-1])
        A=list(map(list,trace[pointer-1]))

        for k in range(ijk[pointer-1][2]+1,10):
            if S[ijk[pointer-1][0]][ijk[pointer-1][1]][k]==1:
                A[ijk[pointer-1][0]][ijk[pointer-1][1]]=k
                ijk[pointer-1][2]=k
                S[ijk[pointer-1][0]][ijk[pointer-1][1]][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                for kk in range(9):
                    S[ijk[pointer-1][0]][kk][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                    S[kk][ijk[pointer-1][1]][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                for kk in range(int(ijk[pointer-1][0]/3)*3,int(ijk[pointer-1][0]/3)*3+3):
                    for ll in range(int(ijk[pointer-1][1]/3)*3,int(ijk[pointer-1][1]/3)*3+3):
                        S[kk][ll][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                return
        pointer = pointer-1

        S=copy.deepcopy(traSe[pointer-1])
        A=list(map(list,trace[pointer-1]))


        while True:
            for k in range(ijk[pointer-1][2]+1,10):
                if S[ijk[pointer-1][0]][ijk[pointer-1][1]][k]==1:
                    A[ijk[pointer-1][0]][ijk[pointer-1][1]]=k
                    ijk[pointer-1][2]=k
                    S[ijk[pointer-1][0]][ijk[pointer-1][1]][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                    for kk in range(9):
                        S[ijk[pointer-1][0]][kk][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                        S[kk][ijk[pointer-1][1]][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                    for kk in range(int(ijk[pointer-1][0]/3)*3,int(ijk[pointer-1][0]/3)*3+3):
                        for ll in range(int(ijk[pointer-1][1]/3)*3,int(ijk[pointer-1][1]/3)*3+3):
                            S[kk][ll][A[ijk[pointer-1][0]][ijk[pointer-1][1]]]=0
                    return
            pointer = pointer-1
            if pointer < 1:
                print('WRONG SUDOKU')
                global endflag
                endflag=1
                return

            S=copy.deepcopy(traSe[pointer-1])
            A=list(map(list,trace[pointer-1]))

def nextcell():
    global pointer
    global endflag
    for i in range(9):
        for j in range(9):
            if A[i][j]==0:
                for k in range(1,10):
                    if S[i][j][k]==1:
                        trace.append([])
                        ijk.append([])
                        traSe.append([])

                        trace[pointer]=list(map(list,A))
                        ijk[pointer]=[i,j,k]
                        traSe[pointer]=copy.deepcopy(S)
                        
                        pointer += 1
                        A[i][j]=k
                        S[i][j][A[i][j]]=0
                        for kk in range(9):
                            S[i][kk][A[i][j]]=0
                            S[kk][j][A[i][j]]=0
                        for kk in range(int(i/3)*3,int(i/3)*3+3):
                            for ll in range(int(j/3)*3,int(j/3)*3+3):
                                S[kk][ll][A[i][j]]=0
                        return
    endflag=1

def basic():
    
    for i in range(9):#single value in 1-cell
        for j in range(9):
            if sum(S[i][j])==1:
                for k in range(1,10):
                    if (A[i][j]==0)and(S[i][j][k]==1):
                        A[i][j]=k
                        S[i][j][A[i][j]]=0
                        for kk in range(9):
                            S[i][kk][A[i][j]]=0
                            S[kk][j][A[i][j]]=0
                        for kk in range(int(i/3)*3,int(i/3)*3+3):
                            for ll in range(int(j/3)*3,int(j/3)*3+3):
                                S[kk][ll][A[i][j]]=0
    
    for k in range(1,10):
        
        for i in range(9):#single value in row
            s=0
            for j in range(9):
                if (A[i][j]==0)and(S[i][j][k]==1):
                    s+=1
                    t=j
            if s==1:
                A[i][t]=k
                S[i][t][A[i][t]]=0
                for kk in range(9):
                    S[i][kk][A[i][t]]=0
                    S[kk][t][A[i][t]]=0
                for kk in range(int(i/3)*3,int(i/3)*3+3):
                    for ll in range(int(t/3)*3,int(t/3)*3+3):
                        S[kk][ll][A[i][t]]=0
        
        for j in range(9):#single value in column
            s=0
            for i in range(9):
                if (A[i][j]==0)and(S[i][j][k]==1):
                    s+=1
                    t=i
            if s==1:
                A[t][j]=k
                S[t][j][A[t][j]]=0
                for kk in range(9):
                    S[t][kk][A[t][j]]=0
                    S[kk][j][A[t][j]]=0
                for kk in range(int(t/3)*3,int(t/3)*3+3):
                    for ll in range(int(j/3)*3,int(j/3)*3+3):
                        S[kk][ll][A[t][j]]=0

init()
trace=[]
traSe=[]
ijk=[]
pointer = 0
endflag=0
COMP=''
start=datetime.now()
while endflag==0:
    while COMP != str(A):
        COMP=str(A)
        basic()
    bs()
print(datetime.now()-start)
for i in range(9):
    print(A[i])
print()
