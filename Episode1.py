# sets in python
# set is a collection of non-repititive elements

s = {2,3,4,4,4,5,6,6,6,"vivek","vivek"}
print(type(s))
print(s) # {2,3,4,5,6,vivek}
s.add(22)# contains only one arguments 
print(s)
s.remove("vivek") # remove from the set any elements
print(s)

s1={"genix","gemini","vivek",2}
print(s.union(s1)) #{2,3,4,5,6,'vivek',22,'genix','gemini'}
print(s.intersection(s1))  #{2} #only output have numbers

