while True:
    print("😊.Hello namaste welcome to our Pattern Generator and Number Analyzer.😊")
    print("👇select an option:👇")
    print("1. Pattern Generator.")
    print("2. Number Analyzer.")
    print("3. For Exit the program.")

    print()
    choice = int(input("Enter your choice:"))
    print()
    print()
    match choice:
            case 1:
                row = int(input("Enter number of rows for pattern:"))
                if row >= 0:
                    for i in range(1,row+1):
                        for j in range(1,i+1):
                            print("*",end=" ")
                        print()
                else:
                    print("please enter a positive number.")  
                    
                    row = int(input("Enter number of rows for pattern:"))
                    
                    for i in range(1,row+1):
                        for j in range(1,i+1):
                            print("*",end=" ")
                    print()
                    print()
            case 2:
                print("Enter a range to anlyze the numbers in that range:")
                start = int(input("Enter starting number of the range:"))
                end = int(input("Enter ending number of the range:"))
                print()
                if end > start:
                    sum = 0
                    evensum = 0
                    oddsum = 0
                    for i in range(start, end+1):
                        if i % 2 == 0:
                            print(i," is an even number. ")
                            evensum = evensum + i
                            sum = sum + i
                        else:
                            print(i," is a an odd number. ")
                            oddsum = oddsum + i
                            sum = sum + i
                    print("The sum of even numbers in the range is:",evensum)
                    print("The sum of odd numbers in the range is:",oddsum) 
                    print("The sum of all numbers is: ",sum)
                    print()
                    print()
                else:
                    print("👉Pleaze enter a progressive range ie; 1-10")
                    print()
                    print()
                    continue

            case 3:
                print("Thank you for using our program>>😊")
                print()
                print()
                break
            case _:
                print("Invalid choice. Please select a valid option.")
                print()
                print()

'''

output:
😊.Hello namaste welcome to our Pattern Generator and Number Analyzer.😊
👇select an option:👇
1. Pattern Generator.
2. Number Analyzer.
3. For Exit the program.

Enter your choice:2


Enter a range to anlyze the numbers in that range:
Enter starting number of the range:1
Enter ending number of the range:10
1  is a an odd number. 
2  is an even number. 
3  is a an odd number. 
4  is an even number. 
5  is a an odd number. 
6  is an even number. 
7  is a an odd number. 
8  is an even number. 
9  is a an odd number. 
10  is an even number. 
The sum of even numbers in the range is: 30
The sum of odd numbers in the range is: 25
The sum of all numbers is:  55

😊.Hello namaste welcome to our Pattern Generator and Number Analyzer.😊
👇select an option:👇
1. Pattern Generator.
2. Number Analyzer.
3. For Exit the program.

Enter your choice:1


Enter number of rows for pattern:5
* 
* * 
* * * 
* * * * 
* * * * * 


😊.Hello namaste welcome to our Pattern Generator and Number Analyzer.😊
👇select an option:👇
1. Pattern Generator.
2. Number Analyzer.
3. For Exit the program.

Enter your choice:2


Enter a range to anlyze the numbers in that range:
Enter starting number of the range:10
Enter ending number of the range:1

👉Pleaze enter a progressive range ie; 1-10


😊.Hello namaste welcome to our Pattern Generator and Number Analyzer.😊
👇select an option:👇
1. Pattern Generator.
2. Number Analyzer.
3. For Exit the program.

Enter your choice:3


Thank you for using our program>>😊
'''