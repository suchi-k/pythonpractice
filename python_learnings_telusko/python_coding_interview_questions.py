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
l = [01, 20, 03, 40, 05, 60]
