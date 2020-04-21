#   moduleAttendanceRecords.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    The Module Attendance Records programme will allow a lecturer do the following tasks for any
#                   module that they teach.


def writeLine():
    print("-" * 35)


def checkForNum(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Must be numeric...")
    return number


def loginScreen():
    name = input("Name: ")
    password = input("Password: ")

    userData = open('loginData.txt', 'r')
    data = userData.read().splitlines()

    userName, userPass = data[:2]

    if name == userName and password == userPass:
        print("Welcome Anna")

    else:
        print("Module Record System - Login Failed")


def mainMenuScreen():
    print("Module Record System - Options")
    writeLine()
    while True:
        userOption = checkForNum("1. Record Attendance"
                                 "\n2. Generate Statistics"
                                 "\n3. Exit"
                                 "\n>>")
        if 0 < userOption <= 3:
            break
        else:
            print("Invalid input")


def genStatScreen():
    print("Module Record System(Statistics) - Choose a Module")
    writeLine()
    userOption = checkForNum("1. SOFT_6017"
                             "2. COMP_1234"
                             ">>")

    print("Module: "
          "\nNumber of students: "
          "\nNumber of Classes: "
          "\nAverage Attendance: "
          "\nLow Attender(s): "
          "\nNon Attender(s): "
          "\nBest Attender(s): ")


def recordAttendanceScreen():
    print("Module Record System(Attendance) - Choose a Module")
    writeLine()
    userOption1 = checkForNum("1. SOFT_6017"
                              "2. COMP_1234"
                              ">>")


def main():
    loginScreen()
    mainMenuScreen()
    genStatScreen()
    recordAttendanceScreen()


main()
