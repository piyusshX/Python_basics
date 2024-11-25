# **kwargs -> It allows a function to accept a variable number of keyword arguments, packing them into a dictionary. 
# This is useful when you don’t know in advance what specific keyword arguments will be passed

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(Hero="Deku", Power="One for All", Inspiration="All Might")
print("\n")
print_kwargs(Anime="Natsume Yuujinchou", Main_Character="Natsume Takashi")