from numpy import *
arr = array([1,2,3,4,5])
'''
In Numpy is stands for numeric
view is adifferent function whch helps createing anew array.
shallow copy means it simply copy the elements then both the add the elements 
Deep copy arr = arr1.copy()

'''

arr[1]=7
arr = arr +5
print(arr)
arr1 =array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
arr3 = arr1 +arr2
# print(concatenate(arr1+arr2))
print(arr3)
# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))
# this way you copying the arrays
arr2 =arr1
arr2 = arr1.view()#view is adifferent function whch helps createing anew array.

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))