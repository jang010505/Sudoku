import pygame
import random  # asdhashfksad
from pygame.locals import *

table = [[0]*9 for i in range(9)]

now_i = 0
now_j = 0

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
            if checkSquare(i*3, j*3) == False:
                return False
    return True


def initTable(level):
    for i in range(9):
        for j in range(9):
            table[i][j] = 0
    for i in range(random.randrange(10, 21)):
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
    for i in range(9):
        for j in range(9):
            table[i][j] = 0


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
    `


def startGame(self):
    run = True
    global now_i
    global now_j
    global start_time
    global end_time
    global game_time
    game_time = pygame.time.get_ticks()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stopGame()
                if event.key == pygame.K_UP:
                    if now_i > 0:
                        now_i -= 1
                if event.key == pygame.K_DOWN:
                    if now_i < 8:
                        now_i += 1
                if event.key == pygame.K_LEFT:
                    if now_j > 0:
                        mow_j -= 1
                if event.key == pygame.K_RIGHT:
                    if now_j < 8:
                        now_j += 1


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
                        py  game.display.flip()
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
