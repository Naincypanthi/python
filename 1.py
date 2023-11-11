class first:
    def disp(self):
        self.a=int(input("enter your no."))
        print("this is a real value")
        print(f"{self.a}")
class second(first):
    def disp2(self):

        self.sq=self.a*self.a
        print("this is a square value of a ")
        print(f"{self.sq}")
class third(first):
    def disp3(self):
        print("this is a queue value of a ")
        self.qu=self.a*self.a*self.a
        print(f"{self.qu}")
ob2=second()
ob3=third()

ob2.disp()      #a=4 => ob2

ob3.a=ob2.a
ob2.disp2()
ob3.disp3()

