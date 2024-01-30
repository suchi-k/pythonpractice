a = [1,21,32,"str",0.1,(1,2,3),{'a':1,'b':2,'c':3}]
# for i in a:
#     if i==list:
#         print(i)
#     elif i== str:    
#         print(i)
#     else:
#         print(i)    

test = [i if isinstance(i, dict) else "Not a List" for i in a] 
print(test) 


# def test(a):
#     for i in a:
#         if i == list:
#             print(i)
        # elif i == str:
    #         print(i)
    #     else:
    #         print(i)
    # return a
# practice = test([1, 21, 32, "str", 0.1, (1, 2, 3), {'a': 1, 'b': 2, 'c': 3}])
# print(practice)

a.append([1,2,3])
# print(a)
a.insert(0,12)
# print(a)
z =[]

def test(a):
        for i in a:
            if i in z:
                z.append(i)  
                print(z)


q = test([1, 21, 32, "str", 0.1, (1, 2, 3), {'a': 1, 'b': 2, 'c': 3}])
print(q)