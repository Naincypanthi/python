class first:
    def getnumber(self):
        self.a=int(input("enter your first number"))
        self.b=int(input("enter your second number"))
class second(first):
    def calculation(self):
        self.c=self.a+self.b
        print(f"{self.a}")
class third(first):
    def multi(self):
        self.d=self.a*self.b
        print(f"{self.d}")
ob2=second()
ob3=third()
ob2.getnumber()
ob3.a=ob2.a
ob3.b=ob2.b
ob2.calculation()
ob3.multi()


