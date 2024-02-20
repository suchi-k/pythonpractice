''''
Recursion means function call itself
'''

# def main():
#     print("Hello World")
#     main()
# main() 

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())# This is limit if you want how many times are iterate then 
# # we used limit function()
# i = 0
# def main():
#     global i
#     i+=1
#     print("Hello World", i)
#     main()
# main()    


import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
i = 0
def sum(a,b):
    global i
    i+=1
    c= a+b
    print(c,i)
    sum(10,54)
sum(10,54)  