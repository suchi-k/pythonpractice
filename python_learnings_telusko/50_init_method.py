class computer:
    def __init__(self,cpu,ram):
        self.cpu =cpu
        self.ram = ram
                    
    def display(self):
        print('i5,16gb,1TB')

    def display(self):
        print('This config is',self.cpu,self.ram)
        

coml =computer('i5',16)
com2 = computer('vwl',80)       
coml.display()  
com2.display()  