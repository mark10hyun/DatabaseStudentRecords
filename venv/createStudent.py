import sqlite3


class createStudent:

    @staticmethod
    def newS():
        #Connects to the Student Database
        conn = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn.cursor()
        userExit = 1
        #User can create as many students as they please
        while userExit == 1:
            inputID = int(input("Enter Student Id: "))
            inputFirstName = input("Enter Student First Name: ")
            inputFirstName = inputFirstName.lower()
            inputLastName = input("Enter Student Last Name: ")
            inputLastName = inputLastName.lower()
            inputGPA = float(input("Enter GPA: "))
            inputMajor = input("Enter Major: ")
            inputMajor = inputMajor.lower()
            inputFacAdvisor = input("Enter Faculty Advisor: ")
            inputFacAdvisor = inputFacAdvisor.lower()
            isDeleted = 1
            # Insert a new row of data, inline to table
            #delete set to 1 for soft delete
            c.execute("""
               INSERT INTO Student(StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor, deleted)
               VALUES (?, ?, ?, ?, ?, ?,?)""",
                      (inputID, inputFirstName, inputLastName, inputGPA, inputMajor, inputFacAdvisor, isDeleted))
            # save (commit) the changes
            conn.commit()
            StudentId = c.lastrowid
            print("Record created", StudentId)
            userExit = int(input("Do you want to add another student? Press 1 for yes OR 0 for no."))
        #Close data base
