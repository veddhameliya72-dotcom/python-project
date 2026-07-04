# for case 1:
# date and time operation:



import datetime, time

def current_time():
   date_time = datetime.datetime.now()
   date = date_time.strftime("%d/%m/%Y")
   time = date_time.time().replace(microsecond=0)

   print(f"Current Date = {date}")
   print(f"Current Time = {time}")

def date_difference():
  
   date_1 = input("Enter The First Date (DD/MM/YYYY): ")
   date_2 = input("Enter The Second Date (DD/MM/YYYY): ")

   try:
      date_1 = datetime.datetime.strptime(date_1, "%d/%m/%Y").date()
      date_2 = datetime.datetime.strptime(date_2, "%d/%m/%Y").date()
   except ValueError:
      print("Invalid Date Format")

   difference = date_2 - date_1

   print(f"Difference is: {difference.days}")

def formate_date():
   while True:
      print("\nchoose the Fomrat's: ")
      print("1. YYYY/MM/DD ")
      print("2. DD/MM/YYYY")
      print("3. Exit\n")
      choice = int(input("Enter Your Choice: "))
      print()

      match choice:
         case 1: 
            date = datetime.datetime.now().strftime("%Y/%m/%d")
            print(f"choosen format: {date}")            
 
         case 2: 
            date = datetime.datetime.now().strftime("%d/%m/%Y")

            print(f"choosen format: {date}")
         case 3:
            print("you are exiting from the format date module...........")
            break
         case _:
            print("youve entered invalid choice...........")

def stop_watch():
   print("Enter for Starting The Stopwatch...")
   input()
    
   start_t = time.time()
   print("Stopwatch is Started! Press Ctrl+C To Stop.")
    
   try:
      while True:
         elapsed_time = int(time.time() - start_t)
         print(f"Elapsed Time: {elapsed_time} Seconds", end="\r")
         time.sleep(1)
            
   except KeyboardInterrupt:
      print(f"\nStopwatch is Stopped. Time: {elapsed_time} Seconds")


def count_down():
   try:
      start = int(input("Enter value of countdown: "))
   except ValueError:
      print("Invalid Number")

   for i in range(start, 0, -1):
      print(f"{i}", end="\r")
      time.sleep(1)
   print("Hurrah mission accomplished!")  
