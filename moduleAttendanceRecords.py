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


def loadModules():
    moduleInfo = open('modules.txt', 'r')
    moduleCodeList = []
    moduleNameList = []

    while True:
        line = moduleInfo.readline().strip()
        if line == "":
            break
        lineData = line.split(', ')
        moduleCodeList.append(lineData[0])
        moduleNameList.append(lineData[1])

    moduleInfo.close()

#    print(moduleCodeList)
#    print(moduleNameList)

    return moduleCodeList, moduleNameList


def getClassAttendance(moduldeCode):
    classData = open(moduldeCode, 'r')
    studentNameList = []
    presentList = []
    absentList = []
    excuseList = []

    while True:
        line = classData.readline().strip()
        if line == "":
            break
        lineData = line.split(',')
        studentNameList.append(lineData[0])
        presentList.append(lineData[1])
        absentList.append(lineData[2])
        excuseList.append(lineData[3])

    classData.close()

#    print(studentNameList)
#    print(presentList)
#    print(absentList)
#    print(excuseList)

    return studentNameList, presentList, absentList, excuseList


def takeClassAttendance(moduleCode, studentNameList, presentList, absentList, excuseList):
    print("Module Record System(Attendance) - Choose a Module")
    writeLine()
    option = checkForNum("1. SOFT_6017"
                         "\n2. COMP_1234")


def updateClassDate(moduleCode, studentNameList, presentList, absentList, excuseList):
    classData = open("testModule.txt", "w")
    for x in range(0, 3):
        print(f"{studentNameList[x]},{presentList[x]},{absentList[x]},{excuseList[x]}", file=classData)

    classData.close()


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
            print("Invalid input! Must be a number between 1 to 3")


def genStatScreen():
    print("Module Record System(Statistics) - Choose a Module")
    writeLine()

    while True:
        userOption = checkForNum("1. SOFT_6017"
                                 "2. COMP_1234"
                                 ">>")
        if 0 < userOption <= 2:
            break
        else:
            print("Invalid input! Must be a number between 1 to 2")

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

    while True:
        userOption1 = checkForNum("1. SOFT_6017"
                                  "2. COMP_1234"
                                  ">>")
        if 0 < userOption1 <= 2:
            break
        else:
            print("Invalid input! Must be a number between 1 to 2")


def main():
    loginScreen()
    mainMenuScreen()
    genStatScreen()
    recordAttendanceScreen()


#   studentNameList, presentList, absentList, excuseList = getClassAttendance("SOFT_6017.txt")
#   takeClassAttendance("test", studentNameList, presentList, absentList, excuseList)