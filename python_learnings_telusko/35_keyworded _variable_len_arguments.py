def person(name,*data):# this is tuple first arg is separate and second arg 
    print(name)         # will come tuple format excute
    print(data)

person('suchi',25,'jmd',1234)    

def person(name,**data):# if you want multiple args in function call that  
    print(name)         # time we can use **keyword args
    print(data)

person('suchi',age = 25,city = 'jmd',phone = 1234)    

# Here we can use forloop key and value pairs
def person(name,**data):
    print(name)  

    for i ,k in data.items():       
        print(i,k)

person('suchi',age = 25,city = 'jmd',phone = 1234) 
