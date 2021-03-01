import pygame
import random


def checkRow(I):        # 행 검사
    checkList = [0]*10
    for i in range(9):
        if table[I][i] == 0:
            continue
        if checkList[table[I][i]]:
            return False
        checkList[table[I][i]] += 1
    return True


def checkCol(J):        # 열 검사
    checkList = [0]*10
    for i in range(9):
        if table[i][J] == 0:
            continue
        if checkList[table[i][J]]:
            return False
        checkList[table[i][J]] += 1
    return True


def checkSquare(I, J):      # 3X3 격자 검사
    checkList = [0]*10
    for i in range(I*3, I*3+3):
        for j in range(J*3, J*3+3):
            if table[i][j] == 0:
                continue
            if checkList[table[i][j]]:
                return False
            checkList[table[i][j]] += 1
    return True


def accept():           # 테이블 검사
    for i in range(9):
        if checkRow(i) == False:
            return False
    for i in range(9):
        if checkCol(i) == False:
            return False
    for i in range(3):
        for j in range(3):
            if checkSquare(i*3, j*3) == False:
                return False
    return True


def initTable():
    table = [[0]*9 for i in ramge(9)]
    for i in range(random.randrange(10, 31)):
        randomPoint = random.randrange(81)
        now_i = randomPoint//9
        now_j = randomPoint % 9
        if table[now_i][now_j] != 0:
            i -= 1
        else:
            randomNumber = random.randrange(1, 10)
            table[now_i][now_j] = randomNumber
            if accrpt() == False:
                i -= 1
                table[now_i][now_j] = 0
