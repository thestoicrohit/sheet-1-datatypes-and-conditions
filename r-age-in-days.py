n = int(input())
years = n // 365
n %= 365
months = n // 30
n %= 30
days = n
print(years, "years")
print(months, "months")
print(days, "days")
