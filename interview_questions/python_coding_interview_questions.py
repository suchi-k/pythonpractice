""" 
Question:1 
Get the output from the given input in below format

ip = "aaaaabbbbbccccddd"
op = "5a5b4c3d"
"""
from collections import Counter

def format_op(ip):
    """ brute force step-by-step"""
    d = Counter(ip)
    output = []
    for i,val in d.items():
        output.append((str(val)+i)) 
    # print(output)
    test1 = ''.join(output)
    return test1

print(format_op("aaaaabbbbbccccddd"))

def format_op(ip):
    """ one-liner code using in-built Counter function """
    return ''.join([str(val) + key for key, val in Counter(ip).items()])

print(format_op("aaaaabbbbbccccddd"))

def format_op(ip):
    """ without using in-built Counter function """
    # creating our own counter using for loop
    d = {} # {'a':5, 'b':5}
    for i in ip:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return ''.join([str(val) + key for key, val in d.items()])

print(format_op("aaaaabbbbbccccddd"))

""" 
Question:2
Get the output from the given input in below format

ip = "aaaaabbbbbccccdddddddd"
op = 5 # highest number of times character repeated
"""
def find_highest_repeat_char(ip):
    counter = 1
    ans = 1
    for i in range(len(ip) - 1):
        if ip[i] == ip[i+1]:
            # increment the counter since characters sitting beside are same
            counter += 1
        else:
            # store the max count and reset the counter
            ans = max(ans, counter)
            counter = 1
    
    # if last character in given ip is having highest repeated count
    ans = max(ans, counter)
    return ans
            
print(find_highest_repeat_char("aaaaabbbbbccccdddddddd"))

""" 
Question:3
reverse the string

ip = "suchi"
op = "ihcus"
"""

def reverse_str(ip):
    # using slicing 
    # return ip[::-1] 
    
    # using reversed() function
    # return "".join(reversed(ip))

    # using for-loop with negative index
    # for i in range(-1, -len(ip)-1, -1):
    #     print(ip[i], end='')

    # using list comprehension
    return ''.join([ip[i] for i in range(len(ip)-1, -1, -1)])

    # using factorial
    # if len(ip) == 0:
    #     return ip
    # else:
    #     return reverse_str(ip[1:]) + ip[0]

print(reverse_str("suchi"))

""" 
Question:4
using lambda function and retrieve first n even numbers
"""
n = 4
print(list(filter(lambda x:x%2==0, range(n*2))))

""" 
Question:4
Format given list into dict using index as keys and elements as values
"""

nums = [3,1,2,4]
l1=[76, 23, 45, 12, 54, 9] 
print("Original List:", l1)
 
# sorting list using nested loops without used built in sort function
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
print("Sorted List", l1)

sa = [5,1,2,4,3]
print("original list:",sa)
for i in range(0,len(sa)):
    for j in range(i+1,len(sa)):
        if sa[i] >= sa[j]:
            sa[i],sa[j] = sa[j],sa[i]
print("sorted list",sa)
sa.sort()
print(sa)

'''
when we use @classmethod and @staticmethod 

We generally use the class method to create factory methods. Factory methods 
return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
'''

class Person:
    @ classmethod
    def math(cls,marks):
        print('hi')

    @ staticmethod
    def subject(science,hindi):
        print(f"{science} is a 35/100 marks,{hindi} is a 45/100")

Person.math(45)  
Person.subject(35,45)        
# obj = Person()
# obj.math(45)
Person.math(45) 
# obj = subject()
# obj.subject(35,45)

class Method:
    def __init__(self,name):
        self.name = name
        print("This is constructor method")

obj = Method('dasd')  

class A:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def m(self):
        print("This is instance method")

obj = A('harika',21)
obj.m()

# class methods

class A:
    # This is constructor method
    def __init__(self, name):
        self.name = name
        print('Hi') 

class B(A):
    def m1(self):
        print('This is method overridding')
    
    # if you have same function then python execute last one
    def m1(self):
        print('This is a cat') 

obj = A('')  
obj = B('')
obj.m1()

class M:
    @ staticmethod
    def test(self):
        print("This is a static method")
        
    @ classmethod
    def test1(cls,name):
        print("This is a class method")

M.test('hi') 
obj = M()
obj. test('hi')
obj.test1('suchi')


"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])