# Moduler and Packager...........
from pdb import run

from Modules import date_time, dir_modul, file_op, maths, random_num, uuid_gene

print("=" * 40)
print("Welcome To Multi-Utility Toolkit")
print("=" * 40)
def main():
  while True:

    print("Choose An Option:")
    print("1. Date-Time And Time Operation")
    print("2. Mathemetical Operation")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custome Module)")
    print("6. Explore Module Atrribute dir()")
    print("7. Exit")
    print("=" * 40)
    choice = int(input("Enter Your Choice: "))

    match choice:
      case 1: 
        while True:
          print("\nDate-Time And Time Operation")
          print("1. Display Current Date And Time")
          print("2. Calculate Difference Between Two Dates/Time")
          print("3. Formate Date Into Custome Format")
          print("4. Stopwatch")
          print("5. Countdown Timer")
          print("5. Back To Main Menu\n")
          sub_choice_1 = int(input("Enter Your Choice: "))
          print()

          match sub_choice_1:
            case 1:
              date_time.current_time()
              print()
            case 2: 
              date_time.date_difference()
            case 3: 
              date_time.formate_date()
            case 4: 
              date_time.stop_watch()
            case 5: 
              date_time.count_down()
            case 5:
              print("EXITING DATE TIME AND TIME OPERATION MENU.....") 
              break
            case _: 
              print("Invalid Choice Entered 🚫")

      case 2:
        while True:
          print("\nMathemetical Operations:")
          print("1. Calculate Factorial")
          print("2. Solve Compound Interest")
          print("3. Trigonometric Calculation")
          print("4. Aria Of GEomatric Shape")
          print("5. Back To Main Menu\n")
          sub_choice_2 = int(input("Enter Your Choice: "))
          print()

          match sub_choice_2:
            case 1: 
              mathemetic.cal_factorial()
            case 2: 
              mathemetic.compound_interest()
            case 3: 
              mathemetic.Trigonometri()
            case 4: 
              mathemetic.calculate_area()
            case 5:
              print("EXITING MATHEMATICAL OPERATIONS MENU.....")
              break
            case _:
              print("Invalid Choice Entered")

      case 3: 
        while True:
          print("\nRandom Data Generations:")
          print("1. Generate Random Number")
          print("2. Generate Randome List")
          print("3. Create Random Password")
          print("4. Generate Randome OTP")
          print("5. Back To Main Menu\n")
          sub_choice_3 = int(input("Enter Your Choice: "))
          print()

          match sub_choice_3:
            case 1: 
              random_num.random_num()
            case 2: 
              random_num.random_list()
            case 3: 
              random_num.generate_password()
            case 4: 
              random_num.generate_otp()
            case 5: 
              print("EXITING RANDOM DATA GENERATION MENU.....")
              break
            case _:
              print("Invalid Choice Entered!!")

      case 4:
        uuid_gene.generate_uuid()
      case 5: 
        while True:
          print("\nFile Operations:")
          print("1. Create A New File")
          print("2. Write To A File")
          print("3. Read From A File")
          print("4. Append To A File")
          print("5. Back To Main Menu\n")
          sub_choice_4 = int(input("Enter Your Choice: "))
          print()

          match sub_choice_4:
            case 1: 
              file_op.create_file()
            case 2: 
              file_op.write_file()
            case 3: 
              file_op.read_file()
            case 4: 
              file_op.append_file()
            case 5:
              print("EXITING FILE OPERATIONS MENU.....")
              break
            case _: 
              print("Invalid Choice Entered!!")

      case 6: 
        dir_modul.module_attributes()
      case 7:
        print("Thanks for using this program 😊") 
        print("YOu can give 10 marks if are satisfied with this program 😁")   
        break
      case _:
        print("Invalid Choice Entered!!!")

if __name__ == "__main__":
  main()
                               
