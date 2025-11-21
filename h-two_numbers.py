import math

A, B = map(float, input().split())
x = A / B

floor_val = math.floor(x)
ceil_val = math.ceil(x)
if x >= 0:
    round_val = int(x + 0.5)
else:
    round_val = int(x - 0.5)

print("floor", int(A), "/", int(B), "=", floor_val)
print("ceil", int(A), "/", int(B), "=", ceil_val)
print("round", int(A), "/", int(B), "=", round_val)
