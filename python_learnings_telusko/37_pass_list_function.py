lst = [10,23,40,56,79,87,21,93]
def count(lst):
    even  = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even =+1 
        else:
            odd =+1   
        return even ,odd        
even,odd = count(lst)    
print("Even:{}and odd:{}".format(even,odd))     
