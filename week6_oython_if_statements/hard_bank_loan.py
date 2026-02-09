# Bank Loan Approval
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
years_of_work = int(input("Enter years of work: "))

if salary >= 30000 and credit_score >= 650 and years_of_work >= 2:
    print("Loan approved")
else:
    print("Loan denied")
