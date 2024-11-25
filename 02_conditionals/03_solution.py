marks = int(input("Enter your Marks : "))

if marks > 100 or marks < 0:
    print("Invalid Marks!! Please enter valid marks")
    exit()

if marks > 89:
    grade = 'A'
elif marks > 79:
    grade = 'B'
elif marks > 69:
    grade = 'C'
elif marks > 59:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is",grade)