'''
output:

ample run output · TXT
========================================
Welcome To Multi-Utility Toolkit
========================================
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: 
Date-Time And Time Operation
1. Display Current Date And Time
2. Calculate Difference Between Two Dates/Time
3. Formate Date Into Custome Format
4. Stopwatch
5. Countdown Timer
6. Back To Main Menu
 
Enter Your Choice: 
Current Date = 04/07/2026
Current Time = 11:21:52
 
 
Date-Time And Time Operation
1. Display Current Date And Time
2. Calculate Difference Between Two Dates/Time
3. Formate Date Into Custome Format
4. Stopwatch
5. Countdown Timer
6. Back To Main Menu
 
Enter Your Choice: 
Enter The First Date (DD/MM/YYYY): Enter The Second Date (DD/MM/YYYY): Difference is: 549
 
Date-Time And Time Operation
1. Display Current Date And Time
2. Calculate Difference Between Two Dates/Time
3. Formate Date Into Custome Format
4. Stopwatch
5. Countdown Timer
6. Back To Main Menu
 
Enter Your Choice: 
 
choose the Fomrat's: 
1. YYYY/MM/DD 
2. DD/MM/YYYY
3. Exit
 
Enter Your Choice: 
choosen format: 2026/07/04
 
choose the Fomrat's: 
1. YYYY/MM/DD 
2. DD/MM/YYYY
3. Exit
 
Enter Your Choice: 
you are exiting from the format date module...........
 
Date-Time And Time Operation
1. Display Current Date And Time
2. Calculate Difference Between Two Dates/Time
3. Formate Date Into Custome Format
4. Stopwatch
5. Countdown Timer
6. Back To Main Menu
 
Enter Your Choice: 
EXITING DATE TIME AND TIME OPERATION MENU.....
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: 
Mathemetical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculation
4. Aria Of GEomatric Shape
5. Back To Main Menu
 
Enter Your Choice: 
Enter Number For Factorial: Factorial Of '5' is: 120
 
Mathemetical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculation
4. Aria Of GEomatric Shape
5. Back To Main Menu
 
Enter Your Choice: 
Enter The Principal Amount: Enter The Annual Interest Rate: Enter The Time The Money Is Invested For (In Years): Enter The Number Of Times Interest Is Compounded Per Year: 
The Total Amount After 2.0 Years Is: 1102.5
The Total Interest Earned Is: 102.5
 
Mathemetical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculation
4. Aria Of GEomatric Shape
5. Back To Main Menu
 
Enter Your Choice: 
Enter The Degree: Sine of 30°: 0.49999999999999994
Cosine of 30°: 0.8660254037844387
Tangent of 30°: 0.5773502691896257
 
Mathemetical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculation
4. Aria Of GEomatric Shape
5. Back To Main Menu
 
Enter Your Choice: 
Enter shape (rectangle, triangle): Enter length: Enter width: The area of the rectangle is: 50.0
 
Mathemetical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculation
4. Aria Of GEomatric Shape
5. Back To Main Menu
 
Enter Your Choice: 
EXITING MATHEMATICAL OPERATIONS MENU.....
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: 
Random Data Generations:
1. Generate Random Number
2. Generate Randome List
3. Create Random Password
4. Generate Randome OTP
5. Back To Main Menu
 
Enter Your Choice: 
Enter Starting Range: Enter Ending Range: Random Integer is: 41
 
Random Data Generations:
1. Generate Random Number
2. Generate Randome List
3. Create Random Password
4. Generate Randome OTP
5. Back To Main Menu
 
Enter Your Choice: 
Total numbers You Want In Your List? Enter Starting Range: Enter End Range: Generated List: [49, 21, 3, 11, 34]
 
Random Data Generations:
1. Generate Random Number
2. Generate Randome List
3. Create Random Password
4. Generate Randome OTP
5. Back To Main Menu
 
Enter Your Choice: 
Enter password length: Your random password is: mDYHS65ybN
 
Random Data Generations:
1. Generate Random Number
2. Generate Randome List
3. Create Random Password
4. Generate Randome OTP
5. Back To Main Menu
 
Enter Your Choice: 
Your Generated OTP is: 517728
 
Random Data Generations:
1. Generate Random Number
2. Generate Randome List
3. Create Random Password
4. Generate Randome OTP
5. Back To Main Menu
 
Enter Your Choice: 
EXITING RANDOM DATA GENERATION MENU.....
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: Generated UUID is: 4a922965-67cc-47e6-a13e-bac2c10c1b3f
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: 
File Operations:
1. Create A New File
2. Write To A File
3. Read From A File
4. Append To A File
5. Back To Main Menu
 
Enter Your Choice: 
Enter Filename to be created: File sample.txt Created Successfully...............
 
File Operations:
1. Create A New File
2. Write To A File
3. Read From A File
4. Append To A File
5. Back To Main Menu
 
Enter Your Choice: 
Enter Filename: Enter Content To Write: Content is been uploaded successfully...............
 
File Operations:
1. Create A New File
2. Write To A File
3. Read From A File
4. Append To A File
5. Back To Main Menu
 
Enter Your Choice: 
Enter Filename To Read: Hello from the toolkit demo
 
File Operations:
1. Create A New File
2. Write To A File
3. Read From A File
4. Append To A File
5. Back To Main Menu
 
Enter Your Choice: 
Enter Filename: Enter Content To Append: Content Appended Successfully.................................
 
File Operations:
1. Create A New File
2. Write To A File
3. Read From A File
4. Append To A File
5. Back To Main Menu
 
Enter Your Choice: 
EXITING FILE OPERATIONS MENU.....
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: 
--- Available Module Attributes ---
 
Functions In 'date_time':
 - count_down
 - current_time
 - date_difference
 - datetime
 - formate_date
 - stop_watch
 - time
 
Functions In 'mathemetic':
 - Trigonometri
 - cal_factorial
 - calculate_area
 - compound_interest
 - math
 
Functions In 'random_num':
 - generate_otp
 - generate_password
 - random
 - random_list
 - random_num
 
Functions In 'file_op':
 - append_file
 - create_file
 - read_file
 - write_file
 
Functions In 'uuid':
 - generate_uuid
 - uuid
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: Thanks for using this program 😊
You can give 10 marks if are satisfied with this program 😁
'''
