#   moduleAttendanceRecords.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    The Module Attendance Records programme will allow a lecturer do the following tasks for any
#                   module that they teach.

import numpy as np


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
    while True:
        name = input("Name: ")
        password = input("Password: ")

        userData = open('loginData.txt', 'r')
        data = userData.read().splitlines()

        userName, userPass = data[:2]

        if name == userName and password == userPass:
            print("Welcome Anna")
            break

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

    while True:
        userOption = checkForNum(f"1. {moduleCodeList[0]}"
                                 f"\n2. {moduleCodeList[1]}"
                                 "\n>>>")

        if userOption == 1:
            moduleCode = "SOFT_6017"
            break
        elif userOption == 2:
            moduleCode = "SOFT_6018"
            break
        else:
            print("Invalid input! Must be a number between 1 to 2")

    return moduleCode


def getClassAttendance(moduleCode):
    classData = open(f"{moduleCode}.txt", 'r')
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
    print(f"Module Record System(Attendance) - {moduleCode}")
    writeLine()
    print(f"There are {len(studentNameList)} students enrolled.")
    for i, student in enumerate(studentNameList):
        attendance = int(input(f"Student #{i + 1}: {studentNameList[i]}\n"
                               f"1. Present\n"
                               f"2. Absent\n"
                               f"3. Excused\n> "))
        if attendance == 1:
            presentList[i] += 1
        if attendance == 2:
            absentList[i] += 1
        if attendance == 3:
            excuseList[i] += 1

    updateClassDate(moduleCode, studentNameList, presentList, absentList, excuseList)


def updateClassDate(moduleCode, studentNameList, presentList, absentList, excuseList):
    classData = open(f"{moduleCode}.txt", "w")

    for x in range(len(studentNameList)):
        print(f"{studentNameList[x]},{presentList[x]},{absentList[x]},{excuseList[x]}", file=classData)

    print(f"{moduleCode}.txt updated with latest attendance records")

    classData.close()
    writeLine()


def genStatScreen(moduleCodeList):
    print("Module Record System(Statistics) - Choose a Module")
    writeLine()

    while True:
        userOption = checkForNum(f"1. {moduleCodeList[0]}"
                                 f"\n2. {moduleCodeList[1]}"
                                 "\n>>")
        if userOption == 1:
            moduleCode = "SOFT_6017"
            break
        elif userOption == 2:
            moduleCode = "SOFT_6018"
            break
        else:
            print("Invalid input! Must be a number between 1 to 2")

    return moduleCode


def generateAndSaveStats(moduleCode, studentNameList, presentList, absentList, excuseList):
    totalClasses = calTotalDays(presentList, absentList, excuseList)
    attendanceRateList = calAttendanceRate(presentList, absentList, excuseList)
    numStudent = len(studentNameList)
    avgAttendance = sum(presentList) / len(presentList)

    names = np.array(studentNameList)
    values = np.array(attendanceRateList)

    lowAttendanceRateName = names[np.where(values < 70)]
    nonAttenderName = names[np.where(values == 0)]
    bestAttenderName = names[np.where(values == max(values))[0]]

    print(f"Module: {moduleCode}"
          f"\nNumber of students: {numStudent}"
          f"\nNumber of Classes: {totalClasses}"
          f"\nAverage Attendance: {avgAttendance}")

    print("Low Attender(s):")
    for names in lowAttendanceRateName:
        print(f"\t\t{names}")

    print("None Attender(s):")
    for names in nonAttenderName:
        print(f"\t\t{names}")

    print("Best Attender(s):")
    for names in bestAttenderName:
        print(f"\t\t{names}")

    writeLine()


def calTotalDays(presentList, absentList, excuseList):
    totalDays = presentList[1] + absentList[1] + excuseList[1]

    return totalDays


def calAttendanceRate(presentList, absentList, excuseList):
    attendanceRateList = []
    for i in range(len(presentList)):
        rate = ((presentList[i] / (presentList[i] + absentList[i] + excuseList[i])) * 100)
        attendanceRateList.append(rate)

    return attendanceRateList


def main():
    loginScreen()
    moduleCodeList, moduleNameList = loadModules()

    while True:
        mainMenuChoice = mainMenuScreen()

        if mainMenuChoice == 1:
            moduleCode = recordAttendanceMainScreen(moduleCodeList)
            studentNameList, presentList, absentList, excuseList = getClassAttendance(moduleCode)
            takeClassAttendance(moduleCode, studentNameList, presentList, absentList, excuseList)

        if mainMenuChoice == 2:
            moduleCode = genStatScreen(moduleCodeList)
            studentNameList, presentList, absentList, excuseList = getClassAttendance(moduleCode)
            generateAndSaveStats(moduleCode, studentNameList, presentList, absentList, excuseList)


main()
