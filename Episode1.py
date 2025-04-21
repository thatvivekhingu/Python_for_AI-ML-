# raise in prg( agar aapka dev prg me galati  kar rha hai toh uske code ko stop kardo prg stop kardo)

a=int(input("enter number :"))
b=int(input("enter second number:"))

if(b==0):
    raise ZeroDivisionError("zero division is not allowed")

print(f"the division of {a} and {b} is :{a/b}")

#output
'''enter number :3
enter second number:0
Traceback (most recent call last):
  File "c:\Users\Vivek Hingu\OneDrive\Desktop\moviesSeason01\Episode1.py", line 7, in <module>
    raise ZeroDivisionError("zero division is not allowed")
ZeroDivisionError: zero division is not allowed'''