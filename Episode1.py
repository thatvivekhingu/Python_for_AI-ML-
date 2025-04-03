# functions in python

'''def sum():
    a=int(input("enter number"))
    b=int(input("enter number"))

    c=a+b
    print(c)

sum()
'''
# function with arguments

def say(name):
    print("good morning"+ " "+name)
say("vivek")


def say(name,ending):
    print("good morning"+ " "+name +" "+ending)
say("vivek","how do you do??")


# in function with return value

def say():
    print("good morning")
    return "ok"
a=say()
print(a)
# output 
# good morning
# ok



#functions in default arguments

def say(name,ending="kem chho?"):
    print("good morning"+ " "+name+" "+ending)
say("vivek" ,"majama" ) # o/p good morning vivek majama
say ("vivek") # o/p good morning vivek kem chho

