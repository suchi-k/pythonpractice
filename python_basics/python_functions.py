### functions

# function defintion writes only once. Function call might be "n" number of times.
# function can be implemented with and without arguments
# function can return any data type int, Bool, None, str, list, dict, set, function, class obj, generator obj
# function can have single or multiple return statements but only one return statement gets executed
# function helps to obtain re-usability of code and to go with DRY principle

# Type 1: simple function with no args
#------------------------------------
from cmath import pi


def sample_func():
    return "hello "

# a = sample_func()


# Type 2: function with positional arguments (veg, rice, meat, milk)
#------------------------------------------------------------------
# 1) if you are defining a function with pos args, then at the time of function call
# you must pass the number of args required for the respective function
# 2) for pos args, the passed parameters/values from function call would be arranged in the same order
# 3) Always a single return statement will execute for a given function call.
def prepare_food_pos_args(veg, rice, meat, milk):
    """ Function helps to prepare the food based on the received args """

    print(f"veg: {veg}, rice: {rice}, meat: {meat}, milk: {milk}")
    if veg is not None and rice is not None and meat is not None and milk is not None:
        return "Food is prepared for all the items Veg Rice Meat Milk"

    elif veg is not None:
        return "Veg Rice is cooked"

    elif rice is not None:
        return "White rice is cooked"

    elif meat is not None:
        return "Biryani is prepared"
    
    elif milk is not None:
        return "Sweets are prepared with milk products"

    else:
        return "No Food is prepared"

# print(prepare_food_pos_args("carrot", "rice", "chicken", "ghee"))


# Write a function prepare_food with below business logic
# 1) if one or more items provided return "Food prepared for given items: item1, item2, ....." 
# 2) if no item provided return "NO Food is prepared"

# Type 3(a): function with keyword arguments implementing with specified args declaring with None/default value 
#------------------------------------------------------------------------------------------------------ 
def prepare_food_kw_args(veg=None, rice=None, meat=None, milk='curd'):
    """ Function helps to prepare the food based on the received args """
    print(f"veg: {veg}, rice: {rice}, meat: {meat}, milk: {milk}")

    if meat is not None or veg is not None or rice is not None or milk is not None:
        return f"Food prepared for given items: {meat}, {veg}, {rice}, {milk}"

    return "NO Food is prepared"

# print(prepare_food_kw_args(meat="chicken", veg="carrot", rice='rice'))
# print(prepare_food_kw_args(meat="chicken", veg="carrot", rice='rice',milk='ghee'))


# Type 3(b): function with keyword arguments implementing with **kwargs as we don't know how many args to be specified
#---------------------------------------------------------------------------------------------------------------------
# 1) While calling function, positional args cannot appear after keyword arguments
def prepare_food_args(*args,**kwargs):
    """ Function helps to prepare the food based on the received args """
    # print(args) # tuple()
    # print(kwargs) # dict{}

    # print("args: ", args)
    # print("kwargs: ", kwargs)

    # print("args: ", args, "kwargs: ", kwargs)

    print(f'args: {args}, kwargs: {kwargs}')

    if any(kwargs):
        return f"Food is prepared for given items: {', '.join(list(kwargs.values()))}"

    return "NO Food is prepared"

print(prepare_food_args(meat="chicken", veg="carrot", milk="ghee", rice='rice'))
# print(prepare_food_args('beans','milk', 1, meat="chicken"))

## Note:
# any() function helps to Return True if bool(x) is True for any x in the iterable. 
# If the iterable is empty, return False.

# print(any([])) # False
# print(any([1])) # True
# print(any({})) # False
# print(any([0,0,0,0,0])) # False
# print(any([0,0,0,0,1])) # True
# print(all([0,0,0,0,1])) # False
# print(all([1,1])) # True
# print(all([2,3,41])) # True


###############################################################################
def func(): # without args
    print("calling without args function \n")

def func1(a, b): # pos args
    print("calling Pos args function ", end='')
    print(f"a={a}, b={b} \n")

def func2(*args): # n number of pos args 
    print("calling n number of pos args function ")
    print(f"*args = {args} \n")

def func3(**kwargs): # n number of keyword args
    print("calling n number of keyword args function ")
    print(f"**kwargs = {kwargs} \n")

def func4(*args, **kwargs): # n number of args & kwargs
    print("calling n number of args and keyword args function ")
    print(f"*args = {args} \n**kwargs = {kwargs} \n")

def func5(a=None, b=None): # keyword args
    print("calling keyword args function ")
    print(f"a={a}, b={b} \n")


func()
func1("vinay", 5)
func2("vinay", 5, [5,6,7], (1,2,3), {"a":2})
func3(name="vinay", nums=[5,5,6])
func4(4, 5, name="vinay", nums=[5,5,6])
func5(a="vinay")