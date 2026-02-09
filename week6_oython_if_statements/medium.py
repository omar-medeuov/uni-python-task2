# Task 1: Grade System
score = float(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Task 2: Maximum of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

# Task 3: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Task 4: Traffic Light
color = input("Enter traffic light color (red, yellow, green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

# Task 5: Login System
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Login failed")
