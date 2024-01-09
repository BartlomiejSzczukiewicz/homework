import math

class C():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        if self.x > 0 and self.y > 0:
            return 1
        if self.x > 0 and self.y < 0:
            return 4
        if self.x < 0 and self.y < 0:
            return 3
        if self.x < 0 and self.y > 0:
            return 2
    def m2(self,a,b):
        quadrant = self.m1()
        if a == 0 or b == 0:
            quadrant2 = 0
        if a > 0 and b > 0:
            quadrant2 = 1
        if a > 0 and b < 0:
            quadrant2 = 4
        if a < 0 and b < 0:
            quadrant2 = 3
        if a < 0 and b > 0:
            quadrant2 = 2
        if quadrant == quadrant2:
            return True
        return False
    def m3(self,a,b):
        distance = math.sqrt((a-self.x)**2+(b-self.y)**2)
        if distance > 5:
            return True
        return False
plane = C(2,3)

print(plane.m1())
print(plane.m2(7,4))
print(plane.m2(-3,1))
print(plane.m3(8,5))
print(plane.m3(4,7))

plane1 = C(0,5)

print(plane1.m1())
print(plane1.m2(4,7))
print(plane1.m2(-7,0))