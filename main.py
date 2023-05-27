#Fundamental Data Types

#Int (integers) => Numbers
#Float => floating point numnber (number with decimals)

#print(type(2 + 4))
#print(type(2 - 4))
#print(type(2 * 4))
#print(type(2 / 4))

#print(type(9.9 + 1.1))

#print(2**3)
#print(2 // 4)
#print(5 // 4)
#print(5 % 4)

#Math Functions (actions)

#print(round(3.1))
#print(abs(-20))

#operator precedence

#print(20 + 3 * 4)

# ()
# **
# * /
# + -

#Variables = everthing that defines/stores an information
#example: iq = 190
#iq = variable
#assingning a variable can also be called "binding"

#Expressions:
# iq = 100
#user_age = iq / 5
#"iq / 5"  is an expression
#the whole "user_age = iq / 5" or "iq = 100" are statements.

#argumented assignement operator

#some_value = 5
#some_value += 2
#this would give a result of "5" + "2" = 7

#Strings

#print(type("helloooo there 34!"))
#username = 'lisisara'
#password = 'strongpassword'

#long_string = '''
#WOW
#O O
#---
#'''
#print(long_string)

#string concatenation = adding strings together

#Type Conversion
# from hashlib import new


# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

#is the same as:

# print(type(int(str(100))))

# Escape Sequence:
# weather = "\t It\'s \"kind of\" sunny \n hope u have a good day!"

#the back-slash(\) tells the programm that everything that comes after the "" is a string

#print(weather)

# "\t" adds a tab to what comes after
#"\n" adds a new line

#Formatted strings:

#name = 'Johnny'
#age = 55

#print('hi ' + name + '. You are ' + str(age) + ' years old!')

#in the formatted string way(new version in python3):

#print(f'hi {name}. You are {age} years old!')

#or (older version on python2) by order:

#print('hi {}. You are {} years old!'.format('Johnny', '55'))

#or (older version on python2) by variable:

#print('hi {}. You are {} years old!'.format(name, age))

#print('hi {1}. You are {0} years old!'.format(name, age))

#String Indexes: strings are immutable but the values can be re-assigned.
#Example:
#selfish = 123
#I can re-assign the value of selfish like this:

#selfish = 1357

#What I can not: mutate the value of selfish without actually reassigning it to a new value

#Example:

# selfish = '123'
#selfish[0] = '8'
#print(selfish)

# we could add '8' to the string selfish:
# selfish = selfish + '8'

#print(selfish)

#string slicing:

#selfish = 'me me me'
#selfish = '01234567'
#01234567 (the index position of each letter in the string, counting the spaces)
#[start:stop:stepover] ex: [0:8:2] <= start at 0 and stop at 2 (not including 2 and stepping over every second number)

#print(selfish[0])
#print (selfish[::2])
#start from the beginning and step over every second number

#print (selfish[-1]) #will start printing out from the end of the list, backwards

#print (selfish[::-1]) #reversed of the string, reversed order

#Build in functions

#len(lenght): counting starts at 1, not 0.

#print(len('hellloooo'))

# greet = 'hellloooo'
#print(greet[:])
#print(greet[0:len(greet)])

#string methods

# quote = 'to be or not to be'
#print(quote.upper())
#print(quote.capitalize())
#print(quote.lower())
#print(quote.find('be'))  #the result here would be '3', which means that the word 'be' appears in the index number '3' or the quote, counting the spaces and starting the count from 0.

#print(quote.replace('be', 'me'))

#Booleans (bool) = true or false

# name = 'Lisis'
# is_cool = False

# is_cool = True

#Exercise: Type Conversion

# name = 'Lisis Araujo'
# age = 29
# relationship_status = 'married'

# #to change relationshio status, just reassign it:

# relationship_status = 'it\'s complicated'

#print(relationship_status)

#birth_year = input('What year were you born?') #the input here is taken as a string, even if it's typped as an integer. Therefore, we have to convert this input into an int(see below) for the programm to be able to calculate it, as it's not possible to calculate a str with an int.

#age = 2022 - int(birth_year)
#print(f'your age is: {age}')

#exercise password checker

#username = input('what is your username?')
#password = input('what is your password?')

#password_length = len(password)
#hidden_password = '*' * password_length

#print(f'{username}, your password, {hidden_password}, is {len(password)} letters long.')




# LISTS / LIST SLICING. With list slicing, we create a new "copy" of the previous list.

# string = 'helloooo'
# string[0:2:1] # start, stop, step = start by index 0, stop at index 2 and go 1 by 1.
# amazon_cart = [
#     'notebooks', 
#     'sunglasses',
#     'toys',
#     'grapes'
# ]
# print(amazon_cart[0::2]) # start at begining, go till the end and skip every second.

# # we can change items of the list because lists are mutable. Exampple:
# amazon_cart[0] = 'laptop'
# print(amazon_cart) # now 'notebook' was replaced by 'laptop'

# new_cart = amazon_cart[0:3] # this is a new created list (by list slicing)
# new_cart = amazon_cart # this would make the amazon list be like the new created cart, including the modifications we made to it.
# # if we want to make new_cart = amazon_cart and keep the original list of amazon_cart, then we need to write it like this:
# new_cart = amazon_cart[:] # the [:] means to copy, which is different from modifying. 
# new_cart[0] = 'gum'
# print(new_cart) 

