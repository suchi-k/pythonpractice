# Dictionaries acts like HashMap that means 
# Dict object does not allow having duplicate Keys. (*** Important Note)
# If we try to update/add an existing key with new value again to the dictionary, then value for the key gets overrided.
# Note: Dictionary keys should be always of type immutable that means dict allows str, tuple, int as their keys. 
# We cannot keep list data type as a Dict key. 

# d = {} # empty dict
# # d.update([1,2]) # update function accepts only dictionary object as an arg
# d.update({"name": "vinay"}) 
# print(d) # d = {"name": "vinay"}

# d.update({"age":24})
# print(d) # d = {"name": "vinay", "age":24}

# d.update({"name":"kumar"}) 
# print(d) # d = {"name": "kumar", "age":24}

# print(d.items()) # [('name', 'kumar'), ('age', 24)] items() returns key:val in tuples
# print(d.keys()) # ['name', 'age'] keys() returns in list
# print(d.values()) # ['kumar', 24] values() returns in list

# for key in d: # iteration occurs on dict keys() by default 
#     print(key) # returns key for each iteration

# for item in d.items(): # performing iteration on dict ietms()
#     print(item) # returns (key, value) in form of tuple for each iteration. Eg: ('name', 'kumar')
#     print(item[0]) # to see the key Eg: name
#     print(item[1]) # to see the val Eg: kumar


# for key, val in d.items(): # performing iteration on dict ietms()
#     print(key) # unpacks the (key, val) tuple to key, value for each iteration Eg: name 
#     print(val) # Eg: kumar

## Testing what data types allowed as dict keys (List and Dict data types are not allowed as dict keys)
# d = {"name":"vinay", (1,2):45, 3:"hyd", {"a":"n"}:678, [1,2]:8, None:"NA", True:67} # Not allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd", [1,2]:8, None:"NA", True:67} # Not allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd", None:"NA", True:67} # Allowed
# d = {"name":"vinay", (1,2):45, 3:"hyd"} # Allowed
# print(d)


## 1) Dict object does not allow having duplicate Keys. (your keys shouldn't get modified at run time)
# d = {1:{"a":[]}, 3:4, 1:5} # key 1 is duplicated so it considers the last occurence val that means {1:5}

## 2) Dict cannot allow unhashable data types (like Lists and Dictionaries) as its keys
# li = ['vinay', 2, 4, 'hyd']
# d = {li:56} # why Lists are not considered as dict keys? (unhashable type: 'list')
# Ans: you can modify the list. Lists are mutable. We can make the item assignemnt in List data types. 
# li[3]='bang' --> ['vinay', 2, 4, 'bang']
# if your List->li is modified then what if the purpose of keeping this one as your dict key

# dict = {'vinay': 'hyd', 'sree':'bang'}
# d = {dict:56} # why Dicts are not considered as dict keys? (unhashable type: 'dict')
# Ans: you can modify the dictionary. Dicts are mutable. dict['sree']='pune' --> dict = {'vinay': 'hyd', 'sree':'pune'}
# if your List->li is modified then what if the purpose of keeping this one as your dict key


## 3) you can only read the elements with the help of index position from immutbale objects.
# We cannot make item assignment on immutable objects like strings, tuples.
# string = "vinay" 
# print(string[0]) # v
# print(string[-1]) # y
# string[0] = 'k' # Correct or Wrong statement ?
# # Ans: Strings are Immutable. TypeError: 'str' object does not support item assignment

# tu = (2,3,4)
# tu[0] = 5 # TypeError: 'tuple' object does not support item assignment

## get() in dict
# dict = {"city":"HYD", "country":'IND'}
# dict.items() # [("city", "HYD"), ("country", 'IND')]
# dict.keys() # ['city', 'country']
# dict.values() # ['HYD', "IND"]
# # print(dict.get()) # get() takes one arg i.e. we need to pass key
# print(dict.get('city'), dict['city']) # 'HYD''HYD'

## why do we use get() if we can access the value by calling the key name in square bracket format??
# print(dict['state']) # KeyError: 'state' i.e  state key is not defined/found in the dict
# print(dict.get('state')) # None (No Error)
# print(dict.get('state', "NO state provided")) # NO state provided (No Error)

## Ans: suppose let's say we have list of dictionaries. 
# Find all the state values provided in the list. If state is not provided print 'Not Available'
l = [
    {"city":"Bang", "country":'IND', 'state':'karnataka'}, 
    {"city":"Pune", "country":'IND', 'state':'Maharashtra'}, 
    {"city":"HYD", "country":'IND'}, 
    {"city":"Chennai", "country":'IND'}
    ]

# print(l[0].get('state')) # karnataka
# print(l[1].get('state')) # Maharashtra
# print(l[2].get('state')) # None
# print(l[3].get('state')) # None

# for obj in l:
#     print(obj.get('state', "Not Provided"))

## sorting the list of dictionaries. sort() function plays with '<' and '>'
# l = [1,2,3,8,7,0,54,23]
# l.sort() # arrange the elements in ascending order by default
# print(l) # [0, 1, 2, 3, 7, 8, 23, 54] # 1<2? 1<3? 1<8? 1<0?(swap) 


## Know the operation/usage of '<', '>' on which Data Types (cannot apply on dict types)
## 1) We can apply < on same types of int, str, list, tuple, bool instances
# print(4<5) # True
# print("vinay"<"kumar") # False (if you apply < on str objects it arranges the strings in alphabetical order)
# print([1,2]<[3,4]) # True
# print((1,2)<(3,4)) # True
# print(True<False) # False # (1<0)

# print({"a":1}<{"a":2}) # TypeError: '<' not supported between instances of 'dict' and 'dict'

## 2) We cannot apply < on different types of instances
# print(4<"5") # TypeError: '<' not supported between instances of 'int' and 'str'
# print("vinay"<[1,2]) # TypeError: '<' not supported between instances of 'str' and 'list'
# print([1,2]<(3,4)) # TypeError: '<' not supported between instances of 'str' and 'list'
# print((1,2)<{"a":(3,4)}) # TypeError: '<' not supported between instances of 'tuple' and 'dict'
# print(True<"vinay") # TypeError: '<' not supported between instances of 'bool' and 'str'

## We cannot apply sort() on a list which are having different types of elements
# l = [2, "vinay", [], (), True] # 2<"vinay"? (int<str)
# l.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

## We cannot apply sort() directly on a list of dictionaries

l = [
    {"city":"Bang", "country":'IND', 'state':'karnataka', 'cases':3456}, 
    {"city":"Pune", "country":'IND', 'state':'Maharashtra', 'cases':9876}, 
    {"city":"HYD", "country":'IND', 'cases':78}, 
    {"city":"Chennai", "country":'IND', 'cases':12345}
    ]

# print("Input list to be sorted:: \n", l)
l.sort(key=lambda x:x['cases'], reverse=True) # list of dict gets sorted as per cases in asc order
print(l)
sorted_l = sorted(l, key=lambda i: i['cases'], reverse=True)
print(sorted_l)

# city - cases
# for x in sorted_l:
#     print(x['city'], x['cases']) # x={'city': 'Chennai', 'country': 'IND', 'cases': 12345}

# l=[5,3,2,4,1]

# a = l.sort()
# print(sorted(l))