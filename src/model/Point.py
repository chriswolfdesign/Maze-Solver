class Point:
    def __init__(self, x, y, parent=None):
        self._x = x
        self._y = y
        self._parent = parent

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_parent(self):
        return self._parent

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.get_x() == other.get_x() and self.get_y() == other.get_y()
