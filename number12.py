def check_conditions(number: int) -> bool:
    if(number >= 10 & number <= 20):
        return True
    elif(number % 7 ==0):
        return True
    else:
        return False


print(check_conditions(15))
print(check_conditions(21))
print(check_conditions(5))

