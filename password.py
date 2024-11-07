import random
def cube(count):
    return random.randint(1,count)
def gen(count):
    symvol="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password=''
    for i in range(count):
        password+=random.choice(symvol)
    return password