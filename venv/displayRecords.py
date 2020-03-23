import sqlite3


class displayRecords:

    @staticmethod
    def printAll():
        conn2 = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn2.cursor()
        userExit = 1
        while userExit == 1:
            print("-------------------All Student Records--------------------- \n")
            c.execute("SELECT * FROM Student WHERE deleted = 1")
            # Fetches all items that are not deleted.
            items = c.fetchall()
            for item in items:
                # prints everything but the deleted variable
                print(item[:5])
            conn2.commit()
            print("----------------------------------------------------------- \n")
            userExit = int(input("Do you want to update another student? Press 1 for yes OR 0 for no. \n"))
        conn2.close()
