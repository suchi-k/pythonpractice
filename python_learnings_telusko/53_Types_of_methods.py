class student:
    school = 'suchi' #class method
    def __init__(self,m1,m2,m3): 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value     
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class..in abc molude")

#class methods work class varaibles
# instance methods work instance varaibles
# work extra varaibles if you want class varaibles instance varaibles go to
#the static methods.
                            

    
           

s1 = student(34,35,65)
s2 = student(89,65,66)
student.info()