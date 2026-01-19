def compare_number(numberA: int, numberB: int, numberC: int) -> int:
    if(numberA > numberB and numberA > numberC):
        return numberA
    elif(numberB > numberA and numberB > numberC):
        return numberB
    else:
        return numberC


print(compare_number(10, 5, 3))
print(compare_number(2, 15, 8))
print(compare_number(4, 6, 20))
