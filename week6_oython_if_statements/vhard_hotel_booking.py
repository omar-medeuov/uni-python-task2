# Hotel Room Booking
room_type = input("Enter room type (standard, deluxe, suite): ").lower()
nights = int(input("Enter number of nights: "))
season = input("Enter season (peak, regular, off): ").lower()

if room_type == "standard":
    price = 100
elif room_type == "deluxe":
    price = 200
elif room_type == "suite":
    price = 350
else:
    print("Invalid room type")
    price = 0

if price > 0:
    if season == "peak":
        price *= 1.5
    elif season == "off":
        price *= 0.8

    total = price * nights
    print("Total cost: $" + str(round(total, 2)))
