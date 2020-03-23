import sqlite3


class deleteStudent:

    @staticmethod
    def is_Deleted():
        #Connect to student db
        conn2 = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn2.cursor()
        userExit = 1
        #user can remove as many records as possible
        while userExit == 1:
            print("What Student would you like to remove/delete?\n")
            userInput = int(input("Enter Student ID "))
            userDelete = 0
            #soft delete
            #doesnt delete but sets delete variable to 0. So when user views all the records all of the tuples with a delete = 0 will not show but will still be present
            c.execute("UPDATE Student SET deleted = ? WHERE StudentId=?", (userDelete, userInput,))
            conn2.commit()
            print("Student has been deleted")
            userExit = int(input("Would you like to delete another student? Press 1 for CONTINUE...Press 0 to EXIT"))
        conn2.close()
