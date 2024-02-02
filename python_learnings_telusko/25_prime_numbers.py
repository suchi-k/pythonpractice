"""
Explanation: A prime number is a natural number greater than 1 that
has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}. 
"""

from math import sqrt

nums = 15


def is_prime(number):
    """
    1) The idea to solve this problem is to iterate through 
    all the numbers starting from 2 to (N/2) using a for loop.
    
    2) For every number, check if it divides N.
    
    3) If we find any number that divides N, we return False.
    
    4) If we did not find any number between 2 and N/2 which divides N 
    then it means that N is prime and we will return True.
    """
    if number <= 1:
        print(f"{number} is not a Prime Number")
        return False
    
    # logic to check prime or not
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            print(f"{number} is not a Prime Number")
            return False
    
    print(f"{number} is a Prime Number")
    return True

print(is_prime(nums))

def is_prime(number):
    """
    Instead of checking till N, we can check till √N because 
    a larger factor of n must be a multiple of a smaller factor 
    that has been already checked. 
    Now let’s see the code for the first optimization method ( i.e. checking till √n )
    """
    if number <= 1:
        return f"{number} is not a Prime Number"
    
    # logic to check prime or not
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return f"{number} is not a Prime Number"
    
    return f"{number} is a Prime Number"

print(is_prime(nums))