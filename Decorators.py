
def decoratorfun(welcome):
    def a():
        print("Start")
        welcome()
        print("end")
    return a
    
def subFun():
    print("Sun Fun")
    
obj = decoratorfun(subFun)

obj()
      
