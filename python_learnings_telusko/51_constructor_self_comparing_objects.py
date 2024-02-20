class computer:
    def __init__(self):
        self.name ='suchi'
        self.age = 20

    def update(self):
        self.age = age   

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False             

c1 = computer()
c1.age = 21
c2 = computer()
if c1.compare (c2):
    print("They are same")
else:
    print("They are not same")    

c1.name = 'su'
c2.age = 24
print(c1.name)
print(c2.age)

