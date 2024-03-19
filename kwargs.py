
def fun(**kwargs):
    if 'name' in kwargs:
        print("My name is {0}".format(kwargs['name']))
    if 'age' in kwargs:   
        print("My age is {0}".format(kwargs['age']))

fun(name='champ',age=24)