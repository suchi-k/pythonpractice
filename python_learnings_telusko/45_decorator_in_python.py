'''
Decorator can helps we dont distrub the original function and  if you
put the dev function one file to another file and we write any logic we didnt change 
original func then we will write decorator func.

'''

def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div) 
div(2,3)           