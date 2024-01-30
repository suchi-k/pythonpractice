"""
string (lower, upper, capitalize, count, find, format, join, split, strip, islower, isupper, isalpha, isalnum, isdigit, isnumeric, replace)
lists (append, extend, insert, pop, index, sort, sorted, remove, count, sum, len, max, min)
tuple (index, count, sum, len, max, min)
dictionaries (items, keys, values, update, get)
"""


string = """Contrary to popular belief, Lorem Ipsum is not simply random text. 
It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. 
Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, 
looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, 
and going through the cites of the word in classical literature, discovered the undoubtable source. 
Lorem Ipsum comes from sections 1.10.32 and 1.10.32 of "de Finibus Bonorum et Malorum" 
(The Extremes of Good and Evil) by Cicero, written in 45 BC. 
This book is a treatise on the theory of ethics, very popular during the Renaissance. 
The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32"""


# print(string.lower()) # All letters in the given string can be converted to lower-Case
# print(string.upper()) # All letters in the given string can be converted to UPPER-Case
# print(string.capitalize()) # Fisrt letter of the string becomes Capital Letter

## split() function returns list of strings. This function helps us to split the given string based on the delimeter.
# print(string.split()) # default parameter: ' ' (whitespace) {string.split(' ')}
# print(len(string.split())) ## returns how many words present in the given string
# print(string.split('.')) # splitting the paragraph with delimeter: '.' (pointer/full-stop)
# print(len(string.split('.'))) # retruns how many sentences in the given string
# print(string.split('1.10.32')) # splits the string with the given delimeter

# name = 'Vinay Kumar Reddy' # ['Vinay', 'Kumar', 'Reddy']
# print(name.split('a')) # ['Vin', 'y Kum', 'r Reddy']
# print(name.split('Vinay')) # ['', ' Kumar Reddy']
# print(name.split('V')) # ['', 'inay Kumar Reddy']
# print(name.split('Suchi')) # ['Vinay Kumar Reddy']
# print(name.split('vinay')) # ['Vinay Kumar Reddy']

## Strip() fucntion returns String by removing passed parameter-characters from the given string at both start & end.
# name = '   Kumar   '
# name1 = 'vivvvnaykumarreddyiviiii'
# print(name.strip()) # 'Kumar'
# print(name.strip('a')) # '   Kumar   '
# print(name1.strip('vi')) # 'naykumarreddy'

## rstrip() fucntion returns String by removing passed parameter-characters from the given string at the end
## lstrip() fucntion returns String by removing passed parameter-characters from the given string at the start
# name1 = 'vivvvnaykumarreddyiviiii'
# print(name1.rstrip('vi')) # 'vivvvnaykumarreddy'
# print(name1.lstrip('vi')) # 'naykumarreddyiviiii'

## find() used to return the lowest index value of the first occurrence of the substring from the input string; else it returns -1. 
# name = 'vivvvnaykumarreddyiviiii'
# print(name.find('iv'))


## format() is a technique of the string category permits you to try and do variable substitutions and data formatting.
# string = '{} is a good option for beginners in python'
# v = [1, 2, 3] # int/str/list/tuple/dict any type can be replaced in the {} while using format()
# print(string.format(v))

# string = '{} is a good option for {} in python'
# v = [1, 2, 3] # int/str/list/tuple/dict any type can be replaced in the {} while using format()
# print(string.format(v)) # error must pass two args to replace two {} in string
# print(string.format(v,v))

## positional vs named args
# --------------------------
# 1) positional formatting
# string = '{} is a good option for {} in python'
# a = "dash_1"
# b = "dash_2"
# print(string.format(a,b)) # dash_1 is a good option for dash_2 in python
# print(string.format(b,a)) # dash_2 is a good option for dash_1 in python

# 2) named formatting
# string = '{x1} is a good option for {x2} in python'
# a = "dash_1"
# b = "dash_2"
# print(string.format(x1="vinay",x2="hdsbhdsbs")) # vinay is a good option for hdsbhdsbs in python
# print(string.format(x2=a,x1=b)) # dash_2 is a good option for dash_1 in python

# suchi_details = {"name":"Suchi", "age":23}
# vinay_details = {"name":"Vinay", "age":27}
# bharathi_details = {"name":"Bharathi", "age":51}

# # print("Hi, MY name is Suchi I am 23 years old") # static print (values are hard-coded)
# # dynamic print (using string format())
# print("Hi, MY name is {name} I am {age} years old".format(name=bharathi_details['name'], age=bharathi_details['age'])) 

