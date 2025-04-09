# super key

class grandfather:
    def __init__(self):  # create the constuructor
        print("constructor of grandfather")
    a="Dada"

class father(grandfather):
     def __init__(self):
        print("constructor of father")
     b ="Pappa"

class Son(father):
     def __init__(self):
        super().__init__()            # used super key to also call its method and its super class method
        print("constructor of son")
     c="Son"

obj=Son()
print(obj.c)

#o/p: 
# constructor of father 
# constructor of Son 
# Son