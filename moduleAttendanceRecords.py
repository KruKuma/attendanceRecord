#   moduleAttendanceRecords.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    The Module Attendance Records programme will allow a lecturer do the following tasks for any
#                   module that they teach.


def loginScreen():
    name = input("Name: ")
    password = input("Password: ")

    userData = open('loginData.txt', 'r')
    userName, userPass = userData.readlines()

    print(userName + userPass)


#    if name == userName and password == userPass:
#        print("Welcome Anna")
#
#    else:
#        print("Module Record System - Login Failed")


def mainMenuScreen():
    print("Module Record System - Options")
    userOption = int(input("1. Record Attendance"
                           "\n2. Generate Statistics"
                           "\n3. Exit"
                           "\n>>"))


def genStatScreen():
    print("Module Record System(Statistics) - Choose a Module")
    userOption = int(input("1. SOFT_6017"
                           "2. COMP_1234"
                           ">>"))

    print("Module: "
          "\nNumber of students: "
          "\nNumber of Classes: "
          "\nAverage Attendance: "
          "\nLow Attender(s): "
          "\nNon Attender(s): "
          "\nBest Attender(s): ")


def recordAttendanceScreen():
    print("Module Record System(Attendance) - Choose a Module")
    userOption1 = int(input("1. SOFT_6017"
                            "2. COMP_1234"
                            ">>"))



def main():
    loginScreen()
    mainMenuScreen()
    genStatScreen()
    recordAttendanceScreen()


main()
