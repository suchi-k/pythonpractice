#-------Normal fucntion to lambda function-------------#
print('\n-------Normal fucntion to lambda function-------------')
def func():
    return "Hello"
    
out = func()
print("Normal Function: ", out)

out = lambda :"Hello"
print("Lambda function: ", out())
#-------Normal fucntion to lambda function-------------#


#-------fucntion with args to lambda function-------------#
print('\n-------fucntion with args to lambda function-------------')
def div(a,b):
    return a/b

out = div(5, 10) # func call
print("Function with args: ", out)

out = lambda a,b:a/b
print("Lambda with args: ", out(5,10))
#-------fucntion with args to lambda function-------------#

#-------fucntion with *args to lambda function-------------#
print('\n-------fucntion with *args to lambda function-------------')
def func(*args):
    return sum(args)

out = func(1,2,3)
print("Function with *args: ", out)

out = lambda *args:sum(args)
print("Lambda with *args", out(1,2,3))
#-------fucntion with *args to lambda function-------------#

#-------fucntion with list comprehension to lambda function-------------#
print('\n-------fucntion with list comprehension to lambda function-------------')

arr = [1,2,3,4,5,6]

def func(arr):
    return [i for i in arr if i % 2 == 0]

print("Normal func having list comprehension: ", func(arr))

out = lambda arr:[i for i in arr if i%2==0]
print("Lambda having list comprehension: ", out(arr))
#-------fucntion with list comprehension to lambda function-------------#

#---------------------
def even_num(arr):
    return [i for i in arr if i%2==0]
    
def odd_num(arr):
    return [i for i in arr if i%2!=0]

even = even_num(arr)
odd = odd_num(arr)
print(f"\nNormal function returning even and odd\neven: {even}\nodd: {odd}")
#---------------------

#---------------------
even_num = lambda arr: [i for i in arr if i%2==0]
odd_num = lambda arr: [i for i in arr if i%2!=0]
even = even_num(arr)
odd = odd_num(arr)
print(f"\nLambda returning even and odd\neven: {even}\nodd: {odd}")
#---------------------

#-------Normal for loop with Normal function-------------#
def normal_fun(var):
    """ returns True if var in vowels else False """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (var in vowels):
        return True
    else:
        return False
        
seq = ['a', 'v', 'k', 's', 'b', 'd', 'i']
res = []
for i in seq:
    if normal_fun(i) == True:
        res.append(i)
        
print("\nNormal for loop with normal function: ", res)
#-------Normal for loop with Normal function-------------#

#-------filter with lambda function-------------#
lambda_fun = lambda var: True if var in ['a', 'e', 'i', 'o', 'u'] else False
print("\nFilter with lambda function: ", list(filter(lambda_fun, seq)))
#-------filter with lambda function-------------#
