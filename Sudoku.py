import pygame
import random

table = [[0]*9 for i in ramge(9)]

# 행 검사


def checkRow(I):
    checkList = [0]*10
    for i in range(9):
        if checkList[table[I][i]]:
            return False
        checkList[table[I][i]] += 1
    return True

# 열 검사


def checkCol(J):
    checkList = [0]*10
    for i in range(9):
        if checkList[table[i][J]]:
            return False
        checkList[table[i][J]] += 1
    return True

# 3X3 격자 검사


def checkSquare(I, J):
    checkList = [0]*10
    for i in range(I*3, I*3+3):
        for j in range(J*3, J*3+3):
            if checkList[table[i][j]]:
                return False
            checkList[table[i][j]] += 1
    return True

# 검사 함수


def accept():
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


def initTable():
