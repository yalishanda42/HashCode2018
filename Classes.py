"""Define all needed classes and methods related to them."""


class Intersection:
    """Defines an intersection by its position"""

    def __init__(self, row, col):
        self.row = row
        self.col = col


def distanceBetween(Intersection1, Intersection2):
    """Return the distance between two intersections"""
    return abs(Intersection1.row - Intersection2.row)\
        + abs(Intersection1.col - Intersection2.col)


class Ride:
    """Defines a ride by its input parameters"""

    def __init__(self,
                 startIntersection,
                 endIntersection,
                 earliestStepToStart,
                 latestStepToFinish):
        self.startPos = startIntersection
        self.endPos = endIntersection
        self.earliestStep = earliestStepToStart
        self.latestStep = latestStepToFinish

    def __str__(self):
        """Return all ride parameters in a single-line string; for test only"""
        return self.startPos.row,\
            self.startPos.col,\
            self.endPos.row,\
            self.endPos.col,\
            self.earliestStep,\
            self.latestStep


class Vehicle:
    pass
