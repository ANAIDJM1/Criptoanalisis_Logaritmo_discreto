import math

def factorizable(a,b):
  if((a/b).is_integer()):
    #print("True")
    return True
  else:
    #print("False")
    return False



def iterador(c): # debe devolver0,1,-1,2,-2,...

  if c==0:
    c=(c+1)
    print(c)
    return c
  if c>0:
    c=c*(-1)
    print(c)
    return c
  else:
    c=c-1
    print(c)
    return c



def criba_cuadratica2(n):
  basefactores =criba_cuadratica(n)
  m=math.ceil(math.sqrt(n))
  c=0
  #repeat
  ti=iterador(c) #0,1,-1,2,-2,...
  a=(m+ti)
  b=(m+ti)^2-n

  for i in range(0, len(basefactores)-1):
    if (factorizable(b,basefactores[i])==True):
      print(a)
      print(b)
      print(basefactores[i])


def criba_cuadratica(n):
  primos = []
  for i in range(2, n+1):
    es_primo = True
    for j in range(2, int(i ** 0.5) + 1): #potencia de i^1/2 + 1
      if i % j == 0:
        es_primo = False
        break
    if es_primo:
      primos.append(i)
  primos.append(-1)
  return primos




if __name__ == '__main__':
  # probamos con un valor de 17 bits
  print(criba_cuadratica(253438))
  iterador(0)




