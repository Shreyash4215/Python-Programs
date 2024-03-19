
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b

print("sum: {0},Diff: {1}, Mult: {2}, Div: {3},Mod:{4}".format(add,sub,mul,div,mod))
print("sum: %d,Diff: %d, Mult: %d, Div: %10.3f  ,Mod:%d"%(add,sub,mul,div,mod))