class A:
    def __init__(self):
        print("in A Init")
class B:
    def __init__(self):
        print("in B Init")  

#obj = B()

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")  

obj = C()        