#dictionary in python chpater 5 #
#  It is mutable
# it is a key and value pairs
marks={"vivek":79,
       "yash":87,
       "Vaibhavi":88
    }

print(marks.type(marks))
print(marks["vivek"]) # define pair of element first  so they give second element of the pair 
print(marks.items()) # tey shows that all iteam which is contains in dict in tuple form
print(marks.keys) # show all the key
print(marks.values) #show all the values
print(marks.update({"vivek":99,"vaibhavi ":99,"sakshi":88})) # it is updates any values of pair and add pair in dict
