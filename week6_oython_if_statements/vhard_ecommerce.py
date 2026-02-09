# E-Commerce Discount System
total = float(input("Enter total amount: "))
membership = input("Enter membership type (gold, silver, none): ").lower()
coupon = input("Do you have a coupon? (yes/no): ").lower()

if membership == "gold":
    discount = 0.20
elif membership == "silver":
    discount = 0.10
else:
    discount = 0

if coupon == "yes":
    discount += 0.05

final_price = total - (total * discount)
print("Discount: " + str(int(discount * 100)) + "%")
print("Final price: $" + str(round(final_price, 2)))
