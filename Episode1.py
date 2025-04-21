# try else in python

try:
    a =int(input("enter thr number:"))
    
except ValueError as e:
    print("this is value error")
else:
    print("try vala execute ho gaya toh else statement bhi execute hogaya")

#output:

# enter thr number:33
# try vala execute ho gaya toh else statement bhi execute hogaya


#enter thr number:mmmm
#this is value error