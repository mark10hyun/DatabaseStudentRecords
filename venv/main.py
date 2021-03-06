from createStudent import *
from displayRecords import *
from searchBy import *
from updateStudent import *
from deleteStudent import *
import sqlite3

# Mark Hyun
choice = 1
print("\n")
print("Hello, welcome to the School database system.")
# user can interact with this program as long as they please.
while choice == 1:
    print("Here are options that are accessible to you: \n")
    print("1) Retrieving all Student Records \n")
    print("2) Creating a new Student Record \n")
    print("3) Search by \n")
    print("4) Update Student Record \n")
    print("5) Delete Student Record \n")
    print("To EXIT? Enter 0 to EXIT | Enter 8 to CONTINUE \n")
    print("\n")
    userInput = int(input("What would you like to do? *input number of desired action* \n"))
    # displays all records
    if userInput == 1:
        displayRecords.printAll()
    # creates new student
    if userInput == 2:
        createStudent.newS()
    # Groups by
    if userInput == 3:
        searchBy.groupBy()
    # Update record
    if userInput == 4:
        updateStudent.updateRec()
    # Delete
    if userInput == 5:
        deleteStudent.is_Deleted()

    if userInput == 0:
        choice = 0
