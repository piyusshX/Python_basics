# yield -> similar to return keyword yield keyword also returns the value but ye memory me uss function
# ko rakta hai along with its state meaning kitna kaam ye function kar chuka hai. Iss liye yield keyword 
# generator functions me zadatar use hota hai.

def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i

for num in even_generator(10):
    print(num)