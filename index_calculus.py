import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#limite_primos: representa el límite superior hasta el cual se considerarán los números primos en el proceso de factorización.
def index_calculus(n, limite_primos):
    factores = []
    primos = []
    log_limit = int(math.log(limite_primos) / math.log(2))
    for i in range(2, limite_primos):
        if all(i % j for j in range(2, int(math.sqrt(i)) + 1)):
            primos.append(i)
            print(primos)
    for i in range(len(primos)):
        exponent = int(math.log(n) / math.log(primos[i]))
        while exponent >= 1:
            factor = int(math.pow(primos[i], exponent))
            if n % factor == 0:
                factores.append(factor)
                n = int(n / factor)
                exponent = int(math.log(n) / math.log(primos[i]))
            else:
                exponent -= 1
    for i in range(log_limit):
        numero_randm = random.randint(2, n - 1)
        x = pow(numero_randm, int((n - 1) / limite_primos), n)
        if x != 1:
            for j in range(1, log_limit):
                y = pow(x, pow(2, j), n)
                if y == n - 1:
                    break
                if j == log_limit - 1:
                    factor = gcd(n, x - 1)
                    if factor > 1:
                        factores.append(factor)
                        n = int(n / factor)
    if n > 1:
        factores.append(n)
    return print(factores)

if __name__ == '__main__':
    #primo de 16 bits 65535, nro no primo 65471 // raiz 255
    n = 800  # Número de 10 bits
    limite_primos = int(math.sqrt(n))  # Límite superior para la consideración de primos
    factores = index_calculus(n, limite_primos)
    print("Factores:")
    print(factores)