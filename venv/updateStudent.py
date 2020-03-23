import sqlite3


class updateStudent:

    @staticmethod
    def updateRec():
        conn2 = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn2.cursor()
        userExit = 1
        while userExit == 1:
            inputID = int(input("Enter Student Id that you want to update: "))
            userInput = input("What would you like to up date? Major or Advisor? ")
            if userInput == "major":
                majorUpdate = input("Enter new Major: ")
                c.execute("UPDATE Student SET Major = ? WHERE StudentId=? AND deleted = 1", (majorUpdate, inputID,))
                conn2.commit()

            if userInput == "advisor":
                advisorUpdate = input("Enter new advisor: ")
                c.execute("UPDATE Student SET Major = ? WHERE StudentId=? AND deleted = 1", (advisorUpdate, inputID,))
                conn2.commit()
            print("Updated")
            userExit = int(input("Do you want to update another student? Press 1 for yes OR 0 for no."))

        conn2.close()
