import math

n = int(input("number: "))
sum = 0

while n > 0:
     sum += n % 10
     print(sum)
     n //= 10
     print(n)

print("final: ", sum)