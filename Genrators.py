
def square(n):
    for i in range(n):
        yield i**2

for n in square(10):
        print(n)
