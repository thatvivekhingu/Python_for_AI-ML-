# MUltilevel Inheritance in python

class grandfather:
    a="Dada"

class father(grandfather):
    b ="Pappa"

class Son(father):
    c="Son"

obj=Son()
print(obj.c,obj.b,obj.a)