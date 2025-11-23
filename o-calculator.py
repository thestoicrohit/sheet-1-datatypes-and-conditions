s = input().strip()

# find operator
for op in "+-*/":
    if op in s:
        A, B = s.split(op)
        A = int(A)
        B = int(B)
        if op == '+':
            print(A + B)
        elif op == '-':
            print(A - B)
        elif op == '*':
            print(A * B)
        else:  # '/'
            print(A // B)
        break
