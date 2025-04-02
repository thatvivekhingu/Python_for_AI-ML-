# practice que 1 to 3 

# practice que 1 :Write a program to print multiplication table of a given number using for loop.
'''
n=int(input("enter the number :"))

for i in range(1,11):
   print(f"{n}x{i}={n*i}")
'''

# practice que 2 :  Write a program to greet all the person names stored in a list 'l' and which starts with S.

'''l=["sumit","saujanya","vivek","java","sagar"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")
'''

# practice que 3 : Write a program to find whether a given number is prime or not.

'''n=int(input("enter the number :"))

for i in range(2,n):
    if(n%i)==0:
        print("This is not a prime number:",n)
        break
    else:
        print("This is a prime number:",n)
        break
'''

