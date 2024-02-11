'''
Global varaible means out side the function  it can access every where or any where work it
Local varaible means in side the function it can access only inside and work also inside .
if you want or put outside local variable is not work
perference is always given local varaible
Global varaible we can give one value and after you change the value then that case global 
value  remember that changed value dont forgot 
Local varaible we can give one value and after you change the value inside that change value 
only take local varaible and after forgot that values if condition or logic is completed if you want 
that local varaible is printed that is not defined.


'''

a =15

def something():
    a =20
    print("inside function",a)# this local variable
something()  

print("outside function",a)# this global variable


a =15

def something():
    global a  # this is global varaible we cant change local variable we can mentioned
    a =20     # a global variable inside. 
    print("inside function",a)
something()  

print("outside function",a)

a =15
print(id(a))
def something():
    local_a = 9
    x = globals()['a']  # this global varaible is changing the inside function that 
    print(id(x)) #local varaible is not effected 
    local_a = 10
    print("inside function",a)
    globals()['a'] =25
   

something()  

print("outside function",a) 
print(a) #global variable
print(local_a) #local variable