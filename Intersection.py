class Intersection:
    """Defines an intersection by its position"""

    def __init__(self, row, col):
        self.row = row
        self.col = col


def distanceBetween(Intersection1, Intersection2):
    """Return the distance between two intersections"""
    return abs(Intersection1.row - Intersection2.row)\
        + abs(Intersection1.col - Intersection2.col)
