# Job Application Filter
age = int(input("Enter your age: "))
experience = int(input("Enter years of experience: "))
degree = input("Enter your degree (bachelor, master, none): ").lower()
programming = input("Do you have programming skills? (yes/no): ").lower()

if age < 18 or age > 60:
    print("Not eligible: age must be between 18 and 60")
elif experience < 2:
    print("Not eligible: need at least 2 years of experience")
elif degree == "none":
    print("Not eligible: a degree is required")
elif programming != "yes":
    print("Not eligible: programming skills are required")
else:
    print("Eligible for the job")
