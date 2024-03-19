
def check():
    while True:
        try:
            a = int(input("Please Value of a in numbers:"))
            b = int(input("Please Value of b in numbers:"))
        except:
            print("you did not entered numbers")
            continue
        else:
            print("yes its numbers")
            break
        finally:
            print("Execution Seccessful")
            print(a+b)
            
check()            
            
        