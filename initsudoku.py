# 스도쿠 판을 랜덤으로 생성하는 코드


import random


table = [[0]*9 for i in range(9)]
board = [[0]*9 for i in range(9)]
row = [[0]*10 for i in range(10)]
col = [[0]*10 for i in range(10)]
diag = [[0]*10 for i in range(10)]

flag = False

def initTable():
    seq_point = [0, 4, 8]
    for offset in range(0, 9, 3):
        seq = [i for i in range(1, 10)]
        random.shuffle(seq)
        for idx in range(9):
            now_i, now_j = idx//3, idx%3
            row[now_i+offset][seq[idx]] = 1
            col[now_j+offset][seq[idx]]=1
            k = seq_point[offset//3]
            diag[k][seq[idx]] = 1
            board[offset+now_i][offset+now_j] = seq[idx]

def makeTable(k):
    global flag
    if flag:
        return True
    if k>80:
        for i in range(9):                  
            for j in range(9):
                table[i][j] = board[i][j]
        flag = True
        return True
    now_i, now_j = k//9, k%9
    start_number = random.randint(1, 9)
    if board[now_i][now_j]:
        makeTable(k+1)
    for m in range(1, 10):
        m = 1+(m+start_number)%9
        d = (now_i//3)*3+now_j//3
        if row[now_i][m]==0 and col[now_j][m]==0 and diag[d][m]==0:
            row[now_i][m], col[now_j][m], diag[d][m] = 1, 1, 1
            board[now_i][now_j] = m
            makeTable(k+1)
            row[now_i][m], col[now_j][m], diag[d][m] = 0, 0, 0
            board[now_i][now_j] = 0

initTable()
makeTable(0)

for i in range(9):
    print(table[i])




            
        
