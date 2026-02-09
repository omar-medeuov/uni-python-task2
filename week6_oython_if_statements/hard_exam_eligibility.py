# Exam Eligibility
attendance = float(input("Enter attendance percentage: "))
exam_score = float(input("Enter exam score: "))

if attendance >= 75 and exam_score >= 50:
    print("Student can pass")
else:
    print("Student cannot pass")
