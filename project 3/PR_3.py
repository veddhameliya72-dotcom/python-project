print("Welcome to the student data organizer: \n")
list_of_all_students = []
while True:
    print("\n1. To add student data.")
    print("2. Display all students.")
    print("3. Update student information")
    print("4. Delete student.")
    print("5. Display sujects offered.")
    print("6. Exit.\n")

    choice = int(input("Enter your choice: \n"))
    found = False
    match choice:
        case 1:
            found = True
            id = int(input("Students ID: "))
            name = input("Students Name: ")
            age = int(input("Students Age: "))
            grade = input("Students Grade: ").upper()
            Date_of_Birth = input("Date of Birth (YYYY-MM-DD)")
            subject = input("Enter students subject: (separated by commas)")
            print("-------------------------------------")
            print("***Student data added successfully***")
            print("-------------------------------------\n")            

            student = {"id": id,"name": name,"age": age,"grade": grade,"Date_of_Birth": Date_of_Birth,"subject": subject}
            list_of_all_students.append(student)
           

        case 2:
            if not found:
                for student in list_of_all_students:
                    print(student)
            else:
                print("No students found.")
        case 3:
            entered_id = int(input("Enter students id: ")) 
            for student in list_of_all_students:
                if student["id"] == entered_id:
                    print("1. Update name.")
                    print("2. Update age.")
                    print("3. Update grade.")
                    print("4. Update date of birth.")
                    print("5. Update subject.")                        
                    
                    update_choice = int(input("Enter your choice: "))

                    match update_choice:
                        case 1:
                            new_name = input("Enter new name: ")
                            student["name"] = new_name
                        case 2:
                            new_age = int(input("Enter new age: "))                                
                            student["age"] = new_age
                        case 3:
                            new_grade = input("Enter new grade: ").upper()
                            student["grade"] = new_grade
                        case 4:
                            new_dob = int(input("Enter new date of birth (YYYY-MM-DD): "))
                            student["Date_of_Birth"] = new_dob
                        case 5:
                            new_subject = input("Enter new subject: (separated by commas) ")
                            student["subject"] = new_subject
                        case _:
                            print("Invalid choice.")
                            print("")
                    print("-------------------------------------")
                    print("***Student updated successfully***")
                    print("-------------------------------------\n") 
                else:
                    print("Student not found.")            
                        
        case 4:
            delete_id = int(input("Entrer the students ID to delete: "))

            for student in list_of_all_students:
                if student["id"] == delete_id:
                    list_of_all_students.remove(student)
                    print("-------------------------------------")
                    print("***Student data deleted successfully***")
                    print("-------------------------------------")

                else:
                    print("Student not found.")
        case 5:
            subjects_offered = set()
            for student in list_of_all_students:
                subject = student["subject"]
                subjects_offered.append(subject)
            
            print("Subjescts offered: ",subjects_offered)
            print("-------------------------------------")
            
        case 6:
            print("Exiting the program dhanyavad!")
            print("-------------------------------------")
            print("-------------------------------------")
            break
'''
output:
Welcome to the student data organizer:
 

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 1

Students ID: 101
Students Name: ved
Students Age: 15
Students Grade: A+
Date of Birth (YYYY-MM-DD)2010-10-27
Enter students subject: (separated by commas) Eng, Maths
-------------------------------------
***Student data added successfully***
-------------------------------------

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 1

Students ID: 102
Students Name: xyz
Students Age: 16
Students Grade: A+
Date of Birth (YYYY-MM-DD)2009-09-26
Enter students subject: (separated by commas) SCi, Computer
-------------------------------------
***Student data added successfully***
-------------------------------------

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 2

{'id': 101, 'name': 'ved', 'age': 15, 'grade': 'A+', 'Date_of_Birth': '2010-10-27', 'subject': 'Eng, Maths'}

{'id': 102, 'name': 'xyz', 'age': 16, 'grade': 'A+', 'Date_of_Birth': '2009-09-26', 'subject': 'SCi, Computer'}

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 3
Enter students id: 101
1. Update name.
2. Update age.
3. Update grade.
4. Update date of birth.
5. Update subject.
Enter your choice: 1
Enter new name: dev
-------------------------------------
***Student data updated successfully***
-------------------------------------
Student not found.

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 2

{'id': 101, 'name': 'dev', 'age': 15, 'grade': 'A+', 'Date_of_Birth': '2010-10-27', 'subject': 'Eng, Maths'}

{'id': 102, 'name': 'xyz', 'age': 16, 'grade': 'A+', 'Date_of_Birth': '2009-09-26', 'subject': 'SCi, Computer'}

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 5
Subjescts offered:  {'SCi, Computer', 'Eng, Maths'}
-------------------------------------

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 4
Entrer the students ID to delete: 102
Student deleted successfully.
-------------------------------------
***Student data deleted successfully***
-------------------------------------

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 2

{'id': 101, 'name': 'dev', 'age': 15, 'grade': 'A+', 'Date_of_Birth': '2010-10-27', 'subject': 'Eng, Maths'}

1. To add student data.
2. Display all students.
3. Update student information
4. Delete student.
5. Display sujects offered.
6. Exit.

Enter your choice: 6
Exiting the program dhanyavad!
-------------------------------------
-------------------------------------
'''

