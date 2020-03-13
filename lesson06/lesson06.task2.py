class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_count(self):
        return self._length * self._width * 25 * 5


road = Road(100, 20)
print(road.road_count())