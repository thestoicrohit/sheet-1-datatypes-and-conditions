x = int(input())

is_prime = True

if x == 1:
    is_prime = False
else:
    i = 2
    while i * i <= x:
        if x % i == 0:
            is_prime = False
            break
        i = i + 1

if is_prime:
    print("YES")
else:
    print("NO")
