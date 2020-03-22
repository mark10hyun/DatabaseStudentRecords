import sqlite3


class deleteStudent:

    @staticmethod
    def is_Deleted():
        conn2 = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn2.cursor()
        userExit = 1
        while userExit == 1:
            print("What Student would you like to remove/delete?\n")
            userInput = int(input("Enter Student ID "))
            userDelete = 0
            c.execute("UPDATE Student SET deleted = ? WHERE StudentId=?", (userDelete, userInput,))
            conn2.commit()
            print("Student has been deleted")
            userExit = int(input("Would you like to delete another student? Press 1 for CONTINUE...Press 0 to EXIT"))
        conn2.close()
