"""
AQA GCSE Computer Science – Programming Project NEA  
Airport Task – Incomplete Solution

Author: TT
School: PS
Date Created: 09/07/2025  
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
distance_from_ljla = [] # ljl = Liverpool John Lennon Airport
distance_from_bia = [] # bia = Bournemouth International Airport

# flight details
# also i'll make this a 2d list probably
aircrafts = ["medium narrow body",
             "large narrow body",
             "medium wide body"
             ]
running_cost = [8, 7, 5]
maximum_flight_range = [2650, 5600, 4050]
capacity_for_standard = [180, 220, 406]
minimum_first_class = [8, 10, 14]

# initalise variables
code_uk = None
code_abroad = None

aircraft = None


# get the details from the csv
with open('Airports.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        airport_codes.append(row[0])
        airport_names.append(row[1])
        distance_from_ljla.append(int(row[2]))
        distance_from_bia.append(int(row[3]))

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
            t = airport_details()
        elif option in ("enter flight details", "2"):
            t = flight_details()
        elif option in ("enter price plan and calculate profit", "3"):
            t = calculate_profit_pp()
        elif option in ("clear data", "4"):
            code_uk = None
            code_abroad = None
            print("Data has been cleared!")
        else:
            print("That is not a valid option!")

# enter airport details
def airport_details():
    code_uk = input("Enter the three-letter airport code (UK): ").upper().strip()
    if code_uk not in ("LPL", "BOH"):
        print("That is not a valid three-letter code.")
        code_uk = None
        return

    code_abroad = input("Enter the three-letter airport code (ABROAD): ").upper().strip()
    for p in airport_codes:
        if code_abroad == p:
            idx = airport_codes.index(p)
            print(airport_names[idx])
            return

    print("A airport could not be found with this code.")
    code_uk = None
    return

# enter flight details
def flight_details():
    aircraft = input("Enter the type of aircraft that will be used: ").lower().strip()
    if aircraft not in aircrafts:
        print("That is not a valid type of aircraft.")
        aircraft = None
        return
    idx = aircraft.index(aircrafts)
    #air_details = str(running_cost[idx]) + "km" + "yadadada" ) # didn't have time to continue, here's where the updates will start
    
    pass

# enter price plan (pp) and calculate profit
def calculate_profit_pp():
    pass

# start
menu()
