import time
import subprocess as sp
import os
import sys

from input import Keyboard
from Scores import HiScores
from MovableObjects import Enemy, Player


def saveLog(**obj):
    # DEBUG
    obj = str(obj)
    with open("log.txt", "a") as f:
        f.write(obj + "\n")


class Test:
    def __init__(self, name: str="", speed: int=100) -> None:
        if name == "":
            name = "Guest"
        self.speed = (0.00016 * speed) / 100
        self.playername: str = name
        self.player: Player = Player()
        self.enemy: Enemy = Enemy()
        self.kb_input: Keyboard = Keyboard()
        self.scoreLog: HiScores = HiScores()
        self.terminal_size: list = self.getTerminalSize()
        self.score: int = 0

    def draw(self, obj, clear_time: float=0) -> None:
        if clear_time == 0:
            clear_time = self.speed
        print(obj, end="", flush=True)
        time.sleep(clear_time)
        sp.call("clear", shell=True)

    def checkIfScore(self) -> bool:
        cond1: bool = self.player.y_coord == self.enemy.y_coord
        cond2: bool = self.player.x_coord == self.enemy.x_coord
        if cond1 and cond2:
            self.score += 1
        return cond1 and cond2

    def getTerminalSize(self) -> list:
        self.terminal_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        return self.terminal_size

    def move(self, up: bool=False, down: bool=False, left: bool=False, right: bool=False) -> None:
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
            print("Encerrado!".center(self.terminal_size[0]))
            print("Hi-Score".center(self.terminal_size[0], "-"))
            print()
            print("".join([x.center(self.terminal_size[0]) for x in self.scoreLog.output().split("\n")]))
            print("-".center(self.terminal_size[0], "-"))


def argparser(args=sys.argv[1:]):
    if args:
        if "-s" in args or "--speed" in args:
            if len(args) > 1:
                try:
                    x = int(args[1])
                    return x
                except ValueError:
                    return 100
            else:
                print("Erro! Valor invalido!")
                raise SystemExit
        else:
            print("Erro! Flag não encontrada!")
            raise SystemExit
    return 100


if __name__ == "__main__":
    v = argparser()
    try:
        print("Use WASD para mover!")
        test = Test(input("Insira seu nome e aperte ENTER para iniciar: "), speed=v)
    except KeyboardInterrupt:
        print("Encerrado pelo usuario!")
        raise SystemExit
    test.mainLoop()
