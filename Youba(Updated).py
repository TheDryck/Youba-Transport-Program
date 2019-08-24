def driver_make(firstName, lastName, carMakeAndModel, numberOfTripsCompleted=0):
    return ('Driver', [firstName, lastName, carMakeAndModel, numberOfTripsCompleted])


def getDriverInfo(Driver):
    #print(Driver)
    return Driver[1]


def driver_getFirstName(Driver):
    return getDriverInfo(Driver)[0]


def driver_getLastName(Driver):
    return getDriverInfo(Driver)[1]


def driver_getCarMakeAndModel(Driver):
    return getDriverInfo(Driver)[2]


def driver_getNumberOfTripsCompleted(Driver):
    return getDriverInfo(Driver)[3]


def driver_increaseTripsCompleted(Driver):
    if (Driver[0] == 'Driver'):
        getDriverInfo(Driver)[3] = driver_getNumberOfTripsCompleted(Driver) + 1


def driver_isNewDriver(Driver):
    return driver_getNumberOfTripsCompleted(Driver) == 0


def availabilityQueue_make(LocationName):
    return ('AvailabilityQueue', LocationName, [])


def get_Drlist(availabilityQueue):
    return availabilityQueue[2]


def availabilityQueue_getLocationName(availabilityQueue):
    return availabilityQueue[1]


def availabilityQueue_front(availabilityQueue):
    return get_Drlist(availabilityQueue)[0]


def availabilityQueue_enqueue(availabilityQueue, Driver):
    get_Drlist(availabilityQueue).append(Driver)


def availabilityQueue_dequeue(availabilityQueue):
    get_Drlist(availabilityQueue).pop(0)


def availabilityQueue_isEmpty(availabilityQueue):
    return get_Drlist(availabilityQueue) == []


availabilityQueue_UWI = availabilityQueue_make('UWI')

availabilityQueue_Papine = availabilityQueue_make('Papine')

availabilityQueue_Liguanea = availabilityQueue_make('Liguanea')

availabilityQueue_HalfWayTree = availabilityQueue_make('Half-Way-Tree')



def getAvailabilityQueue(LocationName):
    for availabilityQueue in  availabilityQueue_LIST:
        if availabilityQueue_getLocationName(availabilityQueue) == LocationName:
            return availabilityQueue
        
def calculateDiscount(PassengerTelephoneNumber):
    discount = 0
    for k in knownPassengers:
        if PassengerTelephoneNumber == k:
            discount = knownPassengers[k] * 0.10
    return discount

def getFare():
    return fare

Fare = 100
def calculateFare(StartLocation, EndLocation, PassengerTelephoneNumber):
    new = getFare() - (calculateDiscount(PassengerTelephoneNumber) * getFare())
    return float(new)


locations = {'UWI':availabilityQueue_UWI, 'Papine':availabilityQueue_Papine, 'Liguanea':availabilityQueue_Liguanea, 'Half-Way-Tree':availabilityQueue_HalfWayTree}

def moveTaxi(StartLocation, EndLocation):  
    if not availabilityQueue_isEmpty(locations[StartLocation]):
        fDriver = availabilityQueue_front(locations[StartLocation])
        availabilityQueue_dequeue(locations[StartLocation])
        availabilityQueue_enqueue(locations[EndLocation], fDriver)
        driver_increaseTripsCompleted(fDriver)
        
        
def requestTaxi(PassengerTelephoneNumber, PassengerLocation, PassengerDestination):
    if PassengerLocation == PassengerDestination:
        print ('Error: Your Location and Destination are the same')

    else:
        calculateFare(PassengerLocation, PassengerDestination, PassengerTelephoneNumber)
        #ans = input("Please enter 'Y' to confirm or 'N' to cancel this action")
        if request == 'Y':
            if not availabilityQueue_isEmpty(locations[PassengerLocation]):
                fDriver = availabilityQueue_front(locations[PassengerLocation])
                moveTaxi(PassengerLocation, PassengerDestination)
                driver_increaseTripsCompleted(fDriver)
                for k in knownPassengers:
                    if PassengerTelephoneNumber == k:
                        knownPassengers[k] = 0
            else:
                for k in knownPassengers:
                    if PassengerTelephoneNumber == k:
                        knownPassengers[k] += 1
                        return "There are no available drivers in your location"
