import sys
import time
from coordinates import CoordinateX, CoordinateY
from input import Keyboard
import subprocess as sp


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


class Test:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.kb_input = Keyboard()

    def draw(self, clear_time=0.0016):
        print(self.player.player_state, end="", flush=True)
        sp.call("clear", shell=True)
        time.sleep(clear_time)

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
        while True:
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
            self.draw()


if __name__ == "__main__":
    test = Test()
    print("Use WASD para mover!")
    input("Aperte ENTER para iniciar!")
    test.mainLoop()