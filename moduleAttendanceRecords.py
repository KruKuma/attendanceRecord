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

    print(moduleCodeList)
    print(moduleNameList)

    return moduleCodeList, moduleNameList


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

    if userOption == 1:
        option = 1
    if userOption == 2:
        option = 2
    if userOption == 3:
        exit()

    return option


def recordAttendanceMainScreen(moduleCodeList):
    print("Module Record System(Attendance) - Choose a Module")
    writeLine()

    numModule = len(moduleCodeList)
    optionStr = ""

    for i, option in enumerate(moduleCodeList):
        optionStr += f"{i + 1}. {option}\n"

    while True:
        userOption = checkForNum(optionStr)
        if 0 < userOption <= numModule:
            break
        else:
            print("Invalid input! Must be a number between 1 to 2")


def getClassAttendance(moduleCode):
    classData = open(moduleCode, 'r')
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
        presentList.append(int(lineData[1]))
        absentList.append(int(lineData[2]))
        excuseList.append(int(lineData[3]))

    classData.close()

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


def genStatScreen():
    print("Module Record System(Statistics) - Choose a Module")
    writeLine()

    while True:
        userOption = checkForNum("1. SOFT_6017"
                                 "\n2. COMP_1234"
                                 "\n>>")
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


def main():
    loginScreen()
    modeCodeList, moduleNameList = loadModules()
    mainMenuChoice = mainMenuScreen()

    if mainMenuChoice == 1:
        moduleCode = recordAttendanceMainScreen(modeCodeList)
        takeClassAttendance(moduleCode, studentNameList, presentList, absentList, excuseList)

    if mainMenuChoice == 2:
        genStatScreen()


#   main()
#   studentNameList, presentList, absentList, excuseList = getClassAttendance("SOFT_6017.txt")
#   takeClassAttendance("test", studentNameList, presentList, absentList, excuseList)


modeCodeList, moduleNameList = loadModules()
moduleCode = recordAttendanceMainScreen(modeCodeList)
