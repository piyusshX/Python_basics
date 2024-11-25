day = input("is wednesday(true/false) : ")
age = int(input("Enter your age : "))

# ticketPrice = 0
# if age < 18:
#     ticketPrice += 8
# else:
#     ticketPrice += 12

ticketPrice = 8 if age >= 18 else 12
# agar if condition true hogi to 8 value assign hogi nhi to 12


if day :
    ticketPrice -= 2

print("Your movie ticket Price : ", ticketPrice)