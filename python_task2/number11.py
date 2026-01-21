def calculate(numberA: int, numberB: int, operator: str) -> int:
    if operator == "+":
        return numberA + numberB
    elif operator == "-":
        return numberA - numberB
    elif operator == "*":
        return numberA * numberB
    elif operator == "/":
        return numberA / numberB


print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 5, "/"))

