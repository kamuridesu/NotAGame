class CoordinateX:
    def __init__(self, char: str) -> None:
        self.char: str = char
        self.x_coord_list: list = []
        self.x_coord: int = self.updateCoordLen()

    def updateCoordLen(self) -> int:
        self.x_coord = len(self.x_coord_list)
        return len(self.x_coord_list)

    def clear(self) -> None:
        self.x_coord_list = []
        self.updateCoordLen()

    def __add__(self, value: int) -> None:
        for x in range(value):
            self.x_coord_list.append(self.char)
        self.x_coord = self.updateCoordLen()

    def __sub__(self, value: int) -> None:
        if self.x_coord_list and value <= self.x_coord:
            self.x_coord_list.remove(self.char)
        self.x_coord = self.updateCoordLen()

    def __eq__(self, o: object) -> bool:
        if self.x_coord == o.x_coord:
            return len(self.x_coord_list) == len(o.x_coord_list)
        return False

    def __str__(self) -> str:
        return str(self.x_coord)


class CoordinateY:
    def __init__(self, char: str) -> None:
        self.char: str = char
        self.y_coord_list: list = []
        self.y_coord: int = self.updateCoordLen()

    def updateCoordLen(self) -> int:
        self.y_coord = len(self.y_coord_list)
        return len(self.y_coord_list)
    
    def clear(self) -> None:
        self.y_coord_list = []
        self.updateCoordLen()

    def __add__(self, value: int) -> None:
        for x in range(value):
            self.y_coord_list.append(self.char)
        self.x_coord = self.updateCoordLen()

    def __sub__(self, value: int) -> None:
        if self.y_coord_list and value <= self.y_coord:
            self.y_coord_list.remove(self.char)
        self.y_coord = self.updateCoordLen()
    
    def __eq__(self, o: object) -> bool:
        if self.y_coord == o.y_coord:
            return len(self.y_coord_list) == len(o.y_coord_list)
        return False
    
    def __str__(self) -> str:
        return str(self.y_coord)