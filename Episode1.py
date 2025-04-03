# practice que chpter 8

# que :Write a program using functions to find greatest of three numbers.

'''
def great(a,b,c):
    
    
    if(a>b and a>c):
        print(a,"is greatest number:")
    elif(b>a and b>c):
        print(b,"is greatest number:")
    elif(c>b and c>a):
        print(c,"is greatest number:")

great(4,7,3)'''

# que  : Write a python program using function to convert Celsius to Fahrenheit.

def converter():
    c=int(input("enter celcious :"))
    f=(c*1.8)+32
    print(f"Fehrenhit value is :{f}")
    
converter()