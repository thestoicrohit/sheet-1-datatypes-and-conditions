n = int(input())

arr = list(map(int, input().split()))

mn = arr[0]
pos = 1

i = 0
while i < n:
    if arr[i] < mn:
        mn = arr[i]
        pos = i + 1
    i = i + 1

print(mn, pos)
