# Files Operator
File_name = "Jornal.txt"

class No_Content(Exception):
    pass
class wrong_choice(Exception):
    pass

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# 1.
def Create_file ():
    choice = input("Do want to create a file (Yes/No):").lower()
    if choice == "yes": 
        try:
            file = open(File_name,"x")
            file.close 
            print("File created successfully.....................")
            print("-"*20)
        except FileExistsError:
            print("There is a file which Exists......")
        else :
            pass

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#2.
def Add_Entry():
    try:
        Date = input("Enter Date and Time (DD-MM_YY::00:0 am/pm) : ")
        Entry = input("Enter your journal Entry: ")
        file = open(File_name,"a")
        file.write("\n\nDate & Time : " + Date + "\n")
        file.write("Entry       : " + Entry + "\n\n")
        print("-"*30)
        file.close()
        print("Entry Added successfully.....................")
        print("-"*20)

    except FileNotFoundError:
        print("Create a file for Journal")
        print("-"*20)

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#3.
def Read_file():
    try:
        file = open(File_name,"r")
        content = file.read()

        if content == "":
            raise No_Content()
        else:
            print("FILE CONTEXT:")
            print("-"*10)
            print(content)
            print("-"*10)
            print("END")

        file.close
    except FileNotFoundError: 
        print("Create a file for Journal")
        print("-"*20)   

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#4.
def Search_Entry():
    while True:
        print("\n1. Date/Time.")
        print("2. Keyword.")
        print("3. Exit.\n") 
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                file = open(File_name, "r")
                lines = file.readlines()
                file.close()
                Date_time = input("Enter Date and Time (DD-MM_YY::00:0 am/pm) : ")
                found = False
                for line in lines:
                    if Date_time or "Entry" in line:
                        print(line)
                        found = True
                    
                if not found:
                    print("Tere is no Entry of this Date")
                    print("-"*10)

            case 2:
                file = open(File_name, "r")
                lines = file.readlines()
                file.close()
                keyword = input("Enter the Keyword:")
                found = False
                for line in lines:
                    if keyword or "Date & Time" in line:
                        print(line)
                        found = True
                if not found:
                    print("There no such word...........") 
                    print("-"*10)       
        
            case 3:
                print("Exited from Search Entries....")
                print("-"*10)
                break
            case _:
                raise wrong_choice

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#5.
def clear_all():
        try:
            choice = input("\nAre you sure you want to delete all entries? (yes/no): ")

            if choice.lower() == "yes":
                file = open(File_name, "w")
                file.close()
                print("\nAll entries deleted successfully!")
                print("-*20")
            else:
                print("\nDeletion cancelled.")
                print("-"*20)

        except FileNotFoundError:
            print("\nJournal file does not exist.") 
            print("-"*5)          


print("Welcome.......................\n")  
while True:

    print("\n1. Create a  File:")
    print("2. Add a new Entry.")
    print("3. view all Entries.")
    print("4. Search for an Entry.")
    print("5. Delete Entries.")
    print("6. Exit.\n")  

    choice = int(input("Enter your choice:"))  
    match choice:
        case 1:
            Create_file ()
        
        case 2:
            Add_Entry()

        case 3:
            Read_file()

        case 4:
            Search_Entry()

        case 5:
            clear_all()
            
        case 6:
            print("HAVE A NICE DAY.....................HAVE A GOOD DAY....................HAVE WONDERFULLL DAY")
            print("-------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------------------")
            break
        case _:
            raise wrong_choice
        
'''

output:


Welcome
1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:1
Do want to create a file (Yes/No):yes
File created successfully.....................
--------------------

1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:2
Enter Date and Time (DD-MM_YY::00:0 am/pm) : 27-10-2020
Enter your journal Entry: hii i am learning python
------------------------------
Entry Added successfully.....................
--------------------

1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:3
FILE CONTEXT:
----------


Date & Time : 27-10-2020
Entry       : hii i am learning python


----------
END

1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:4

1. Date/Time.
2. Keyword.
3. Exit.

Enter your choice:1
Enter Date and Time (DD-MM_YY::00:0 am/pm) : 27-10-2020




Date & Time : 27-10-2020

Entry       : hii i am learning python




1. Date/Time.
2. Keyword.
3. Exit.

Enter your choice:2
Enter the Keyword:python




Date & Time : 27-10-2020

Entry       : hii i am learning python




1. Date/Time.
2. Keyword.
3. Exit.

Enter your choice:3
Exited from Search Entries....
----------

1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:5

Are you sure you want to delete all entries? (yes/no): yes

All entries deleted successfully!
-*20

1. Create a  File:
2. Add a new Entry.
3. view all Entries.
4. Search for an Entry.
5. Delete Entries.
6. Exit.

Enter your choice:6
HAVE A NICE DAY.....................HAVE A GOOD DAY....................HAVE WONDERFULLL DAY
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------


'''        