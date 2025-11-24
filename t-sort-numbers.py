a, b, c = map(int, input().split())

original = [a, b, c]
sorted_nums = sorted(original)

for x in sorted_nums:
    print(x)

print()

for x in original:
    print(x)
