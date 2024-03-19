
for i in range(3,-3,-1):
    try:
        print(1.0/i)
    except ZeroDivisionError:
        print("You're trying to divide by zero")
        