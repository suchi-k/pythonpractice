# '''
# Types of arguments are there 
# 1) Formal arguments is a we define the func and after paratisize
# means() that brackets we can pass the arguments that is formal args in that brackets.
# 2) Actual arguments we can call the func then that time we passed arguments in that call 
# atual arguments.
# 3)Actual arguments can be divide four types
# *) position args
# *)keyword args
# *)default 
# *)varaible length
# '''

# def add(a,b):#his is formal args
#     c =a+b
#     print(c) 
# add(10,25)  #this actual args  

# def person_detials(name,age):
#     print(name)
#     print(age)
# person_detials(name = 'suchi',age = 25)#keyword args


# def person_detials(name,age=19):# if you dont want pass the value in func call()
#     print(name)                  #  that time it will take default value if you pass the 
#     print(age)                   #  value in func call that takes only that valuesand excute
# person_detials(name = 'suchi')

# def person_detials(name,age=19):# if you dont want pass the value in func call()
#     print(name)                  #  that time it will take default value if you pass the 
#     print(age)                   #  value in func call that takes only that valuesand excute
# person_detials(name = 'suchi',age=20)

# def sum(a,*b):# this varaible length
#     print(a)
#     print(b)
# sum(4,5,1,0,23)

def sum(a,*b):# this varaible length two args are there one value go first args,and
    c = a     #second value  go second args if you want the fecth all the value that time  
    for i in b: # we can use for loop
        c= c + i
    print(c)
sum(4,5,1,0,23)


def sum(*b):   
    c = 0 
    for i in b: 
        c= c + i
    print(c)
sum(4,5,1,0,23)# this varaible length we can pass int ,str float.