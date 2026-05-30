class vector:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    def getdata(self):
        self.x=int(input("enter x "))
        self.y=int(input("enter y "))
        self.z=int(input("enter z "))
    def __add__(self,other):
        v=vector()
        v.x=self.x+other.x
        v.y=self.y+other.y
        v.z=self.z+other.z
        return v
    def __sub__(self,other):
        v=vector()
        v.x=self.x-other.x
        v.y=self.y-other.y
        v.z=self.z-other.z
        return v
    def __mul__(self,s):
        v=vector()
        v.x=self.x*s
        v.y=self.y*s
        v.z=self.z*s
        return v
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def dot(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def cross(self,other):
        v=vector()
        v.x=self.y*other.z-self.z*other.y
        v.y=self.z*other.x-self.x*other.z
        v.z=self.x*other.y-self.x*other.z
        return v
    def display(self):
        print("({},{},{})".format(self.x,self.y,self.z))
v1=vector()
v2=vector()
print("Enter vector 1:")
v1.getdata()
print("Enter vector 2:")
v2.getdata()
print("\nAddition:")
(v1+v2).display()
print("\nSubtraction:")
(v1-v2).display()
s=int(input("Enter a scalar value:"))
print("\nMultiplication:")
(v1*s).display()
print("Equality check:")
print(v1 == v2)
print("\nDot product:",v1.dot(v2))
print("\nCross product :")
(v1.cross(v2)).display()
