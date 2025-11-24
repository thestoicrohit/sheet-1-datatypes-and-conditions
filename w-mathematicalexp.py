a, s, b, q, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if s == '+':
    x = a + b
elif s == '-':
    x = a - b
else:
    x = a * b

if x == c:
    print("Yes")
else:
    print(x)