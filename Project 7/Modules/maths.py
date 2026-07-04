import math

def cal_factorial():

  fac = int(input("Enter Number For Factorial: "))
  print(f"Factorial Of '{fac}' is:", math.factorial(fac))

def compound_interest():

  principal = float(input("Enter The Principal Amount: "))
  raw_rate = float(input("Enter The Annual Interest Rate: "))
  time = float(input("Enter The Time The Money Is Invested For (In Years): "))
  n = float(input("Enter The Number Of Times Interest Is Compounded Per Year: "))

  rate = raw_rate/100

  amount = principal * math.pow((1 + rate / n), (n * time))
  total_amount = round(amount, 2)
  interest_earned = round(total_amount - principal, 2)

  print(f"\nThe Total Amount After {time} Years Is: {total_amount}")
  print(f"The Total Interest Earned Is: {interest_earned}")

def Trigonometri():
  angle_degrees = int(input("Enter The Degree: "))

  angle_radians = math.radians(angle_degrees)

  sin_val = math.sin(angle_radians)
  cos_val = math.cos(angle_radians)
  tan_val = math.tan(angle_radians)

  print(f"Sine of {angle_degrees}°: {sin_val}")
  print(f"Cosine of {angle_degrees}°: {cos_val}")
  print(f"Tangent of {angle_degrees}°: {tan_val}")

def calculate_area():
    shape = input("Enter shape (rectangle, triangle): ").lower()
    
    try:
        if shape == "rectangle":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = l * w
            print(f"The area of the rectangle is: {area}")
            
        elif shape == "triangle":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
            print(f"The area of the triangle is: {area}")
            
        else:
            print("Dont be ovesmart, select from given options only.🤚🤚🤚")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")