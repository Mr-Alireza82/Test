import random



def chance(first, last):
    var = random.randint(first, last)
    return var

# show on screen
first = int(input("fisrt: "))
last = int(input("last: "))
print(chance(first, last))