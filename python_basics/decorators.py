def smart_div(func):
    """ Decorator function helps to perform smart division """
    print(f"1. Inside smart_div Decorator, received inputs func: {func}")
    def inner(a,b):
        print(f"3. Inside Inner function recieved inputs a: {a}, b: {b}")
        if a<b:
            a, b = b, a
        return func(a,b)
    print("2. Completing the decorator")
    return inner

@smart_div ## method-2
def div(a, b):
    """ Normal function just perform divide operation on two operands/variables """
    print(f"4. from div function received inputs a:{a} and b:{b}")
    return a/b

## method-1
# bharathi = smart_div(div)
# out = bharathi(5,10)
# print(out)

## method-2 using "@". It should be applied on the function where we need to apply decorator.
out = div(5,10)
print(out)