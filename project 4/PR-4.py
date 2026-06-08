# PR-4

# case 1:
data = []



# case 2:
# for finding the maximum among the list.
def maximum():
    return max(data)

# for finding the minimum among the list.
def minimum():
    return min(data) 

# for finding the sum of all values in the list.
def summ():
    return sum(data)

# for finding the length of the list.
def length():
    return len(data)

# for finding the average of the list.
def avg():
    return sum(data)/len(data)



# for sorting the list in ascending order.
def ascending_order():
    data.sort()
    print(f"Sorted in ascending order: {sorted(data)}") 

# for sorting the list in descending order.
def descending_order():
    data.sort(reverse=True)
    print(f"Sorted in descending order: {sorted(data,reverse=True)}")           


# case 3:
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial (n-1)


print("🎊!Welcome to the data analyser and transformer program!🎊\n")

while True:

    print("\n1. Input Data.")
    print("2. display data Summary.")
    print("3. Calculate Factorial.")
    print("4. Filter Data by Threshold.")
    print("5. sort data.")
    print("6. Display Dataset Statistics.")
    print("7. Exit program.\n")

    choice = int(input("Enter your choice:"))

    match choice:
        case 1: 
            num_elements = int(input("\nEnter a total number off Elements: "))
            for i in range(num_elements):
                element = int(input(f"Enter element {i+1}: "))
                data.append(element)
            print("Data input successful!")
            print("-----------------------------------------------\n")    

        case 2:
            if not list:
                print("\nNo Data found. Please input data first.")
            else:
                print(f"Lenght of an array: ",length())
                print(f"Minimum Value: ",minimum())
                print(f"Maximum Value: ",maximum())
                print(f"Sum of all Value: ",summ())
                print(f"Average of al Value: ",avg())
                print("Displayed Data summary successfully!")
                print("-----------------------------------------------\n")                

        case 3:
            number = int(input("\nEnter a number to calculate its factorial:"))
            print("Factorial of", number, "is", factorial(number))
            print("-----------------------------------------------\n")

        case 4:
            threshold = int(input("Enter the threshold value: "))
            threshold2 = int(input("Enter the ending threshold value: (optional): "))
            print("values between threshold and thershold2:  ")
            f = []
            for i in data:
                if threshold <= i <= threshold2:
                    f.append(i)
            print(f"values between {threshold} and {threshold2}: {f}")
            print("-----------------------------------------------\n")

        case 5:
            if len(data) == 0:
                print("No data to sort. Please input data first.")
            else:
                print("1. ascending order.")
                print("2. descending order.")
                sort_choice = int(input("Enter your choice: "))
                match sort_choice:
                    case 1:
                        ascending_order()
                    case 2:
                        descending_order()
                    case _:
                        print("\nInvalid choice. Please try again.")
                        print("Data sorted successfully!") 
                print("-----------------------------------------------\n")          
        case 6:
            if len(data) == 0:
                print("No data to display statics for. please enter the data first.\n")
                print("-----------------------------------------------\n")
            else:
                print("Data Statistics: ")
                print(f"Minimum Value: ",minimum())
                print(f"Maximum Value: ",maximum())
                print(f"Sum of all Value: ",summ())
                print(f"Average of al Value: ",avg())
            print("Dispayed Data statistics successfully!")
            print("-----------------------------------------------\n")                
        case 7:
            print("Exiting the program. Goodbye!")
            print("-----------------------------------------------\n")
            break
        case _:
            print("Invalid choice. Please try again.")   
            print("-----------------------------------------------\n")                          
    

'''

output:
🎊!Welcome to the data analyser and transformer program!🎊


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:1

Enter a total number off Elements: 4
Enter element 1: 1
Enter element 2: 3
Enter element 3: 2
Enter element 4: 4
Data input successful!
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:2
Lenght of an array:  4
Minimum Value:  1
Maximum Value:  4
Sum of all Value:  10
Average of al Value:  2.5
Displayed Data summary successfully!
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:3

Enter a number to calculate its factorial:5
Factorial of 5 is 120
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:4
Enter the threshold value: 1
Enter the ending threshold value: (optional): 3
values between threshold and thershold2:  
values between 1 and 3: [1, 3, 2]
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:5
1. ascending order.
2. descending order.
Enter your choice: 1
Sorted in ascending order: [1, 2, 3, 4]
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:5
1. ascending order.
2. descending order.
Enter your choice: 2
Sorted in descending order: [4, 3, 2, 1]
-----------------------------------------------


1. Input Data.
2. display data Summary.
3. Calculate Factorial.
4. Filter Data by Threshold.
5. sort data.
6. Display Dataset Statistics.
7. Exit program.

Enter your choice:6
Data Statistics: 
Minimum Value:  1
Maximum Value:  4
Sum of all Value:  10
Average of al Value:  2.5
Dispayed Data statistics successfully!
-----------------------------------------------

Enter your choice:7
Exiting the program. Goodbye!
-----------------------------------------------


'''