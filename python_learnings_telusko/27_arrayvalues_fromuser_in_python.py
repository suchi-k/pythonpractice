''''
We dont know size len of array,how to create the array values from the 
coming user .
we create the blank array we asked the array then we will ask the user
enter the value.
We want the create  array we want take the values from the user.

'''


from array import*
arr = array('i',[])
n = int(input('Enter the length from the array'))
for i in range(n):
    x = int(input('Enter the next value'))
    arr.append(x)
print(arr)    
val = int(input('Enter the value for search'))
k = 0
for i in arr:
    if  i==val:
        print(k)
        break
    k+=1
print(arr.index(val))