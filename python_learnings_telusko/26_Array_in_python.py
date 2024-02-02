"""
When array is created make sure specific/proper typecode is used.
Signed interger typecode "i" allows postive integers and negative integers.
Unsigned integer typecode "I" doesn't allow negative integers.
Array store the same values, doesn't allow different values.
Array function doesn't work directly. You should import array library.
List works directly doesn't require any imports.

List vs Array
List can store any datatype elements.
Array can store specific datatype elements. 
"""
from array import *
var = array('i', [1,23,-564,87]) # this is signed
print("Signed Arrays: ", var)

try:
    var = array('I', [1,23,-564,87]) # this is unsigned
    print("Unsigned Arrays: ", var)
except Exception as e:
    print("Error Message: ", str(e)) # can't convert negative value to unsigned int

var = array('I', [1, 23, 87]) # this is unsigned
print("Buffer Info: ", var.buffer_info()) # (2990700594368, 3)

for i in range(3):
    print(var[i])

# typecode 'u' supports to store only string datatype elements in an array
num = array('u', ['a','e','i','o','u'])
for i in num:
    print(i)

# we can also create an array by using typecode of another array
var = array('I', [1,23,87])
new_array = array(var.typecode, (i for i in var))
for i in new_array:
    print(i)

i = 0
while i< len(new_array):
    print(new_array[i])
    i = i+1 
