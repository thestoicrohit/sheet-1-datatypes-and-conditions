n, m, k = map(int, input().split())

ans = min(n, m, k)
n = n - ans
m = m - ans
k = k - ans

ans = ans + min(n // 2, k)

print(ans)