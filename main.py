"""Google Hash Code Challenge Attempt.

Author: Alexander Ignatov
Country: Bulgaria
2018
"""

from Classes import\
 Intersection as Intersection,\
 Ride as Ride,\
 Vehicle as Vehicle

# Make the neccessary lists
busyVehicles = list()
freeVehicles = list()

waitingRides = list()
pastRides = list()


# FILE input handler

filename = raw_input("Enter name of input file (without '.in' suffix): ")

try:
    inputFile = open('input/'+filename+'.in', "r")

except Exception:
    print "File operation unsuccessfull."
    exit()


firstRow = inputFile.readline()
firstRowArgs = firstRow.split()

# Save first row values
numberOfRowsR = int(firstRowArgs[0])
numberOfColsC = int(firstRowArgs[1])
numberOfVehiclesF = int(firstRowArgs[2])
numberOfRidesN = int(firstRowArgs[3])
perRideBonusB = int(firstRowArgs[4])
numberOfStepsT = int(firstRowArgs[5])

# Save and create all rides (the remaining N rows of the file)
for i in range(numberOfRidesN):
    currLineArgs = inputFile.readline().split()

    startRow = int(currLineArgs[0])
    startCol = int(currLineArgs[1])
    endRow = int(currLineArgs[2])
    endCol = int(currLineArgs[3])
    earliestStep = int(currLineArgs[4])
    latestStep = int(currLineArgs[5])

    newRide = Ride(Intersection(startRow, startCol),
                   Intersection(endRow, endCol),
                   earliestStep,
                   latestStep,
                   i)

    waitingRides.append(newRide)

# Input reading finished
inputFile.close()

# Spawn F Vehicles
for f in range(numberOfVehiclesF):
    freeVehicles.append(Vehicle())


# ----------
# SIMULATION
# ----------
for currStep in range(numberOfStepsT):
    # Sort the waiting rides by 'emergency'
    waitingRides = sorted(waitingRides, key=lambda ride: ride.earliestStep)

    for ride in waitingRides:
        # Some rides may be impossible to complete; we skip them
        if ride.latestStep < currStep:
            waitingRides.remove(ride)
            pastRides.append(ride)
            continue

        # Sort the free vehicles from closest to farthest
        freeVehicles = sorted(
            freeVehicles,
            key=lambda taxi:
                taxi.distanceToRide(ride)
        )

        for taxi in freeVehicles:
            # Find the most suitable vehicle for the ride, if any
            if taxi.checkIfPossibleAndAssignRide(ride, currStep):
                freeVehicles.remove(taxi)
                busyVehicles.append(taxi)

                waitingRides.remove(ride)
                pastRides.append(ride)
                break

    # After assigning all possible rides to vehicles,
    # move the busy vehicles the correct correct step
    for taxi in busyVehicles:
        taxi.move(currStep)

        # we should free the taxi if it reaches its destination now
        if taxi.hasReachedDestination():
            taxi.isBusy = False
            freeVehicles.append(taxi)
            busyVehicles.remove(taxi)

# -----------------
# END OF SIMULATION
# -----------------


# Output to file
with file("output/"+filename+".out", "w") as outputFile:
    for taxi in (freeVehicles + busyVehicles):
        outputFile.write(str(len(taxi.assignedRides))+" "+repr(taxi)+"\n")
