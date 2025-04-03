# practice que 4 : Write a program to calculate the factorial of a given number using for loop.
'''
n = int(input("enter the number of you want to calclute: "))

product=1

for i in range(1,n+1):
    product=product*i
print(f"Factorial of {n} is : {product}")
    
'''

# practice que 5 : Write a program to print the following star pattern. for n = 3  
#  *
# ***
#*****

'''n=int(input("enter the number :"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1), end="") # end ="" means print statement new line add nahi karta
    print("")
    '''

# practice que 6 : Write a program to print the following star pattern. for n = 3  
# *
# **
# ***
'''
n=int(input("enter the number :"))

for i in range(1,n+1):
  
    print("*"*(i), end="") # end ="" means print statement new line add nahi karta
    print("")'''


# practice que 7 : Write a program to print the following star pattern. for n = 3  
# * * *
# *   *
# * * *
'''
n=int(input("enter the number :"))

for i in range(1,n+1):
    if(i==1 or i==n ):
        print("*"*(n),end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
'''