# Inheritance in python

class Animal:
    work="Barking"
    name="camel"



class dog(Animal):
    
    print(f"Animal work is {Animal.work} and its type is {Animal.name}")

a=dog()

