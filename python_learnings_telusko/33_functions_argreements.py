def update(x):
    print(id(x))
    x =8
    print(id(x))
    print("x",x)
a =10
print(id(a))
update(a)
print("a",a)   


def update(lst):
    print(id(lst))
    lst [1] = 25
    print(id(lst))
    print("x",lst)
lst = [10,20,30]            
print(id(lst))
update(lst)
print('lst',lst)







'''
when youpass the value to when you call the function by passing the value to show 
the same id then the movement change the value change the address.
'''