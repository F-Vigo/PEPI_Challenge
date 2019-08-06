############################## INTRODUCTION ##############################


"""
Challenge for The Workshop.
Applicant: VIGO GARCIA, FRANCISCO.
Date: 06/08/2019.
"""



############################## PREPARATION ##############################


class City:
    def __init__(self, name, reward, isBase = False):
        self.name = name
        self.reward = reward
        self.isBase = isBase

cities = {} # Dictionary of the cities in the instance which maps the name of the city to the actual object of type city.
connections = {} # Dictionary that maps every city to their connected cities as well as the corresponding petrol expenses.


def balance(tour): # We call a tour the whole itinerary the player follows. This function gets the actual balance of the tour.
    length = len(tour)
    visited = []

    income = 0
    for i in range(length):
        if not tour[i] in visited: # The reward is obtained only the first time a city is visited.
            income += cities[tour[i]].reward
            visited.append(tour[i])
    expenses = 0
    for i in range(length-1):
        expenses += connections[tour[i]][tour[i+1]]

    return income - expenses
        



############################## INPUT FROM FILE ##############################


instanceFile = open("exercise1.json",'r')

# Unneccessary lines.
instanceFile.readline()
instanceFile.readline()


keepReading = True
while keepReading: # Filling cities.
    
    if instanceFile.readline()[-2] == '{': # The description of a new city starts.
        name = instanceFile.readline()[17:-3]
        line = instanceFile.readline()
        if line[9:13] == "base":
            isBase = True
            line = instanceFile.readline()
        else:
            isBase = False
        reward = int(line[18:-1])
        instanceFile.readline()
        cities[name] = City(name, reward, isBase)
        connections[name] = {}
        
    else: # There is a ']' in the file. No more cities left.
        keepReading = False


instanceFile.readline() # We skip the line '"connections": ['.


keepReading = True
while keepReading: # Filling connections.
    
    if instanceFile.readline()[-2] == '{':
        departure = instanceFile.readline()[17:-3] # "from".
        arrival = instanceFile.readline()[15:-3] # "to".
        cost = int(instanceFile.readline()[16:-1])
        instanceFile.readline()
        
        connections[departure][arrival] = cost
        connections[arrival][departure] = cost
    else:
        keepReading = False


instanceFile.close()



############################## GETTING THE SOLUTION ##############################


base = ""
for c in cities:
    if cities[c].isBase:
        base = c
        break


def toursWithLength(n): # Generates all valid tours of length n.
    newTourList = [[base]]
    
    for i in range(2,n+1): # The loop does nothing for n < 2, as would be desirable.
        oldTourList = newTourList.copy() # Tours with i-1 "setps" taken, that is, i-1 cities visited.
        newTourList = []
        for prevTour in oldTourList:
            x = prevTour[-1] # Last city visited.
            for y in connections[x]: # All possible new cities visited.
                z = prevTour.copy()
                z.append(y) # The path the player had already taken (unfinished yet) plus a new valid city.
                newTourList.append(z)

    return list(filter(lambda x : x[-1] == base, newTourList)) # We accept the turs which end in the base.


def toursUpTo(n): # Generates all valid tours for at most n days.
    result = []
    for i in range(1,n+2): # The player visits n+1 cities (taking into account the base and the beginning and the end as well as repeated cities) in n days.
        result = result + toursWithLength(i)
    return result


def mainFunction(n): # Function that gives the optimal tours.
    tourBalances = [(x, balance(x)) for x in toursUpTo(n)]
    
    maxBalance = max(list(map(lambda x : x[1], tourBalances)))
    maximalTours = list(filter(lambda x : x[1] == maxBalance, tourBalances))
    
    minLength = min(list(map(lambda x : len(x[0]), maximalTours)))
    optimalTours = list(filter(lambda x : len(x[0]) == minLength, maximalTours))
    
    return optimalTours



############################## CONSOLE ##############################


x = input("Have you placed the data file at the script folder? (Y/N) ").upper()
keepAsking = True
while keepAsking:
    if x != 'Y' and x != 'N':
        x = input("Please, repeat your answer. (Y/N) ").upper()
    elif x == 'N':
        x = input("Please, place the data file at the script folder. Have you done it yet? (Y/N) ").upper()
    else:
        keepAsking = False

n = input("Please, enter the maximum number of days (7 in the instructions of the challenge). ")
keepAsking = True
while keepAsking:
    if not n.isdigit():
        n = input("Please, enter a valid number.")
    elif int(n) <= 0:
        n = input("Please, enter a valid number.")
    else:
        keepAsking = False
        n = int(n)

print("The solution(s) is: " + str(mainFunction(n)) + ".")
