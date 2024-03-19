
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b

print('{0:<4} | {1:<4} | {2:<4} | {3:<4} '.format('sum','dif','mul','div','mod'))
print('{0:<4} | {1:<4} | {2:<4} | {3:<4} '.format(add,sub,mul,div,mod))