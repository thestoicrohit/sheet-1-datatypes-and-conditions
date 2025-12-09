n = int(input())

arr = list(map(int, input().split()))

mx = arr[0]

i = 1
while i < n:
    if arr[i] > mx:
        mx = arr[i]
    i = i + 1

print(mx)
