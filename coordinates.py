class CoordinateX:
    def __init__(self, char) -> None:
        self.char = char
        self.x_coord_list = []
        self.x_coord = self.updateCoordLen()

    def updateCoordLen(self):
        self.x_coord = len(self.x_coord_list)
        return len(self.x_coord_list)

    def clear(self):
        self.x_coord_list = []
        self.updateCoordLen()

    def __add__(self, value):
        for x in range(value):
            self.x_coord_list.append(self.char)
        self.x_coord = self.updateCoordLen()

    def __sub__(self, value):
        if self.x_coord_list and value <= self.x_coord:
            self.x_coord_list.remove(self.char)
        self.x_coord = self.updateCoordLen()

    def __eq__(self, o: object) -> bool:
        if self.x_coord == o.x_coord:
            if len(self.x_coord_list) == len(o.x_coord_list):
                return True
        return False

    def __str__(self):
        return str(self.x_coord)


class CoordinateY:
    def __init__(self, char) -> None:
        self.char = char
        self.y_coord_list = []
        self.y_coord = self.updateCoordLen()

    def updateCoordLen(self):
        self.y_coord = len(self.y_coord_list)
        return len(self.y_coord_list)
    
    def clear(self):
        self.y_coord_list = []
        self.updateCoordLen()

    def __add__(self, value):
        for x in range(value):
            self.y_coord_list.append(self.char)
        self.x_coord = self.updateCoordLen()

    def __sub__(self, value):
        if self.y_coord_list and value <= self.y_coord:
            self.y_coord_list.remove(self.char)
        self.y_coord = self.updateCoordLen()
    
    def __eq__(self, o: object) -> bool:
        if self.y_coord == o.y_coord:
            if len(self.y_coord_list) == len(o.y_coord_list):
                return True
        return False
    
    def __str__(self):
        return str(self.y_coord)