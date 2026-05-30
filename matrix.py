class matrix:
    def __init__(self):
        self.mat=[]
    def getdata(self,r,c):
        print("enter matrix elements")
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(int(input("enter value {}:".format(i+1))))
            self.mat.append(row)
    def __add__(self,other):
        res=[]
        for i in range(len(self.mat)):
            row=[]
            for j in range(len(self.mat[i])):
                row.append(self.mat[i][j]+other.mat[i][j])
            res.append(row)
        m=matrix()
        m.mat=res
        return m
    def __sub__(self,other):
        res=[]
        for i in range(len(self.mat)):
            row=[]
            for j in range(len(self.mat[i])):
                row.append(self.mat[i][j]-other.mat[i][j])
            res.append(row)
        m=matrix()
        m.mat=res
        return m
    def __mul__(self,other):
        res=[]
        for i in range(len(self.mat)):
           row=[]
           for j in range(len(self.mat[i])):
               s=0
               for k in range(len(self.mat)):
                   s += self.mat[i][k]*other.mat[k][j]
               row.append(s)
           res.append(row)
        m=matrix()
        m.mat=res
        return m
    def display(self):
        for i in self.mat:
            print(i)
r=int(input("enter no of rows:"))
c=int(input("enter no of columns:"))
m1=matrix()
m2=matrix()
print("enter matrix 1:")
m1.getdata(r,c)
print("enter matrix 2:")
m2.getdata(r,c)
print("Addition")
(m1+m2).display()
print("Subtraction")
(m1-m2).display()
print("multiplication")
(m1*m2).display()
