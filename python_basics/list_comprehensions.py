""" list comprehension helps us to write one liner codes """

#----- single for loop with if and else conditions into list comprehension ------#
l = [1,2,3,4,5,6]

l1 = []
for i in l:
    if i%2 == 0:
        l1.append(i)

l1 = [i for i in l if i%2==0]

l2 = []
for i in l:
    if i%2 == 0:
        l2.append(f"{i} is Even")
    else:
        l2.append(f"{i} is Odd")

print('\nSingle for loop with if and else conditions into list comprehension')
l2 = [f"{i} is Even" if i%2== 0 else f"{i} is Odd" for i in l]
print(l2)


l3 = ['suchi', 'vinay', 'csv', 'xml', 'bang', 'hyd']
vowels = ['a', 'e', 'i', 'o', 'u']

# for i in l3:
#     if 'a' in i:
#         pass
#     elif 'e' in i:
#         pass
#     elif 'i' in i:
#         pass
#     elif 'o' in i:
#         pass
#     elif 'u' in i:
#         pass
#     else:
#         print(i)

print('\nExample of Single for loop with if condition into list comprehension')
for elem in l3:
    if not any([True for char in vowels if char in elem]):
       print(elem)
#----- single for loop with if and else conditions into list comprehension ------#


#----- Multiple for loops without if and else conditions into list comprehension ------#
print('\nMultiple for loops without if and else conditions into list comprehension')
l2 = [[1,2], [3,4],[5,6]] # --> 2D Array (2 Dimensional Array/List)

for i in l2:
    for j in i:
        print(j)
        
l3 = [j for i in l2 for j in i]
print(l3)
#----- Multiple for loops without if and else conditions into list comprehension ------#


#----- Multiple for loops with if conditions into list comprehension ------#
print('\nMultiple for loops with if conditions into list comprehension')
l2 = [[1,2], [3,4],[5,6]] # --> 2D Array (2 Dimensional Array/List)

for i in l2:
    for j in i:
        if j%2==0:
            print(j)
        
l3 = [j for i in l2 for j in i if j%2 == 0]
print(l3)
#----- Multiple for loops with if conditions into list comprehension ------#

#----- Multiple for loops with if and else conditions into list comprehension ------#
print('\nMultiple for loops with if conditions into list comprehension')
l2 = [[1,2], [3,4],[5,6]] # --> 2D Array (2 Dimensional Array/List)

for i in l2:
    for j in i:
        if j%2==0:
            print(f"{j} is Even")
        else:
            print(f"{j} is odd")
        
l3 = [f"{j} is Even" if j%2 == 0 else f"{j} is odd" for i in l2 for j in i]
print(l3)
#----- Multiple for loops with if and else conditions into list comprehension ------#


#----- Multiple for loops with multiple if conditions into list comprehension ------#
print('\nMultiple for loops with multiple if conditions into list comprehension')
l2 = [[1,2], [3,4],"vinay", 56, {"name":"suchi", "city":"NY"}, [5,6]] # --> 2D Array (2 Dimensional Array/List)

for i in l2:
    if isinstance(i,list):
        for j in i:
            if j%2==0:
                print(j)

l3=[j for i in l2 if isinstance(i,list) for j in i if j%2==0]
print(l3)
#----- Multiple for loops with multiple if conditions into list comprehension ------#

#----- Multiple for loops with multiple if and else conditions into list comprehension ------#
print('\nMultiple for loops with multiple if and else conditions into list comprehension')
l2 = [[1,2], [3,4],"vinay", 56, {"name":"suchi", "city":"NY"}, [5,6]] # --> 2D Array (2 Dimensional Array/List)

for i in l2:
    if isinstance(i,list):
        for j in i:
            if j%2==0:
                print(f"{j} is Even")
            else:
                print(f"{j} is Odd")

l3=[f"{j} is Even" if j%2==0 else f"{j} is Odd" for i in l2 if isinstance(i,list) for j in i]
print(l3)
#----- Multiple for loops with multiple if and else conditions into list comprehension ------#