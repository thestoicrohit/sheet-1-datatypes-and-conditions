n = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
positive = 0
negative = 0

for x in numbers:
    if x % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    if x > 0:
        positive = positive + 1
    elif x < 0:
        negative = negative + 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)
