#Create a class BANK and with two function simple interest and compound interest. 
# U need to create instance for pnb, icici and hdfc banks with corresponding input.
import math
class BANK():
    def __init__(self,p,r,t,n):
        self.p=p
        self.r=r
        self.t=t
        self.n=n
    
    def simple(self):
        interest=(self.p*self.r*self.t)/100
        print("simple interest: ", interest)
        
    def compound(self):
        b=1+(self.r/self.n)
        d=self.n*self.t
        e=math.pow(b,d)
        interest2=self.p*e
        print("compound interest: ", interest2)
        
bank_name= input("enter your bank name- pnb,icic or hdfc: ")
p= int(input("enter the amount you have submitted"))
t= int(input("enter the time(year) "))
n= int(input("enter number of times interest is compounded per year"))


if(bank_name=="pnb"):
         
    pnb=BANK(p,2,t,n)
    pnb.simple()
    pnb.compound()
    
if(bank_name=="icic"):

    icic=BANK(p,2,t,n)
    icic.simple()
    icic.compound()
    
    
if(bank_name=="hdfc"):
    hdfc=BANK(p,2,t,n)
    hdfc.simple()
    hdfc.compound()