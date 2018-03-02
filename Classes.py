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


class Vehicle:
    def __init__(self):
        """All vehicles should start from (0, 0)"""
        self.currPos = Intersection(0, 0)
        self.isBusy = False
        self.assignedRides = list()
        self.currRide = None

    def __str__(self):
        """Return the string formed from the list with all assigned rides;

        Very useful for the output
        """
        return self.assignedRides.join(" ")

    def checkIfPossibleAndAssignRide(self, newRide, currStep):
        """Check whether the ride can be completed on time and assigns it;

        Returns True if assigned and False if not assigned.
        """
        # the minimum time required to accomplish the Ride
        # equals the distance
        # from the current position of the car
        # to the last intersection of the Ride
        minTimeToGo = distanceBetween(self.currPos, newRide.endPos)

        if minTimeToGo <= newRide.latestStep - currStep:
            self.currRide = newRide
            self.assignedRides.append(newRide)
            self.isBusy = True
            return True
        else:
            print "Unable to complete the ride in time"
            return False
