def debugger(func):
    def wrapper(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        if args_val == '' :
            args_val = "null"
        kwargs_val = ', '.join(f"{key} : {value}" for key, value in kwargs.items())
        if kwargs_val == '' :
            kwargs_val = "null"
        print(f"Function name -> {func.__name__} // args -> {args_val} // kwargs -> {kwargs_val}")
        return func(*args, **kwargs)
    
    return wrapper

@debugger
def greet(name, greeting="Hey!"):
    print(f"{greeting}, {name}")

greet("Blank", greeting="Welcome back!")

@debugger
def hello():
    print('hello world')

hello()