# print(amazon_cart)

# MATRIX

# matrix = [[]] # an array(list) with another (or many other) array inside of it

# matrix = [
#     [1,2,3],
#     [2,4,6],
#     [7,8,9]
# ]

# print(matrix[0][1]) # here we access the first LIST and then the second item inside that list.

# # LIST METHODS

# basket = [1,2,3,4,5]
# print(len(basket)) # gets the length of the list

# # adding
# basket.append(100) # first we have to delcared what we want to add
# new_list = basket # then create a new object and equal it to the object we just modified
# print(basket)
# print(new_list)


# #insert 
# basket.insert(4, 100) # first we declare where we want to insert (index), then what we want to insert (100). So we insert 100 in the indext position [4]. It modifies the list in place, but does not create a new copy of the list.
# print(basket)

# #extend
# new_list = basket.extend([100,101]) # it just extends the list with the arguments given. It does not create a new list.
# print(basket)

#pop
# basket.pop() # pops off, whatever is at the END of the list
# basket.pop() # everytime this is called, it removes another item of the list
# basket.pop()
# basket.pop(0) # pops the index 0 of the list

# remove
# basket.remove(4) # with remove, we give in the value that we want to remove. With POP we give in the indext position that we want to remove
# print(basket)

# new_list = basket.pop(4) # in this way, pop will return us only the item we "poped out of the list"
# print(new_list)

# # clear
# new_list = basket.clear() # it removes whatever is in the list. Completely clears it
# print(basket)


#------------------------------------------------------

# FOR LOOPS
# for item in 'Zero to Mastery': # "item" is a variable that we created. It could be called anything else. reads: for each item in the iterable(something that is able to be looped over) 'Zero to Mastery', do something.
#     print(item) # the "do something" in this case was to print each item, so each letter.

# for item in [1,2,3,4]: #list
#     print(item)

# for item in {1,2,3,4,5}: #set
#     print(item)

# for item in (1,2,3,4,5,6): #tuple
#     print(item)

# nested loops
# for item in (1,2,3,4,5): 
#     for x in ['a', 'b', 'c']: # here we nested the list inside the tuple. First python goes through the first item in the tuple, then it goes to the second for loop and loops through each item. So we have 1 a, 1 b, 1 c. Then it stops and goes back to the second item of the tuple and jumps again to the second for loop, just like the first one. So 2 a, 2 b, 2 c. And then again, until all the items in the tuple are through
#         print(item, x)

# ITERABLE: list, dictionary, tuple, set, string, etc. Is an object, or collection of items, that can be iterated over. 
# Iterated -> one by one check each item in the collection

#DICTIONARIES

# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user:
#     print(item) # we printed the keys in the dictionary

# for item in user.items(): # gives us the keys and values in a tuple
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# for item in user.items():
#     key, value = item;
#     print(key, value)
# #OR
# for key, value in user.items():
#     print(key, value)

# RANGE FUNCTION (start, stop, step)

# print(range(100))

# for number in range(98, 100):
#     print(number)

# for number in range(0, 10):
#     print('email email list')

# for _ in range(0, 10, 2): # the "_" just indicates that I don't care about how the variable is called, i just want to use the range. It also takes a third parameter, the stepover.
#     print(_)

# for _ in range(10, 0, -2): # we will loop through this 10 times, starting from zero 
#     print(list(range(10)))

# for _ in range(2): # we will loop through this twice
#     print(list(range(10))) # i created a range (iterable object with 10 items), then i converted it into a list

# ENUMERATE FUNCTION 

# for char in enumerate('Helllooo'):
#     print(char)

# for i,char in enumerate('Helllooo'):
#     print(i,char)

# for i,char in enumerate((1,2,3,4)):
#     print(i,char)

# for i,char in enumerate([1,2,3,4]):
#     print(i,char)

# for i,char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is: {i}')

# WHILE LOOPS

# i = 0
# while i < 50:
#     print(i)
#     i += 1
#     break

#OR

# i = 0
# while i < 50: # while this is true, we print i
#     print(i)
#     i += 1
# else:
#     print('done with all the work')


# FOR LOOP VS WHILE LOOP

# my_list = [1,2,3]

# for item in my_list:
#     print(item)

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# while True:
#     input('say something: ')
#     break                           # here it will stop asking for the input as soon as soemthing was entered.

# while True:
#     response = input('say something: ')  # here it will continue asking for input, unless the input is "bye", then it stops.
#     if (response == 'bye'):
#         break


# BREAK, CONTINUE AND PASS (still using my_List)

# continue = makes the method go back to the loop before executing the next line

# my_list = [1,2,3]
# for item in my_list:
#     print(item)
#     continue


# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#     continue

# # pass does nothing. Just passes to the next line.

# my_list = [1,2,3]
# for item in my_list:
#     # still about what to do
#     pass                            ## here the "pass" will make the loop continue and not get an error message that the function is not defined.

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#     pass

# WHAT IS A GOOD CODER?

# 1. clean code
# 2. readability
# 3. predictability 
# 4. DRY: DO NOT REPEAT YOURSELF