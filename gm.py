import sys
import time
import subprocess as sp
import random
import os

from coordinates import CoordinateX, CoordinateY
from input import Keyboard


def saveLog(**obj):
    obj = str(obj)
    with open("log.txt", "a") as f:
        f.write(obj + "\n")


class Player:
    def __init__(self) -> None:
        self.sprite = "x"
        self.x_coord = CoordinateX("  ")
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
        self.x_coord = CoordinateX("  ")
        self.y_coord = CoordinateY("\n")
        self.enemy_state = ""

    def updateEnemyState(self, terminal_size):
        self.x_coord.clear()
        self.y_coord.clear()
        x = random.randint(0, terminal_size[0])
        self.x_coord + x
        y = random.randint(0, terminal_size[1])
        self.y_coord + y
        # saveLog(x=x, y=y)
        # saveLog(enemyx=self.x_coord.x_coord, enemyy=self.y_coord.y_coord)
        state = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.enemy_state = state
        return state
    
    def getCoords(self):
        return [self.x_coord.x_coord, self.y_coord.y_coord]


class Test:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.kb_input = Keyboard()
        self.terminal_size = self.getTerminalSize()

    def draw(self, obj, clear_time=0.000016):
        print(obj, end="", flush=True)
        time.sleep(clear_time)
        sp.call("clear", shell=True)

    def checkIfScore(self):
        cond1 = self.player.y_coord == self.enemy.y_coord
        cond2 = self.player.x_coord == self.enemy.x_coord
        saveLog(y=cond1)
        saveLog(playery=self.player.y_coord.y_coord, enemyy=self.enemy.y_coord.y_coord)
        saveLog(x=cond2)
        saveLog(playerx=self.player.x_coord.x_coord, enemyx=self.enemy.x_coord.x_coord)
        return cond1 and cond2

    def getTerminalSize(self):
        self.terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        return self.terminal_size

    def move(self, up=False, down=False, left=False, right=False):
        if up:
            self.player.y_coord - 1
        if down:
            if not self.player.y_coord.y_coord > self.terminal_size[1]:
                self.player.y_coord + 1
        if left:
            self.player.x_coord - 1
        if right:
            if not self.player.x_coord.x_coord > self.terminal_size[0]:
                self.player.x_coord + 1
        self.player.updatePlayerState()

    def mainLoop(self):
        self.enemy.updateEnemyState(self.terminal_size)
        clear_time = 0.0000016
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
            self.draw(self.player.player_state, clear_time=clear_time)
            self.draw(self.enemy.enemy_state, clear_time=clear_time)
            if self.checkIfScore():
                self.enemy.updateEnemyState(self.terminal_size)
            # content = "\t\t" + str(self.terminal_size) + "\n\t\t" + str(self.player.getCoords()) + "\n\t\t" + str(self.enemy.getCoords())
            # self.draw(content, clear_time=clear_time)
            # self.draw("\n" + str(self.player.getCoords()) + "\n" + str(self.enemy.getCoords()), clear_time=clear_time)
            # self.enemy.updateEnemyState(self.terminal_size)
        sp.call("clear", shell=True)
        print("Encerrado!")


if __name__ == "__main__":
    test = Test()
    print("Use WASD para mover!")
    input("Aperte ENTER para iniciar!")
    test.mainLoop()
    