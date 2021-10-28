from coordinates import CoordinateX, CoordinateY
import random


class Player:
    def __init__(self) -> None:
        self.sprite: str = "x"
        self.x_coord: CoordinateX = CoordinateX(" ")
        self.y_coord: CoordinateY = CoordinateY("\n")
        self.player_state: str = self.updatePlayerState()
    
    def updatePlayerState(self) -> str:
        state: str = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.player_state = state
        return state

    def getCoords(self) -> list:
        return [self.x_coord.x_coord, self.y_coord.y_coord]

    def __str__(self) -> str:
        return self.player_state


class Enemy:
    def __init__(self) -> None:
        self.sprite: str = "o"
        self.x_coord: CoordinateX = CoordinateX(" ")
        self.y_coord: CoordinateY = CoordinateY("\n")
        self.enemy_state: str = ""

    def updateEnemyState(self, terminal_size):
        self.x_coord.clear()
        self.y_coord.clear()
        x: int = random.randint(0, terminal_size[0] - 2)
        y: int = random.randint(0, terminal_size[1] - 2)
        if x == 0 and y == 0:
            return self.updateEnemyState()
        self.x_coord + x
        self.y_coord + y
        state: str = ""
        state += "".join(self.y_coord.y_coord_list)
        state += "".join(self.x_coord.x_coord_list)
        state += self.sprite
        self.enemy_state = state
        return state
    
    def getCoords(self) -> list:
        return [self.x_coord.x_coord, self.y_coord.y_coord]

    def __str__(self) -> str:
        return self.player_state