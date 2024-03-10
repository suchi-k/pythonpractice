'''
class inheritance
single   ,multiple,
'''

class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")   # single inheritance

a1 =A()     
a1.feature1()
#a2.feature2()


class B(A):
    def feature1(self):
        print("Feature 3 working")  # single inheritance
    def feature2(self):
        print("Feature 4 working")
b1 = B()    #B is not    inheritance A,B is inheritance c only.                      

class C(B):
    def feature1(self):
        print("Feature 5 working") # this is multilevel inheritance

class C(A,B):
    def feature1(self):
        print("Feature 3 working") # this is multiple inheritance

c1 = C()           
#c1. access any thing c is parents or grandparents are there      