# join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator
# list = ["1","2","3","4"] # an iterable object
# string = "vinaykumar" # an iterable object
# tuple = ("vinay", "kumar", ) # an iterable object
# dict = {"mobile":"one plus", "price":"40,999"} # an iterable object
# object = 23 # not an iterable object

# print(" --> ".join(list)) # 1 --> 2 --> 3 --> 4
# print(" --> ".join(string)) # v --> i --> n --> a --> y --> k --> u --> m --> a --> r
# print(" --> ".join(tuple)) # vinay --> kumar
# print(" --> ".join(dict)) # mobile --> price
# print(" --> ".join(object)) # TypeError: can only join an iterable


## isalnum() returns Bool type values (True/False)
""" alpha-numeric means string contains either alphabets or numbers or mix of alphabets and numbers """
# string = "abc123"
# print(string.isalnum()) # True
# print("abc".isalnum()) # True
# print("123".isalnum()) # True
# print("abc$%".isalnum()) # False
# print("".isalnum()) # False {empty strings are not considered as alpha-numerics}


## isalpha() returns Bool type values (True/False)
""" alpha means string contains only alphabets """
# string = "abc"
# print(string.isalpha()) # True
# print("123".isalpha()) # False
# print("abc123".isalpha()) # False
# print("".isalpha()) # False


## isnumeric() returns Bool type values (True/False)
""" numeric means string contains only numbers """
# string = "123"
# print(string.isnumeric()) # True
# print("abc".isnumeric()) # False
# print("abc123".isnumeric()) # False
# print("".isnumeric()) # False


## isdigit() returns Bool type values (True/False)
""" digit means string contains only numbers """
# string = "123"
# print(string.isdigit()) # True
# print("abc".isdigit()) # False
# print("abc123".isdigit()) # False
# print("".isdigit()) # False

## islower() returns Bool type values (True/False)
""" lower means string contains only lower-case alphabets (a, b, c, .., z) """
# string = "vinay"
# print(string.islower()) # True
# print("Vinay".islower()) # False
# print("".islower()) # False


## isupper() returns Bool type values (True/False)
""" upper means string contains only upper-case alphabets (A, B, C, D, ..., Z) """
# string = "vinay"
# print(string.isupper()) # False
# print("Vinay".isupper()) # False
# print("VINAY".isupper()) # True
# print("".isupper()) # False

## replace() method replaces a specified phrase with another specified phrase
""" replace() takes two args 1) which value to be replaced 2) what is the new value we are replacing with """
# string = "vinay" 
# print(string[0], string[-1]) # v y
# string[0] = 'k' # cannot make item assignment 
# string.replace("vin", "ab")
# print(string) # abay (WRONG expected output)?
# Ans: Strings are immutable. that means we cannot change the value ***directly***.
# new_string = string.replace("vin", "ab")
# print(new_string) # abay 
# (old variable string is not modified directly but the value is getting replaced and we are saving into new variable new_string)

########################################################################################
## My Practice 
# name= "vinay"
# print(name)
# print(name.lower())
# print(name.upper())
# print(name.find("na"))
# print(name.count("vi"))
# print(name.strip())
# print(name.strip("nay"))
###################################################################################

# Tuple data type is an immutable data type 
# that means values/elements in the tuple containers cannot be changed.
tup = (4,5,3, 2,1,3,3) 
# print(tup.count(3)) # 3
# print(tup.index(3)) # 2 returns the index of First occurence element
# print(sum(tup)) # 21
# print(len(tup)) # 7
# print(min(tup)) # 1
# print(max(tup)) # 5

# tup.sort() # throws error: AttributeError: 'tuple' object has no attribute 'sort'
###################################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
new operations
l = [1,2,3,4,5,6,7,8,9]


l1 = []
for i in l:
    if i%2==1:
        l1.append(i)

print(l1)
bag=['computer','id',1,23,74,0]
bag.append([''])
print(bag)
bag.extend('vinay')
print(bag)

bag[bag.index('v')] = 1

print(bag)
bag.remove(bag.index('computer'))
print(bag)

bag={'a':3,'b':21,'c':23}
print(bag['a'])
for elem in bag:
    print(elem,bag[elem])
    
print(bag.keys())   
print(bag.items())
print(bag.values())
bag={'a':1,'z':[1,2,3],'c':{'q':23}}
print(bag['c']['q'])

