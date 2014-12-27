import random
class Person:
    def __init__(self,Name='None',Age=0,Gender='None',Address='None',PhNo='None',TrID='None'):
       	self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Address=Address       
        self.PhNo=PhNo
        self.TrID=TrID
        self.PNR=self.GenPNR()

    def GenPNR(self):
        return ''.join(random.choice('0123456789ABCDEF') for i in range(10))
    
    def show_data(self):
        print ("Name of Passenger :", self.Name)
        print ("Age :",self.Age)
        print ("Gender :",self.Gender)
        print ("Phone number :", self.PhNo)
        print ("Address :",self.Address)
        print ("Train No. :",self.TrID)
        print ("PNR No :",self.PNR)










 