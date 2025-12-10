n = input().strip()
rev = n[::-1]
rev_num = str(int(rev))
print(rev_num)
if n == n[::-1]:
    print("YES")
else:
    print("NO")
