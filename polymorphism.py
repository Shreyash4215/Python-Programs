class Elon:
    def __init__(self,name):
        self.name = name
            
    def type(self):
        return "Entrepreneur"
        
class Sundar:
    def __init__(self,name):
        self.name = name
            
    def type(self):
        return "CEO"
        
person1 = Elon('Elon Musk')        
person2 = Sundar('Sundar Pichai')   

print(person1.type())     
print(person2.type())    

for i in [person1,person2]:
    print(i.name)
    print(i.type())
    print("****************")
