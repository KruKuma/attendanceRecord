#   moduleAttendanceRecords.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    The Module Attendance Records programme will allow a lecturer do the following tasks for any
#                   module that they teach.


def loginScreen():
    name = input("Name: ")
    password = input("Password: ")

    count = 0
    userData = open('loginData.txt', 'r')
    userInfo = userData.readlines()

    userName = userInfo.strip()

    print(userName)




def main():
    loginScreen()

main()