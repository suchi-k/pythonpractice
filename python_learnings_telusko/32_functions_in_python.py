'''
Functions can helps reusability the code ,becuase we can define the function
once and we can  call multiple times .


'''
def main():
    print('Hello World')
    print('Hi')
main()
def add_sub(a,b):
    a = a+b 
    b = a-b 
    return a ,b
res1,res2 = add_sub(10,45)
print(res1,res2)