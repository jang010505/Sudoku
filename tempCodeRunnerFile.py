import pygame
import random

from pygame.locals import *

table = [[0]*9 for i in range(9)]
board = [[0]*9 for i in range(9)]
row = [[0]*10 for i in range(10)]
col = [[0]*10 for i in range(10)]
diag = [[0]*10 for i in range(10)]
flag = False

now_x = 0
now_y = 0

color = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "PINK": (255, 178, 217),
    "PURPLE": (209, 178, 255),
    "SKYBLUE": (178, 235, 244),
    "LIGHTGREEN": (183, 240, 177),
    "YELLOW": (252, 242, 158),
    "ORANGE": (255, 193, 158),
    "RED": (255, 167, 167)}


start_time = pygame.time.get_ticks()
game_time = pygame.time.get_ticks()
end_time = pygame.time.get_ticks()


def checkRow(I):
    checkList = [0]*10
    for i in range(9):
        if table[I][i] == 0:
            continue
        if checkList[table[I][i]]:
            return False
        checkList[table[I][i]] += 1
    return True


def checkCol(J):
    checkList = [0]*10
    for i in range(9):
        if table[i][J] == 0:
            continue
        if checkList[table[i][J]]:
            return False
        checkList[table[i][J]] += 1
    return True


def checkSquare(I, J):
    checkList = [0]*10
    for i in range(I*3, I*3+3):
        for j in range(J*3, J*3+3):
            if table[i][j] == 0:
                continue
            if checkList[table[i][j]]:
                return False
            checkList[table[i][j]] += 1
    return True


def accept():
    for i in range(9):
        if checkRow(i) == False:
            return False
    for i in range(9):
        if checkCol(i) == False:
            return False
    for i in range(3):
        for j in range(3):
            if checkSquare(i, j) == False:
                return False
    return True


def initSeq():
    seq_diag = [0, 4, 8]
    for offset in range(0, 9, 3):
        seq = [i for i in range(1, 10)]
        random.shuffle(seq)
        for idx in range(9):
            now_i = idx//3
            now_j = idx % 3
            row[offset+now_i][seq[idx]] = 1
            col[offset+now_j][seq[idx]] = 1
            k = seq_diag[offset//3]
            diag[k][seq[idx]] = 1
            board[offset+now_i][offset+now_j] = seq[idx]


def makeTable(k):
    global flag
    if flag:
        return True
    if k > 80:
        for i in range(9):
            for j in range(9):
                table[i][j] = board[i][j]
        flag = True
        return True
    now_i = k//9
    now_j = k % 9
    start_num = random.randint(1, 9)
    if board[now_i][now_j]:
        makeTable(k+1)
    for m in range(1, 10):
        m = 1+(m+start_num) % 9
        d = (now_i//3)*3+now_j//3
        if row[now_i][m] == 0 and col[now_j][m] == 0 and diag[d][m] == 0:
            row[now_i][m] = 1
            col[now_j][m] = 1
            diag[d][m] = 1
            board[now_i][now_j] = m
            makeTable(k+1)
            row[now_i][m] = 0
            col[now_j][m] = 0
            diag[d][m] = 0
            board[now_i][now_j] = 0


def initTable(level):
    global flag
    initSeq()
    makeTable(0)
    count = 0
    if level == 1:
        count = 10
    elif level == 2:
        count = 30
    elif level == 3:
        count = 50
    count = random.randrange(count, count+11)
    order = [i for i in range(81)]
    random.shuffle(order)
    for i in range(count):
        idx = order.pop()
        now_i = idx//9
        now_j = idx % 9
        table[now_i][now_j] = 0


def findcolor(tmp):
    if tmp == 1:
        tmp_color = "WHITE"
    elif tmp == 2:
        tmp_color = "PINK"
    elif tmp == 3:
        tmp_color = "PURPLE"
    elif tmp == 4:
        tmp_color = "SKYBLUE"
    elif tmp == 5:
        tmp_color = "LIGHTGREEN"
    elif tmp == 6:
        tmp_color = "YELLOW"
    elif tmp == 7:
        tmp_color = "ORANGE"
    elif tmp == 8:
        tmp_color = "RED"
    return tmp_color


def drawmain(self, index, check):
    self.fill(color["SKYBLUE"])
    fontmain = pygame.font.Font(None, 50)
    frontinfo = pygame.font.Font(None, 40)
    txtmain = fontmain.render("Welcome to Sudoku", True, color["BLACK"])
    txtstart = frontinfo.render("start game", True, color["BLACK"])
    txtscore = frontinfo.render("score board", True, color["BLACK"])
    txtsetting = frontinfo.render("settings", True, color["BLACK"])
    txtend = frontinfo.render("exit", True, color["BLACK"])
    self.blit(txtmain, (200, 50))
    self.blit(txtstart, (30, 400))
    self.blit(txtscore, (30, 430))
    self.blit(txtsetting, (30, 460))
    self.blit(txtend, (30, 490))
    if index == 0 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[180, 415], [180+10*3**0.5, 425], [180+10*3**0.5, 405]])
    elif index == 1 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[198, 445], [198+10*3**0.5, 455], [198+10*3**0.5, 435]])
    elif index == 2 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[153, 475], [153+10*3**0.5, 485], [153+10*3**0.5, 465]])
    elif index == 3 and check:
        pygame.draw.polygon(
            self, color["BLACK"], [[90, 505], [90+10*3**0.5, 515], [90+10*3**0.5, 495]])
    pygame.display.flip()


