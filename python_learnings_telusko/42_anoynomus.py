def square(a):
    return a*a
result = square(5)
print(result)

ans = lambda a:a*a
result = ans(5)
print(result)

ans = lambda a,b:a+b
result = ans(5,6)
print(result)

'''
Normal function vs anoynomus function lambda
1) In normal functions already function name and def keyword also there we write
so many lines in function but anoynomus function without name we will give the name 
and multiple args but single expression we write only one line code.
'''

