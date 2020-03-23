import sqlite3


class searchBy:
    @staticmethod
    def groupBy():
        conn2 = sqlite3.connect('StudentDB.sqlite')
        # cursor is something that performs an action
        c = conn2.cursor()
        userExit = 1
        while userExit == 1:
            print("What would you like to group by?\n")
            print("1) Group by Major \n")
            print("2) Group by Faculty Advisor \n")
            print("3) Group by GPA \n")
            print("\n")
            userInput = int(input("Please input your desired action: "))
            # Groups by major
            if userInput == 1:
                userMaj = input("Input Major: ")
                userMaj = userMaj.lower()
                c.execute("SELECT * FROM Student WHERE Major = ? AND deleted = 1", (userMaj,))
                items = c.fetchall()
                for item in items:
                    print(item[:5])
            # Groups by Faculty Advisor
            if userInput == 2:
                userFA = input("Input Faculty Advisor: ")
                userFA = userFA.lower()
                c.execute("SELECT * FROM Student WHERE FacultyAdvisor = ? AND deleted =1 ", (userFA,))
                items = c.fetchall()
                for item in items:
                    print(item[:5])
            # Groups by GPA
            if userInput == 3:
                userG = float(input("Input GPA"))
                c.execute("SELECT * FROM Student WHERE GPA = ? AND deleted = 1 ", (userG,))
                items = c.fetchall()
                for item in items:
                    print(item[:5])
            else:
                print("There are no Records with your desired grouping")
            print("----------------------------------------------------------- \n")
            userExit = int(input("Do you want to group by something else? Press 1 for yes OR 0 for no. \n"))
        conn2.commit()
        conn2.close()
