# all imports are Python modules/files
import sys
''' sys.argv statement helps to capture/store the command line or runtime arguments
Command line arguments are nothing but the words we pass while executing Python command.

ex: python <file_name.py> <arg1> <arg2> <arg3>...

Q) how can we read the command line arguments..?
Ans: We know that sys.argv can store the command line arguments in the below format
sys.argv = ['<file_name.py>', '<arg1>', '<arg2>', '<arg3>', ...]
then we can read the specific argument with the help of index

Note: sys.argv or input() always reads the command line arguments in String datatype
'''
x = sys.argv[1]
y = sys.argv[2]
z = x + y
print(z)

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = a + b
print(c)

res = input('enter a char: ')[0]
print(res)

res1 = eval(input('enter an expr: '))
print(res1)
