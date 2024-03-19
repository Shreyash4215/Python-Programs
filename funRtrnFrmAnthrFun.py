
def addMain(a):
    def addSub(b):
        print(a,b)
        return a+b
    return addSub
    
additon = addMain(100)
print(additon(75))

      
