'''Generators function can iterate one item and after you can call the yeid
keyword and another item iterated it helps better the memory if dont have 
generators in python its very diffcult very time is wasted 
'''

def part():
    n = 3
    yield n
    n = n*n
    yield n
a = part()    
print(next(a))
print(next(a))


'''Normal functions once you call all items is iterated'''
def part():
    n = 3
    yield n
    n = n*n
    yield n
a = part()    
for i in a:
    print(i)

# generators expressions list comphersions and generators
a = range(6)
print("list comp",end =":")
c = [x+2 for x in a]
print(c)
print("gen exp",end =":")
d = (x+2 for x in a)
print(d)
print(min(d))

    