def endGame(self):
    global flag
    for i in range(9):
        for j in range(9):
            table[i][j] = 0
            board[i][j] = 0
    for i in range(10):
        for j in range(10):
            row[i][j] = 0
            col[i][j] = 0
            diag[i][j] = 0
    flag = False


def stopGame(self):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


def drawwGameScreen(self):
    global now_x
    global now_y
    self.fill(color["YELLOW"])
    pygame.draw.rect(self, color["BLACK"], [50, 50, 450, 450], 3)
    pygame.draw.line(self, color["BLACK"], [200, 50], [200, 500], 3)
    pygame.draw.line(self, color["BLACK"], [350, 50], [350, 500], 3)
    pygame.draw.line(self, color["BLACK"], [50, 200], [500, 200], 3)
    pygame.draw.line(self, color["BLACK"], [50, 350], [500, 350], 3)
    for i in range(100, 500, 50):
        pygame.draw.line(self, color["BLACK"], [50, i], [500, i], 1)
        pygame.draw.line(self, color["BLACK"], [i, 50], [i, 500], 1)
    font = pygame.font.Font(None, 50)
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0:
                tmp = font.render(str(table[i][j]), True, color["BLACK"])
                self.blit(tmp, (65+j*50, 60+i*50))
    pygame.draw.rect(self, color["WHITE"], [
                     50+now_y*50, 50+now_x*50, 50, 50], 2)
    pygame.display.flip()


def startGame(self):
    run = True
    global now_x
    global now_y
    global start_time
    global end_time
    global game_time
    game_time = pygame.time.get_ticks()
    initTable(1)
    drawwGameScreen(self)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stopGame(self)
                if event.key == pygame.K_UP:
                    if now_x > 0:
                        now_x -= 1
                    drawwGameScreen(self)
                if event.key == pygame.K_DOWN:
                    if now_x < 8:
                        now_x += 1
                    drawwGameScreen(self)
                if event.key == pygame.K_LEFT:
                    if now_y > 0:
                        mow_y -= 1
                    drawwGameScreen(self)
                if event.key == pygame.K_RIGHT:
                    if now_y < 8:
                        now_y += 1
                    drawwGameScreen(self)


def initgame():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("SudokU")
    global start_time
    idx = 0
    check = 0
    run = True
    start_time = pygame.time.get_ticks()
    while run:
        tmp_time = pygame.time.get_ticks()
        if tmp_time-start_time >= 600:
            start_time = tmp_time
            check = abs(check-1)
            drawmain(screen, idx, check)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if idx == 0:
                        startGame(screen)
                        check = 1
                        start_time = pygame.time.get_ticks()
                        drawmain(screen, idx, check)
                    elif idx == 1:
                        screen.fill(color["PINK"])
                        pygame.display.flip()
                    elif idx == 2:
                        screen.fill(color["LIGHTGREEN"])
                        pygame.display.flip()
                    elif idx == 3:
                        run = False
                elif event.key == pygame.K_UP:
                    idx -= 1
                    idx %= 4
                    check = 1
                    start_time = pygame.time.get_ticks()
                    drawmain(screen, idx, check)
                elif event.key == pygame.K_DOWN:
                    idx += 1
                    idx %= 4
                    check = 1
                    start_time = pygame.time.get_ticks()
                    drawmain(screen, idx, check)


initgame()
pygame.quit()
