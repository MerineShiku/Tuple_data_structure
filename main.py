
'''
Tuples are similar to lists, but their values can’t be modified. Because of this, when you use tuples in your code, you are conveying to others that you don’t intend for there to be changes to that sequence of values. Additionally, because the values do not change, your code can be optimized through the use of tuples in Python, as the code will be slightly faster for tuples than for lists.
'''



'''
Tuples use round brackets
The tuple elements are ordered
Tuple is immutable. # How Tuples Differ from Lists
# The primary way in which tuples are different from lists is that they cannot be modified. This means that items cannot be added to or removed from tuples, and items cannot be replaced within tuples.

# You can, however, concatenate 2 or more tuples to form a new tuple.

Tuple elements dont need to be unique
Tuple elements can be different data types


Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

'''
fruit = ()
print(type(fruit)) #empty tuple

'''
Tuples have values between parentheses ( ) separated by commas ,. Empty tuples will appear as coral = (), but tuples with even one value must use a comma as in coral = ('blue coral',).
'''

#coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')'
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


'''


We can concatenate string items in a tuple with other strings using the + operator:


'''

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
print('This reef is made up of ' + coral[1])
 
# Output
# This reef is made up of staghorn coral
# We were able to concatenate the string item at index number 0 with the string 'This reef is made up of '. We can also use the + operator to concatenate 2 or more tuples together.


'''

Slicing Tuples


# We can use indexing to call out a few items from the tuple. Slices allow us to call multiple values by creating a range of index numbers separated by a colon [x:y].

# Let’s say we would like to only print the middle items of coral, we can do so by creating a slice.
'''
print(coral[1:3])
 
# Output
# ('staghorn coral', 'pillar coral')




# When creating a slice, as in [1:3], the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the items at position, 1 and 2 are the items that print out.

# If we want to include either end of the list, we can omit one of the numbers in the tuple[x:y] syntax. For example, if we want to print the first 3 items of the tuple coral — which would be 'blue coral', 'staghorn coral', 'pillar coral' — we can do so by typing:

print(coral[:3])
 
# Output
# ('blue coral', 'staghorn coral', 'pillar coral')
# This printed the beginning of the tuple, stopping right before index 3.

# To include all the items at the end of a tuple, we would reverse the syntax:

print(coral[1:])
 
# Output
# ('staghorn coral', 'pillar coral', 'elkhorn coral')
# We can also use negative index numbers when slicing tuples, similar to the positive index numbers:

print(coral[-3:-1])
print(coral[-2:])
 
# Output
# ('staghorn coral', 'pillar coral')
# ('pillar coral', 'elkhorn coral')
# One last parameter that we can use with slicing is called stride, which refers to how many items to move forward after the first item is retrieved from the tuple.

# So far, we have omitted the stride parameter, and Python defaults to the stride of 1, so that every item between two index numbers is retrieved.

# The syntax for this construction is tuple[x:y:z], with z referring to stride. Let’s make a larger list, then slice it, and give the stride a value of 2:

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print(numbers[1:11:2])
 
# Output
# (1, 3, 5, 7, 9)
# Our construction numbers[1:11:2] prints the values between index numbers inclusive of 1 and exclusive of 11, then the stride value of 2 tells the program to print out only every other item.

# We can omit the first two parameters and use stride alone as a parameter with the syntax tuple[::z]:

print(numbers[::3])
 
# Output
# (0, 3, 6, 9, 12)
# By printing out the tuple numbers with the stride set to 3, only every third item is printed:

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

# Slicing tuples with both positive and negative index numbers and indicating stride provides us with the control to receive the output we’re trying to achieve.


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
'''
# Concatenating Tuples
# Operators can be used to concatenate or multiply tuples. Concatenation is done with the + operator, and multiplication is done with the * operator.

# The + operator can be used to concatenate two or more tuples together. We can assign the values of two existing tuples to a new tuple:

# Because the + operator can concatenate, it can be used to combine tuples to form a new tuple, though it cannot modify an existing tuple.
'''
'''

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

coral_kelp = (coral + kelp)
print(coral_kelp)
 
# Output
# ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis')

'''
Multiplying Tuples
'''
# The * operator can be used to multiply tuples. Perhaps you need to make copies of all the files in a directory onto a server or share a playlist with friends — in these cases you would need to multiply collections of data.

# By using the * operator we can replicate our tuples by the number of times we specify, creating new tuples based on the original data sequence.

'''

# Let’s multiply the coral tuple by 2 and the kelp tuple by 3, and assign those to new tuples:

'''

multiplied_coral = coral * 2
multiplied_kelp = kelp * 3

print(multiplied_coral)
print(multiplied_kelp)
 
# Output
# ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral', 'blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
# ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis', 'wakame', 'alaria', 'deep-sea tangle', 'macrocystis')


# Existing tuples can be concatenated or multiplied to form new tuples through using the + and * operators.


'''

# Tuple Functions
# There are a few built-in functions that you can use to work with tuples. Let’s look at a few of them.
'''

'''
len()
Like with strings and lists, we can calculate the length of a tuple by using len(), where we pass the tuple as a parameter, as in:
'''
# len(coral)
 
# This function is useful for when you need to enforce minimum or maximum collection lengths, for example, or to compare sequenced data.

# If we print out the length for our tuples kelp and numbers, we’ll receive the following output:

print(len(kelp))
print(len(numbers))
 
# Output
# 4
# 13
# We receive the above output because the tuple kelp has 4 items:

# kelp = ('wakame', 'alaria', 'deep-sea tangle', 'macrocystis')
 
# And the tuple numbers has 13 items:

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
 
# Although these examples have relatively few items, the len() function provides us with the opportunity to see how many items are in large tuples.


'''
# max() and min()
# When we work with tuples composed of numeric items, (including integers and floats) we can use the max() and min() functions to find the highest and lowest values contained in the respective tuple.

# These functions allow us to find out information about quantitative data, such as test scores, temperatures, prices, etc.
'''
# Let’s look at a tuple comprised of floats:


 
# To get the max(), we would pass the tuple into the function, as in max(more_numbers). We’ll combine this with the print() function so that we can output our results:

# Just like with the len() function, the max() and min() functions can be very useful when working with tuples that contain many values.

more_numbers = (11.13, 34.87, 95.59, 82.49, 42.73, 11.12, 95.57)


print(max(more_numbers))
 
# Output    # 95.59

print(min(more_numbers))

# Output  # 11.12

# The max() function returned the highest value in our tuple.

# Similarly, we can use the min() function:

# Here, the smallest float was found in the tuple and printed out.


'''
# Conclusion
# The tuple data type is a sequenced data type that cannot be modified, offering optimization to your programs by being a somewhat faster type than lists for Python to process. When others collaborate with you on your code, your use of tuples will convey to them that you don’t intend for those sequences of values to be modified.

'''