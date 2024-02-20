'''
filter can helps the values and filter takes sequence and
it will gives sequence.filter can takes two parameters one is func_name,iterables.
map()takes two parameters one is func_name,iterables.
reduce takes two values at the time for ex:
10 values that time take two values.

'''
from functools import reduce
nums = [1,2,3,56,47]


# evens = list(filter,nums)
evens = list(filter(lambda n:n%2==0,nums))
evens = list(filter(lambda n:n%2==0,nums))
print(evens)

def update(n):
    return n+2
doubles = list(map(lambda n:n+2,evens))
print(doubles)

def add_all(a,b):
    return a+b
sum = reduce (lambda a,b:a+b,doubles)
print(sum)