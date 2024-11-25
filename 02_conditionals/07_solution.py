order_size = input("Order Size : ")
extra_shot = input("Do you need Extra-shot(true/false) : ")

if extra_shot:
    print(f"Order : A {order_size} Coffee with Extra-shot")
else:
    print(f"Order : A {order_size} Coffee without Extra-shot")