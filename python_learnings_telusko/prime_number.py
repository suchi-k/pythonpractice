number = input('Enter the number')
# prime number is greater than 1
if number >1:
    for i in range(2,number):
        if(number % i)==0:
            print(number, "is not prime number")
            break
    else:
        print(number, "prime number")
# if the entered number is lessthan or equal to 1
# then it is not prime number

else:
    print(number, "is not prime number")       