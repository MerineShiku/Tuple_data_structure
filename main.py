'''

Tuples use round brackets
The tuple elements are ordered
Tuple is immutable
Tuple elements dont need to be unique
Tuple elements can be different data types

'''
# fruit = ()
# print(fruit) #empty tuple


# fruit = ("orange", (1, 2, 3, 4), [4, 5,6])
# print(type(fruit)) #<class 'tuple'> tuple can contain multiple data set


# fruit = "hello"
# print(type("hello")) #<class 'str'>

# fruit = "hello",
# print(type(fruit))  #<class 'tuple'>


# fruit =  1, 2, 3

# print(type(fruit)) # <class 'tuple'> python interpretes any data set with a comma as a tuple 

'''
Accessing elements in a tuple via indexing

'''
# fruit =("oranges", "mangoes", "avocado", "pineapples")
# print(fruit[0]) #output >> oranges    This means the tuple are ordered and can be accessed using index



'''
slicing of tuple


'''
# fruit =("oranges", "mangoes", "avocado", "pineapples")
# print(fruit[:]) #output is same as list ('oranges', 'mangoes', 'avocado', 'pineapples')

# print(fruit[::-1]) #output is reverse order of list ('pineapples', 'avocado', 'mangoes', 'oranges')

# print(fruit[::-2]) #output is ('pineapples', 'mangoes') the tuple runs from the end and skips every second item

# print(fruit[::2]) #runs from beginning and skips every second item ('oranges', 'avocado')


# print(fruit[:2]) #runs from beginning to the second item ('oranges', 'mangoes')


'''
tuples are immutable

'''
# fruit =("oranges", "mangoes", "avocado", "pineapples")

# fruit[0] = "pears"
# print(fruit) # error TypeError: 'tuple' object does not support item assignment >> tuple is immutable or cant be reassigned 


# del fruit[0]
# print(fruit) #ypeError: 'tuple' object doesn't support item deletion

'''
You can alter a tuple by deleting one of the tuple elements but you can delete the entire Tuple

'''
# del fruit
# print(fruit) #NameError: name 'fruit' is not defined


'''
Compared to the list the tuple has fewer functions
'''

#print(dir(tuple))


fruit =("oranges", "mangoes", "avocado", "pineapples")
print(fruit.count("oranges")) #output is the number of occurence of the item in the tuple

print(fruit.index("avocado")) #>>output is 2. Avocado is on index position 2