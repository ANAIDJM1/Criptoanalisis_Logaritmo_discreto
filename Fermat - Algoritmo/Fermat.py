import math

'''def primo(n:int):
    if n<=1:
        print("No puede ser negativo, cero o 1")
        return False
    for i in range (2,n):
        if n%i==0:
            print(str(n)+" No es primo")
            return False
    print(str(n)+" Es primo")
    return True'''


def cuadrado_perfecto(n:int)->bool:
    c=0
    raiz=math.sqrt(n)
    if (raiz.is_integer()):
        #print("si")
        True
    else:
        #print("no")
        False

def primo_fermat(n:int):
    a =  math.ceil( math.sqrt(n) )
    b = math.pow(a,2) -n

    while (cuadrado_perfecto(b)==False):
        a=a+1
        b=a*a-n
    print("a "+str(a))
    print("b: "+str(b))
    print ("q= "+str(a-math.sqrt(b)))
    print("p= "+str(a+math.sqrt(b)))



if __name__ == '__main__':
    #primo de 11 bits
    primo_fermat(2039)

