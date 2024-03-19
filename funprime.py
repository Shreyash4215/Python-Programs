
def check(numbers):
    primeNum=[]
    for number in numbers:
        if number>1:
            for i in range(2, int(number/2)+1):
                if(number % i)==0:
                    print(number,"in not prime number")
                    break
            else:
                print(number,"in prime number")
                primeNum.append(number)
        else:
            pass
            
    return primeNum        
    
    
print(check([2,3,4,5,6,7,8,9]))