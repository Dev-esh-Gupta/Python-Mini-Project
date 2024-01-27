def add(*args):
    sum  = 0
    for num in args:
        sum += num
    print(sum)


add(3,4,7,9)
add(4,5,6,1,0,9)

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)


calculate(add=3, multiply=5)