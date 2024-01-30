"""
1) Prepare a list of even numbers start from 2 to 20.

a=[]
for i in range(2,20,2):
    a.append(i)
print(a)

2) Find the numbers which are divisible by 5 from the above prepared list

for i in a:
    if i%5==0:
        print('given number divisible by 5 is:',i)


3) "I am learning Python" Replace this string to "I am learning git" 
and add this to the above list at the middle position/index of the list

v="I am learning Python"
k=v.replace('Python','git')    
print(k)

mid_pos = len(a)//2
a[mid_pos]=k
print(a)

4) Print the index and value from the above list. Output should be in the below format 
--> index of value X is Y (where X is the element and Y is index)

for idx, val in enumerate(a):
    print(f"index of element {val} is {idx}")

"""

"""
a="nm"
print(a)

a=[]
for i in range(1,6,2):
    print(i)
    a.append(i)
print(a)
k=len (a)//2
a[k]=k
print(a)
def arg():
    print('harry potter')
arg()    

"""

#--------------------22-10-2022--------------------
# Find the local time now (like date, week_day, hour and time) of a given country
## input: country_name
## output: (22-10-2022, Saturday, 4, 16:22)

from time_converter import get_country_localtime

print(get_country_localtime('America/Tegucigalpa'))
#--------------------22-10-2022--------------------
