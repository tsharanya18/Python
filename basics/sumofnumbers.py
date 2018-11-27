
n = int(input("enter a number : "))
f = 1

while n > 1:
    f = f + n
    n = n - 1

print(f)


n = int(input("enter a number : "))
f = 0

while n >= 1:
    f = f + n
    n = n - 1

print(f)


n = int(input("enter a number : "))
f = 1
t = 0

while f <= n:
    t = t + f
    f = f + 1

print(t)
