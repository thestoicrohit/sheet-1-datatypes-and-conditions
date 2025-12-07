n, k, a = map(int, input().split())

x = n * k

if x % a != 0:
    print("double")
elif (x // a) <= 2147483647:
    print("int")
else:
    print("long long")