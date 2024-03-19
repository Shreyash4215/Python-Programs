
def square():
    for i in range(10):
        yield i**2

a = square()

print(next(a))
