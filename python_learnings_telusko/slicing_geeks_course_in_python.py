#  '''
#  slicing postive index syntax[start:stop:step]postive index start 0
#  slicing negative index syntax[start:stop:step]negative index start -1

# #  examples:
# '''
a= [10,2.1,34,True,[1,2,3],(10,14),{'a':'1'}]
# for i in range(len(a)-1,-1,-1):# this is negative index -1
#     print(i,a[i])

#  # postive index 0
# print(a[::4])  
for i in range(0,len(a)-1,1):
    print(i,a[i])
    

