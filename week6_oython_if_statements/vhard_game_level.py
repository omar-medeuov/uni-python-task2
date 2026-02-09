# Game Level System
score = int(input("Enter player score: "))
time = int(input("Enter time in seconds: "))
lives = int(input("Enter remaining lives: "))

if score >= 500 and time < 60 and lives >= 3:
    level = "Master"
elif score >= 300 and time < 120 and lives >= 2:
    level = "Pro"
elif score >= 150 and time < 180 and lives >= 1:
    level = "Intermediate"
else:
    level = "Beginner"

print("Player level: " + level)
