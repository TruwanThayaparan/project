"""
AQA GCSE Computer Science – Programming Project NEA  
Airport Task – Incomplete Solution

Author: TT
School: PS
Date Created: 14/07/2025  
Status: Work in Progress – to be updated after next lesson

Note: This solution is for educational purposes only and must not be plagiarised.  
      You are encouraged to develop your own original project to demonstrate your skills.

Description:
This project aims to solve the Airport Task provided by AQA in June 2021.  
Although students can now choose any project, I chose this one as I didn't have any ideas at the time.
"""

# requirements
import csv

# setup

# airport details
airport_codes = []
airport_names = []
distance_from_liverpool = [] # Liverpool John Lennon Airport
distance_from_bournemouth = [] # Bournemouth International Airport

# flight details
'''
order:
type
running cost per seat per 100 km
maximum flight range (km)
capacity if all seats are standard-class
minimum number of first-class seats (if there are any)
'''


aircrafts = {
    "medium narrow body": [8, 2650, 180, 8],
    "large narrow body": [7, 5600, 220, 10],
    "medium wide body": [5, 4050, 406, 14]
}

# initalise variables
uk_code = None
abroad_code = None

aircraft = None
first_class_seats = None
dist_between = None

# get the details from the csv
with open('Airports.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        airport_codes.append(row[0])
        airport_names.append(row[1])
        distance_from_liverpool.append(int(row[2]))
        distance_from_bournemouth.append(int(row[3]))

# main menu
def menu():
    while True:
        print("\nSelect an option:")
        print("1. Enter airport details")
        print("2. Enter flight details")
        print("3. Enter price plan and calculate profit")
        print("4. Clear data")
        option = input().lower().strip()
        if option in ("enter airport details", "1"):
            uk_code, abroad_code, dist_between = airport_details()
        elif option in ("enter flight details", "2"):
            aircraft, first_class_seats = flight_details()
        elif option in ("enter price plan and calculate profit", "3"):
            t = calculate_profit_pp()
        elif option in ("clear data", "4"):
            uk_code, abroad_code, aircraft, first_class_seats, dist_between = None
            print("Data has been cleared!")
        else:
            print("That is not a valid option!")

# enter airport details
def airport_details():
    # enter airport code UK (apcu)
    apcu = input("Enter the three-letter airport code (UK): ").upper().strip()
    if apcu not in ("LPL", "BOH"):
        print("That is not a valid three-letter code.")
        return None, None

    # enter airport code abroad (apca)
    apca = input("Enter the three-letter airport code (ABROAD): ").upper().strip()
    for p in airport_codes: # check if it's valid
        if apca == p:
            idx = airport_codes.index(p)
            print(airport_names[idx])

            if apcu == "LPL":
                length = distance_from_liverpool[idx]
            else:
                length = distance_from_bournemouth[idx]

            print(length)
            return apcu, apca, length

    print("A airport could not be found with this code.")
    return None, None

# enter flight details
def flight_details():
    # enter aircraft (ac)
    ac = input("Enter the type of aircraft that will be used: ").lower().strip()

    if ac not in aircrafts: # check if it exists
        print("That is not a valid type of aircraft.")
        return None, None
    else:
        idx = [ac] + aircrafts[ac]
        #print(idx)

    information = ("running cost per seat per 100 km: " + str(aircrafts[ac][0]) + "\n" +
           "maximum flight range (km): " + str(aircrafts[ac][1]) + "\n" +
           "capacity if all seats are standard-class: " + str(aircrafts[ac][2]) + "\n" +
           "minimum number of first-class seats: " + str(aircrafts[ac][3]))
    print(information)
    
    # check number of first-class seats
    while True:
        try:
            fc_seats = int(input("Enter the number of first-class seats: "))
            break
        except ValueError:
            print("You must enter a integer.")

    # check for issues
    if fc_seats != 0:
        if fc_seats < aircrafts[ac][3]:
            print("Number of first-class seats must not be less than minimum number of first-class seats!")
            return None, None
        if fc_seats > (aircrafts[ac][2] / 2):
            print("Number of first-seats seats must not be greater than half the capacity if all seats are standard-class!")
            return None, None

    # calculate number of standard-class seats on aircraft
    standard_class_seats = aircrafts[ac][2] - fc_seats * 2
    return ac, fc_seats

# enter price plan (pp) and calculate profit
def calculate_profit_pp():

    # check if all details entered
    if uk_code == None or abroad_code == None:
        print("Airport details have not been entered yet (missing airport codes).")
        return None
    if aircraft == None:
        print("Flight details have not been entered yet (missing aircraft).")
        return None
    if first_class_seats == None:
        print("Flight details have not been entered yet (missing number of first class seats).")
        return None

    if aircrafts[aircraft][1] >= dist_between: 
        pass
    else:
        print("Distance between airports exceeds maximum flight range for this aircraft.")
        return None

    # enter prices for standard class and first-class seats
    while True:
        try:
            sc_seat = float(int("Enter price for standard-class seat: "))
            break
        except:
            print("You must enter a number.")

    while True:
        try:
            sc_seat = float(int("Enter price for first-class seat: "))
            break
        except:
            print("You must enter a number.")

    # formula (didn't have time to do this today, will add tomorrow)

# start
menu()
