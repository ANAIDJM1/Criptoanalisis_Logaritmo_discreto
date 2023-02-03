import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lenstra(n):
    if n % 2 == 0:
        return 2
    a = random.randint(1, n-1)
    x = (a*a) % n
    y = x
    c = random.randint(1, n-1)
    g = 1
    while g == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        g = gcd(abs(x-y), n)
    return g

n = 1234567890123456789
factor = lenstra(n)
print("Factor:", factor)
