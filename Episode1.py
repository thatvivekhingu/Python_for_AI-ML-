'''# loops in Python 

# while loop 

i=0
while (i<5):
    print("Pushpa raj")
    i=i+1

# list using while loop

l=[1,2,3,"vivek","shubham","arcade"]

i=0
while(i<len(l)):
    print(l[i])
    i=i+1 # output : all listed element is print



# for loops 

for i in range(0,4):
    print("Google arcade")


# for loop with list 
l=[1,"harry",3,"monkey"]
for i in l:
    print(i)

# fpr loop with tuple 
t=(786,666,"hingu","swags")
for i in t:
    print(i)

#for loop with string 
s="vivek"
for i in s:
    print(i) 
    #o/p : 
    # v
    # i 
    # v 
    # e 
    # k

    # range functions in loop range ( start,end,step-size)

    for i in range(0,10,2):
        print(i)
#output 
#0
#2
#4
#6
#8


# for loop with else 

lis = ["vivek",333,678,954,"code","game",999]

for i in lis:
    print(i)
else:
    print("execute program with else condtion run")
    
'''
# for loop in break

for i  in range(1,20):
    print(i)
    if i==5:
        break # after the 5 prg is stop 

# for loop in continue

for i  in range(1,10):
    print(i)
    if i==8:
        continue  # 8 will skip