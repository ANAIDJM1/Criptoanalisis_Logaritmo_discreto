import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1
    while g == 1:
        x = ((x * x) % n + c) % n
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n
        g = gcd(abs(x - y), n)
    return print(g)

if __name__ == '__main__':
    #numero de 10 bita
    pollard_rho(2023)
