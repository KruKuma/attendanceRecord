#   moduleAttendanceRecords.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    The Module Attendance Records programme will allow a lecturer do the following tasks for any
#                   module that they teach.

import numpy as np  # Added numpy to improve array


def writeLine():
    """
    Function for printing out lines
    :return:
    """
    print("-" * 35)


def checkForNum(prompt):
    """
    Using a value as a prompt from one of the option to verified if its an int or not
    :parameter prompt (int)
    :returns (int)
    """
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Must be numeric...")

    return number


def loginScreen():
    """
    Print out the login screen for the user to input name and password to verified if the name or password
    is in the database or not
    """
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
    """
    This function will read the modules.txt file, it will turn the contents of the file into a list and then return
    the list to be use in other function
    :return: (String)
    """
    moduleInfo = open('modules.txt', 'r')
    moduleCodeList = []
    moduleNameList = []

    # Use while loop to make the list of module code and name
    while True:
        line = moduleInfo.readline().strip()
        if line == "":
            break       # Stop the loop if there's no other line in the file
        lineData = line.split(', ')
        moduleCodeList.append(lineData[0])
        moduleNameList.append(lineData[1])

    moduleInfo.close()

    #    print(moduleCodeList)
    #    print(moduleNameList)

    return moduleCodeList, moduleNameList


def mainMenuScreen():
    """
    This function will display the main menu screen for the use to choose an option then return that option
    :return: (String)
    """
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
        userOption = 1
    if userOption == 2:
        userOption = 2
    if userOption == 3:
        exit()

    return userOption


def recordAttendanceMainScreen(moduleCodeList):
    """
    Take in the mode code list and display it as an option for the user to pick from then will return the code of the
    module to be use later.
    :parameter moduleCodeList(String)
    :return: (String)
    """
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
    """
    Will take in the module code and use the code to open the file of the specified module and read it to created
    the list of names, presents, absents and excuses. To be return for future use
    :param moduleCode:
    :return: (list)
    """
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
    """
    Use the module code to be print out in the top of the menu and use the list generated before to take attendance
    for the class then send the list to be update.
    :param moduleCode:
    :param studentNameList:
    :param presentList:
    :param absentList:
    :param excuseList:
    """
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
    """
    Take in the updated list to be writen into the module file to updated it. The function opens the file and updated
    it accordingly.
    :param moduleCode:
    :param studentNameList:
    :param presentList:
    :param absentList:
    :param excuseList:
    """
    classData = open(f"{moduleCode}.txt", "w")

    for x in range(len(studentNameList)):
        print(f"{studentNameList[x]},{presentList[x]},{absentList[x]},{excuseList[x]}", file=classData)

    print(f"{moduleCode}.txt updated with latest attendance records")

    classData.close()
    writeLine()


def genStatScreen(moduleCodeList):
    """
    Use the module code list to display the option for the user to pick from then returns the module code in string
    to be used in the other function.
    :param moduleCodeList:
    :return: (String)
    """
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
    """
    Use the module code to be display and use the other to calculate different number then display it in other output
    :param moduleCode:
    :param studentNameList:
    :param presentList:
    :param absentList:
    :param excuseList:
    :return:
    """
    totalClasses = calTotalDays(presentList, absentList, excuseList)
    attendanceRateList = calAttendanceRate(presentList, absentList, excuseList)
    numStudent = len(studentNameList)
    avgAttendance = sum(presentList) / len(presentList)

    names = np.array(studentNameList)       # Declare a numpy list for names from the list of student name
    values = np.array(attendanceRateList)   # Declare a numpy list for values from the attendances rate

    # Use numpy to get a list of student names that have less then 70% attendances rate
    lowAttendanceRateName = names[np.where(values < 70)]

    # Use numpy to get a list of student names that have less then 0 attendances rate
    nonAttenderName = names[np.where(values == 0)]

    # Use numpy to get a list of student name that have the best attendances rate
    bestAttenderName = names[np.where(values == max(values))[0]]

    print(f"Module: {moduleCode}"
          f"\nNumber of students: {numStudent}"
          f"\nNumber of Classes: {totalClasses}"
          f"\nAverage Attendance: {avgAttendance}")

    print("Low Attender(s):")
    for names in lowAttendanceRateName:     # Use a for loop to print out the name of low attendance rate students
        print(f"\t\t{names}")

    print("None Attender(s):")
    for names in nonAttenderName:           # Use a for loop to print out the name of students that don't attend
        print(f"\t\t{names}")

    print("Best Attender(s):")
    for names in bestAttenderName:          # Use a for loop to print out the name of students with best attendance
        print(f"\t\t{names}")

    writeLine()


def calTotalDays(presentList, absentList, excuseList):
    """
    Use present, absent and excuse list to calculate the total amount of days since the class began
    :param presentList:
    :param absentList:
    :param excuseList:
    :return: (int)
    """
    totalDays = presentList[1] + absentList[1] + excuseList[1]

    return totalDays


def calAttendanceRate(presentList, absentList, excuseList):
    """
    Use present, absent and excuse list to calculate the attendances rate of each student and return the list of it
    :param presentList:
    :param absentList:
    :param excuseList:
    :return: (list)
    """
    attendanceRateList = []

    # Use a for loop to get the attendance rate for each student and put it into a list
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
