class C():
    def __init__(self,counter):
        self.counter = counter
    def m1(self):
        return self.counter
    def m2(self):
        self.counter = self.counter + 1
        return self.counter
    def m3(self):
        self.counter = self.counter - 1
        return self.counter
    def m4(self,n):
        self.counter = self.counter + n
        return self.counter
    def __str__(self):
        return self.counter

c=C(5)

print(c.m1())
print(c.m2())
print(c.m1())
print(c.m4(-8))
print(c.m1())
print(c.m3())
print(c.m1())
print(c.m4(10))
print(c.m1())
print(c.__str__())
