a = int(input())
b = int(input())
k = 0
while a >= b:
    a //= 2
    k += 1

print(k * 12)