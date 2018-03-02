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


def cmpInters(Intersection1, Intersection2):
    """Return True if both intersections have equal parameters"""
    return Intersection1.row == Intersection2.row and\
        Intersection1.col == Intersection2.col


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
        self.assignedRides = list()
        self.isBusy - False
        self.currRide = None
        self.hasReachedRideStartPos = False

    def __str__(self):
        """Return the string formed from the list with all assigned rides;

        Very useful for the output
        """
        return self.assignedRides.join(" ")

    def distanceToRide(self, ride):
        """Return the distance to the start intersection of a ride"""
        return distanceBetween(self.currPos, ride.startPos)

    def hasReachedDestination(self):
        return cmpInters(self.currPos, self.currRide.endPos)

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
            self.hasReachedRideStartPos = False
            return True
        else:
            print "Unable to complete the ride in time"
            return False

    def move(self, currStep):
        """Either moves the vehicle one step towards its goal
        or stays in the same place according to the rules
        of the simulation
        """
        # First we move it to the correct row
        # Then to the correct column
        # TBA...
