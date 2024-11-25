age = int(input("Provide an age : "))

# if age < 13:
#     print("Child")
# elif age >= 13 and age <= 19:
#     print("Teenager")
# elif age >= 20 and age <=59:
#     print("Adult")
# else:
#     print("Senior")

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")