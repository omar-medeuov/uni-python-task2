# Task 1: Positive or Negative
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Task 2: Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 3: Pass or Fail
score = float(input("Enter the student's score (0-100): "))

if score >= 50:
    print("Pass")
else:
    print("Fail")

# Task 4: Weather Advice
temperature = float(input("Enter the temperature: "))

if temperature > 25:
    print("Hot")
elif temperature >= 10:
    print("Warm")
else:
    print("Cold")

# Task 5: Age Check
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
