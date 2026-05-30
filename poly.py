class Polynomial:
    def __init__(self):
        self.coeffs=[]
    def getdata(self):
        n=int(input("Enter no of coefficients:"))
        print("Enter coefficients")
        for i in range(n):
            self.coeffs.append(int(input("enter coefficient {}:".format(i+1))))
    def __mul__(self,other):
        res=[]
        l=(len(self.coeffs)+ len(other.coeffs))
        for i in range(l):
            res.append(0)
        for i in range(len(self.coeffs)):
            for j in range(len(self.coeffs)):
                res[i+j]=self.coeffs[i]*other.coeffs[j]
        p=Polynomial()
        p.coeffs=res
        return p
    def display(self):
        n=len(self.coeffs)
        for i in range(n):
            pow=n-i-1
            if pow >1:
                print("{}x^{}".format(self.coeffs[i],pow),end='')
            elif pow ==1:
                print("{}x".format(self.coeffs[i]),end='')
            else:
                print("{}".format(self.coeffs[i]),end='')
            if i !=(n-1):
                print("+",end="")
        print()
p1=Polynomial()
p2=Polynomial()
print("Enter polynomial 1:")
p1.getdata()
print("Enter polynomial 2:")
p2.getdata()
print("Result:")
p3=p1*p2
p3.display()
