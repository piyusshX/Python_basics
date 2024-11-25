fruit = input("Enter your Fruit : ")
color = (input(f"Color of your {fruit} : ")).lower()

if color == 'green':
    print(fruit,"is unripe")
elif color == 'yellow':
    print(fruit,"is ripe")
else:
    print(fruit,"is overripe")