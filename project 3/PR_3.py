print("Welcome to the student data organizer: ")
while True:
    print("1. To add student data.")
    print("2. Display all students.")
    print("3. Update student information")
    print("4. Delete student.")
    print("5. Display sujects offered.")
    print("6. Exit.")
    list_of_all_students = []
    choice = int(input("Enter your choice: "))
    found = False
    match choice:
        case 1:
            id = int(input("Students ID: "))
            name = input("Students Name: ")
            age = int(input("Students Age: "))
            grade = input("Students Grade: ").upper()
            Date_of_Birth = int(input("Date of Birth (YYYY-MM-DD)"))
            subject = input("Enter students subject: (separated by commas) ")

            student = {"id": id,"name": name,"age": age,"grade": grade,"Date_of_Birth": Date_of_Birth,"subject": subject}
            list_of_all_students.append(student)
            found = True

        case 2:
            if found == True:
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
                    else:
                        print("Student not found.")            
                        
        case 4:
            delete_id = int(input("Entrer the students ID to delete: "))

            for student in list_of_all_students:
                if student["id"] == delete_id:
                    list_of_all_students.remove(student)
                    print("Student deleted successfully.")

                else:
                    print("Student not found.")
        case 5:
            subjects_offered = set()
            for student in list_of_all_students:
                subject = student["subject"]
                subjects_offered.append(subject)
            
            print("Subjescts offered: ",subjects_offered)
            
        case 6:
            print("Exiting the program dhanyavad!")
            break    

