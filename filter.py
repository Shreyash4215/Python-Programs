
def evenFn(num):
    return num%2==0
    
a=[1,2,3,4,5]   
 
print(list(map(evenFn,a)))
print(list(filter(evenFn,a)))