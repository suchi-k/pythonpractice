'''
why did use numpy in array is single double,or threeblue dimnesionals are there 
that case we use the numpy for  different dimensionals.
ndm is numbers of dimensional 
you want to two arrys convert one array then we use flatten function.
#we can put 6 values inthe array that time its work if didnt put the 
#six values in the array doesnt it work.reshape function is also not execute.
how to convert two d array in matrix.if you give the each  two values then we put semicolones how many rows you want
that case we increase the values also.



'''
from numpy import *

arr1 = array([
                [1,2,3,6,2,9], 
                [4,5,6,7,5,3]#this is two dimensional array how to we check you execute arr1 that time

                        #carefully observe it one array function we can put two arrays  that it this is two d array.  
            ])
print(arr1)
arr2 = arr1.flatten()   
print(arr2)
arr3 = arr2.reshape(3,4)
arr3 = arr2.reshape(2,2,3)

print(arr3)
m = matrix('1 2 3;56 4 7;9 0 8')#if you  didnt put always dimensional arrays then we use this matrix
#in matrix function we used  so many rows but you know how  many rows you want. 
print(m)
print(diagonal(m))#if you want matrix we performs this concepts .py