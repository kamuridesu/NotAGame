import sys
import time
import subprocess as sp
import random
import os
import json

from coordinates import CoordinateX, CoordinateY
from input import Keyboard


def saveLog(**obj):
    obj = str(obj)
    with open("log.txt", "a") as f:
        f.write(obj + "\n")


class HiScores:
    def __init__(self, filename="scores.json"):
        self.filename = filename
    
    def saveScore(self, playername, score):
        scores = self.getAllScores()
        scores[playername] = score
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(scores))

    def getAllScores(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                return json.loads(f.read())
            except json.decoder.JSONDecodeError:
                return {}

    def generateHiScoreList(self):
        scores = self.getAllScores()
        sort = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
        out = ""
        for k, v in enumerate(sort.items()):
            out += str(k) + " - " + str(v[0]) + " == " + str(v[1]) + "\n"
        print(out)





class Player:
    def __init__(self) -> None:
        self.sprite = "x"
        self.x_coord = CoordinateX(" ")
        self.y_coord = CoordinateY("\n")
        self.player_state = self.updatePlayerState()
    
    def updatePlayerState(self):
        state = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.player_state = state
        return state

    def getCoords(self):
        return [self.x_coord.x_coord, self.y_coord.y_coord]


class Enemy:
    def __init__(self) -> None:
        self.sprite = "o"
        self.x_coord = CoordinateX(" ")
        self.y_coord = CoordinateY("\n")
        self.enemy_state = ""

    def updateEnemyState(self, terminal_size):
        self.x_coord.clear()
        self.y_coord.clear()
        x = random.randint(0, terminal_size[0] - 2)
        y = random.randint(0, terminal_size[1] - 2)
        if x == 0 and y == 0:
            return self.updateEnemyState()
        self.x_coord + x
        self.y_coord + y
        state = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.enemy_state = state
        return state
    
    def getCoords(self):
        return [self.x_coord.x_coord, self.y_coord.y_coord]


class Test:
    def __init__(self, name=""):
        if name == "":
            name = "Guest"
        self.playername = name
        self.player = Player()
        self.enemy = Enemy()
        self.kb_input = Keyboard()
        self.scoreLog = HiScores()
        self.terminal_size = self.getTerminalSize()
        self.score = 0

    def draw(self, obj, clear_time=0.00016):
        print(obj, end="", flush=True)
        time.sleep(clear_time)
        sp.call("clear", shell=True)

    def checkIfScore(self):
        cond1 = self.player.y_coord == self.enemy.y_coord
        cond2 = self.player.x_coord == self.enemy.x_coord
        if cond1 and cond2:
            self.score += 1
        return cond1 and cond2

    def getTerminalSize(self):
        self.terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        return self.terminal_size

    def move(self, up=False, down=False, left=False, right=False):
        if up:
            self.player.y_coord - 1
        if down:
            if not self.player.y_coord.y_coord > self.terminal_size[1] - 2:
                self.player.y_coord + 1
        if left:
            self.player.x_coord - 1
        if right:
            if not self.player.x_coord.x_coord > self.terminal_size[0] - 2:
                self.player.x_coord + 1
        self.player.updatePlayerState()
        self.draw(self.player.player_state)
        self.draw(self.enemy.enemy_state)
        self.draw(str(self.score))

    def mainLoop(self):
        self.enemy.updateEnemyState(self.terminal_size)
        self.draw(self.enemy.enemy_state)
        try:
            while True:
                self.getTerminalSize()
                up, down, left, right = [False for i in range(4)]
                if self.kb_input.hit():
                    key = self.kb_input.getch()
                    if ord(key) == 119: # w
                        up = True
                    if ord(key) == 97: # a
                        left = True
                    if ord(key) == 115: # s
                        down = True
                    if ord(key) == 100: # d
                        right = True
                self.move(up, down, left, right)
                if self.checkIfScore():
                    self.enemy.updateEnemyState(self.terminal_size)
        except KeyboardInterrupt:
            sp.call("clear", shell=True)
            self.scoreLog.saveScore(self.playername, self.score)
            print("Encerrado!")
            print("-" * 15 + "Hi-Score" + "-" * 15)



if __name__ == "__main__":
    # print("Use WASD para mover!")
    # test = Test(input("Insira seu nome e aperte ENTER para iniciar!"))
    # test.mainLoop()
    # test.getTerminalSize()
    log = HiScores()
    log.saveScore("kamuri", 2)
    log.saveScore("a", 5)
    log.saveScore("b", 3)
    log.generateHiScoreList()

