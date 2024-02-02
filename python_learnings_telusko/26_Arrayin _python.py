"""
when is array is created specific make sure poper typecode
signed means small lettersis allows postive intgers and negative integers 
unsigned is  capital letters dont allow negative integers
array store the same values different values dont allows.
in array function doesnt work directly because you import array library
and after the array function work.
list is work direcly not import because list store any value 
"""
from array import *
# var = array('i',[1,23,-564,87])#this is signed
# print(var)

# var = array('I',[1,23,-564,87])#this is unsigned
# print(var)
var = array('I',[1,23,87])#this is unsigned
# print(var.buffer_info())

# for i in range(3):
#     print(var[i])
# num = array('u',['a','e','i','o','u'])
# for i in num:
#     print(i)
var = array('I',[1,23,87])
new_array = array(var.typecode, ( i for i in var))
# for i in new_array:
#     print(i)

i = 0
while i<len(new_array):
    print(new_array[i])
    i =i+1 
