n = int(input())
x = 0

while n > 0:
    y = n % 10
    n = n // 10
    if x < y:
        x = y
print(x)
