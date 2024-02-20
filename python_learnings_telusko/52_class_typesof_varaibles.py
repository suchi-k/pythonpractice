class car:
    wheels = 4 # This class namespace
    def __init__(self):
        self.mil = 10  # This is instance namespace
        self.com = 'BMW'
c1 = car()
c2 = car()
c1.mil = 15 #this modify value in class
# c1.wheels = 20 # this modify value in class
car.wheels = 8
print(c1.com, c1.mil,c1.wheels)
print(c2.com, c2.mil,c2.wheels)

