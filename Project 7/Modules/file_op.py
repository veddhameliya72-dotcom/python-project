def create_file():
    filename = input("Enter Filename to be created: ")
    with open(filename, 'w') as f:
        print(f"File {filename} Created Successfully...............")

def write_file():
    filename = input("Enter Filename: ")
    content = input("Enter Content To Write: ")
    with open(filename, 'w') as f:
        f.write(content)
    print("Content is been uploaded successfully...............")

def read_file():
    filename = input("Enter Filename To Read: ")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File Not Found.")

def append_file():
    filename = input("Enter Filename: ")
    content = input("Enter Content To Append: ")
    with open(filename, 'a') as f:
        f.write("\n" + content)
    print("Content Appended Successfully.................................")