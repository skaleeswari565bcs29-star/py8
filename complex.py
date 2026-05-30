class complex:
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def __add__(self,other):
        return complex(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return complex(self.real-other.real,self.imag-other.imag)
    def display(self):
        print("{} + {}i".format(self.real,self.imag))
r1=int(input("enter real part of complex 1:"))
i1=int(input("enter imaginary part of complex 1:"))
r2=int(input("enter real part of complex 2:"))
i2=int(input("enter imaginary part of complex 2:"))
c1=complex(r1,i1)
c2=complex(r2,i2)
print("Addition result:")
(c1+c2).display()
print("Subtraction result:")
(c1-c2).display()
