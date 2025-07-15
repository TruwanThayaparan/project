"""
AQA GCSE Computer Science – Programming Project NEA  
Airport Task – Incomplete Solution

Author: TT
School: PS
Date Created: 15/07/2025  
Status: Completed

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

valid_uk_codes = ("LPL", "BOH")
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
dist_between = None
aircraft = None
first_class_seats = None
standard_class_seats = None

# get the details from the csv (if it exists)
try:
    with open('Airports.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            airport_codes.append(row[0])
            airport_names.append(row[1])
            distance_from_liverpool.append(int(row[2]))
            distance_from_bournemouth.append(int(row[3]))
except FileNotFoundError:
    print("The Airports.txt file is missing!")
    exit()


# main menu
def menu():
    global uk_code, abroad_code, dist_between, aircraft, first_class_seats, standard_class_seats
    
    while True:
        #print("-" * 40)
        print("\nSelect an option:")
        print("1. Enter airport details")
        print("2. Enter flight details")
        print("3. Enter price plan and calculate profit")
        print("4. Clear data")
        print("5. Exit")
        option = input().lower().strip()
        if option in ("enter airport details", "1"):
            uk_code, abroad_code, dist_between = airport_details()
        elif option in ("enter flight details", "2"):
            aircraft, first_class_seats, standard_class_seats = flight_details()
        elif option in ("enter price plan and calculate profit", "3"):
            t = calculate_profit_pp()
        elif option in ("clear data", "4"):
            uk_code, abroad_code, dist_between, aircraft, first_class_seats, standard_class_seats = None, None, None, None, None, None
            print("Data has been cleared! You may now re-enter new airport and flight information.")
        elif option in ("exit", "close", "5"):
            print("The program has ended.")
            break
        else:
            print("That is not a valid option!")


# enter airport details
def airport_details():
    # enter airport code UK (apcu)
    apcu = input("\nEnter the three-letter airport code (UK): ").upper().strip()
    if apcu not in valid_uk_codes:
        print("That is not a valid three-letter code.")
        return None, None, None
    
    # enter airport code abroad (apca)
    apca = input("Enter the three-letter airport code (ABROAD): ").upper().strip()
    for p in airport_codes:  # check if it's valid
        if apca == p:
            idx = airport_codes.index(p)
            print(airport_names[idx])

            if apcu == "LPL":
                length = distance_from_liverpool[idx]
            else:
                length = distance_from_bournemouth[idx]

            print(f"Distance between {apcu} and {apca}: {length} km")
            return apcu, apca, length 
              
    print("No airport could be found with that code.")
    return None, None, None


# enter flight details
def flight_details():
    # enter aircraft (ac)
    ac = input("\nEnter the type of aircraft that will be used: ").lower().strip()

    if ac not in aircrafts: # check if it exists
        print("That is not a valid type of aircraft.")
        return None, None, None
    
    #idx = [ac] + aircrafts[ac]
    #print(idx)

    # display information
    information = ("Running cost per seat per 100 km: £" + str(aircrafts[ac][0]) + "\n" +
           "Maximum flight range (km): " + str(aircrafts[ac][1]) + "\n" +
           "Capacity if all seats are standard-class: " + str(aircrafts[ac][2]) + "\n" +
           "Minimum number of first-class seats: " + str(aircrafts[ac][3]))
    print(information)
    
    # check number of first-class seats
    while True:
        try:
            fc_seats = int(input("Enter the number of first-class seats: "))
            break
        except ValueError:
            print("You must enter an integer.")

    # check for issues
    if fc_seats != 0:
        if fc_seats < aircrafts[ac][3]:
            print("Number of first-class seats must not be less than minimum number of first-class seats!")
            return None, None, None
        if fc_seats > (aircrafts[ac][2] / 2):
            print("Number of first-seats seats must not be greater than half the capacity if all seats are standard-class!")
            return None, None, None

    if fc_seats < 0:
        print("First-class seats cannot be negative.")
        return None, None, None
    
    # calculate number of standard-class seats on aircraft
    sc_seats = aircrafts[ac][2] - fc_seats * 2
    if sc_seats < 0:
         print("Too many first-class seats specified. Not enough remaining seat capacity.")
         return None, None, None
    
    print(f"Number of standard class seats: {sc_seats}")

    total_passengers = fc_seats + sc_seats
    print(f"Total passengers: {total_passengers}")
    return ac, fc_seats, sc_seats


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

    print("\n")
    # enter prices for standard class and first-class seats
    while True:
        try:
            sc_seat_price = float(input("Enter price for standard-class seat (£): "))
            break
        except ValueError:
            print("You must enter a number.")

    while True:
        try:
            fc_seat_price = float(input("Enter price for first-class seat (£): "))
            break
        except ValueError:
            print("You must enter a number.")

    # calculate variables
    flight_cost_per_seat = aircrafts[aircraft][0] * (dist_between / 100)
    flight_cost = flight_cost_per_seat * (first_class_seats + standard_class_seats)
    flight_income = first_class_seats * fc_seat_price + standard_class_seats * sc_seat_price
    flight_profit = flight_income - flight_cost

    # display information (to 2dp)
    information = ("Flight cost per seat: £" + str(round(flight_cost_per_seat, 2)) + "\n" +
           "Flight cost: £" + str(round(flight_cost, 2)) + "\n" +
           "Flight income: £" + str(round(flight_income, 2)) + "\n" +
           "Flight profit: £" + str(round(flight_profit, 2)))
    if round(flight_profit, 2) < 0:
        print("Warning: The proposed pricing plan results in a loss.")
    print(information)
    return

# start
menu()
