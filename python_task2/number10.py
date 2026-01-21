
class Person():
    def __init__(self, age: int):
        self.age = age

    def vote_eligibility(self) -> bool:
        return self.age >= 18

    def bus_eligibility(self) -> bool:
        return self.age >= 21

    def retirement_eligibility(self) -> bool:
        return self.age >= 65



person = Person(23)
if person.vote_eligibility():
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

if person.bus_eligibility():
    print("You are eligible to buy a bus ticket")
else:
    print("You are not eligible to buy a bus ticket")

if person.retirement_eligibility():
    print("You are able to retire")
else:
    print("You are not able to retire")