x = float(input("Enter x: "))
n = int(input("Enter n: "))
SUM = 0

# 1 + x + x^2 + x^3 + x^4 ... x^n

for i in range(n+1):
    SUM += x**i
print(SUM)

SUM = 0


# 1 - x + x^2 - x^3 + x^4 ... x^n

for i in range(n+1):
    SUM += (-x)**i
print(SUM)

SUM = 0


# 1 + 1/x + 1/x^2 + 1/x^3 ... 1/x^n

for i in range(n+1):
    SUM += 1/(x**i)
print(SUM)

SUM = 0


# x + x^2/2 + x^3/3 + x^4/4 ... x^n/n

for i in range(1, n+1):
    SUM += x**i / i
print(SUM)

SUM = 0


# x + x^2/2! + x^3/3! + x^4/4! ... x^n/n!

for i in range(1, n+1):
    fac = 1
    for j in range(1, i+1):
        fac *= j
    SUM += x**i / fac
print(SUM)

SUM = 0
