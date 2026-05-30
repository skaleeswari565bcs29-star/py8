class word:
    def __init__(self,s1):
        self.s1=s1
    def __add__(self,other):
        return word(self.s1+other.s1)
    def __eq__(self,other):
        if self.s1 == other.s1:
            return True
        else:
            return False
    def display(self):
        print("{}".format(self.s1))
s1=input("enter first string:")
s2=input("enter second string:")
w1=word(s1)
w2=word(s2)
print("Concatenation result:")
(w1+w2).display()
print("Equality check:")
print(w1 == w2)
