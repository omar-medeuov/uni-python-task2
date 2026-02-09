# Movie Ticket Price
age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()

if age < 12:
    price = 5
elif age <= 60:
    price = 10
else:
    price = 7

if day == "saturday" or day == "sunday":
    price += 2

print("Ticket price: $" + str(price))
