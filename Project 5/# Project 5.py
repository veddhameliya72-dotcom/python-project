Employee_list = []
Manager_list = []
Developer_list = []


class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.__salary = None

    def setter(self):
        self.name = input("\nName: ")
        self.age = int(input("Age: "))
        self.__salary = int(input("Salary: "))

    def display(self):
        print(f"\nName: {self.name} || Age: {self.age} || Salary: {self.__salary}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = None

    def setter(self):
        super().setter()
        self.department = input("Department: ")

    def display(self):
        print(
            f"\nName: {self.name} || Age: {self.age} || Salary: {self._Employee__salary} || Department: {self.department}")


class Developer(Employee):
    def __init__(self):
        super().__init__()
        self.field = None

    def setter(self):
        super().setter()
        self.field = input("Field Name: ")

    def display(self):
        print(f"\nName: {self.name} || Age: {self.age} || Salary: {self._Employee__salary} || Field: {self.field}")


while True:
    print("\nEmployee Management System")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    match choice:
        case "1":
            emp = Employee()
            emp.setter()
            Employee_list.append(emp)
            print("\nEmployee added successfully!")
            print("---------------------------------------------------------")

        case "2":
            man = Manager()
            man.setter()
            Manager_list.append(man)
            print("\nManager added successfully!")
            print("---------------------------------------------------------")

        case "3":
            dev = Developer()
            dev.setter()
            Developer_list.append(dev)
            print("\nDeveloper added successfully!")
            print("---------------------------------------------------------")

        case "4":
            while True:
                print("\nDisplay Menu")
                print("1. Display Employees")
                print("2. Display Managers")
                print("3. Display Developers")
                print("4. Back")

                display_choice = input("\nEnter your choice: ")

                match display_choice:
                    case "1":
                        print("\nEmployee Details:")
                        for emp in Employee_list:
                            emp.display()
                        print("-------------------------------------------")

                    case "2":
                        print("\nManager Details:")
                        for man in Manager_list:
                            man.display()
                        print("-" * 40)

                    case "3":
                        print("\nDeveloper Details:")
                        for dev in Developer_list:
                            dev.display()
                        print("------------------------------------------------------------" )

                    case "4":
                        break

                    case _:
                        print("Invalid choice! Please try again.")

        case "5":
            print("\nExiting the program...")
            print("----------------------------------------------------------------------------------------"  )
            print("----------------------------------------------------------------------------------------"  )
            break

        case _:
            print("\nInvalid choice! Please try again.")
            print("------------------------------------------------------------------------------")

'''

output:
Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 1

Name: ved
Age: 12
Salary: 21345

Employee added successfully!
---------------------------------------------------------

Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 2

Name: abc
Age: 43
Salary: 213
Department: xyz

Manager added successfully!
---------------------------------------------------------

Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 3

Name: uvw
Age: 32
Salary: 53242
Field Name: backend developer

Developer added successfully!
---------------------------------------------------------

Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 4

Display Menu
1. Display Employees
2. Display Managers
3. Display Developers
4. Back

Enter your choice: 1

Employee Details:

Name: ved || Age: 12 || Salary: 21345
-------------------------------------------


Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 4

Display Menu
1. Display Employees
2. Display Managers
3. Display Developers
4. Back

Enter your choice: 2

Manager Details:

Name: abc || Age: 43 || Salary: 213 || Department: xyz

----------------------------------------

Display Menu
1. Display Employees
2. Display Managers
3. Display Developers
4. Back


Enter your choice: 3

Display Menu
1. Display Employees
2. Display Managers
3. Display Developers
4. Back

Developer Details:

Name: uvw || Age: 32 || Salary: 53242 || Field: backend developer
------------------------------------------------------------

Display Menu
1. Display Employees
2. Display Managers
3. Display Developers
4. Back

Enter your choice: 4

Employee Management System
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice: 5

Exiting the program...
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

'''                        