score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
if score == 100:
    print("Perfect score!")
elif score < 40:
    print("Retake exam required")