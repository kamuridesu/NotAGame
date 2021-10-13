import sys
import time
import subprocess as sp
import random
import os

from coordinates import CoordinateX, CoordinateY
from input import Keyboard


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


class Enemy:
    def __init__(self) -> None:
        self.sprite = "o"
        self.x_coord = CoordinateX("  ")
        self.y_coord = CoordinateY("\n")
        self.enemy_state = ""

    def updateEnemyState(self, terminal_size):
        x = random.randint(0, terminal_size[1])
        self.x_coord + x
        y = random.randint(0, terminal_size[0])
        self.y_coord + y
        state = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.enemy_state = state
        return state


class Test:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.kb_input = Keyboard()
        self.terminal_size = self.getTerminalSize()

    def draw(self, obj, clear_time=0.000016):
        print(obj, end="", flush=True)
        sp.call("clear", shell=True)
        time.sleep(clear_time)

    def checkGameOver(self):
        self.draw(str(self.player.y_coord) + "\n" + str(self.enemy.y_coord))
        if self.player.y_coord == self.enemy.y_coord:
            if self.player.x_coord == self.enemy.x_coord:
                return True
        return False

    def getTerminalSize(self):
        self.terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        return self.terminal_size

    def move(self, up=False, down=False, left=False, right=False):
        if up:
            self.player.y_coord - 1
        if down:
            self.player.y_coord + 1
        if left:
            self.player.x_coord - 1
        if right:
            self.player.x_coord + 1
        self.player.updatePlayerState()

    def mainLoop(self):
        self.enemy.updateEnemyState(self.terminal_size)
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
            self.draw(self.player.player_state)
            self.draw(self.enemy.enemy_state)
            if self.checkGameOver():
                break
        sp.call("clear", shell=True)
        print("Encerrado!")


if __name__ == "__main__":
    test = Test()
    print("Use WASD para mover!")
    input("Aperte ENTER para iniciar!")
    test.mainLoop()
    