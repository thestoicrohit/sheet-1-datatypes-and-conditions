a, b = map(int, input().split())
ans = []
for x in range(a, b + 1):
    s = str(x)
    ok = True
    for c in s:
        if c != '4' and c != '7':
            ok = False
            break
    if ok:
        ans.append(str(x))
if len(ans) == 0:
    print(-1)
else:
    print(" ".join(ans))
