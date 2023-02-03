from math import ceil, sqrt

#Autora: Anaid Jimenez Moreano

'''

  Resuelve para k en β =a^k mod p dado un numero primo p
  b= beta, a = alfa
  si p no es primo no se podria usar el algoritmo de babystep-gianstep.
  
  '''

def bsgs(alfa, beta, p):

    N = ceil(sqrt(p - 1))  # p-1 si p es primo // Si n = √ p −1, entonces k = q*n+r, por lo que

    #construccion de la tabla
    #  Baby step. //base, exponente, mod
    tabla = {pow(alfa, i, p): i for i in range(N)}

    # Usando el teorema de Fermat para recomponer
    c = pow(alfa, N * (p - 2), p)

    #
    #Busca el equivalente en la tabla Giant step.
    for j in range(N):
        y = (beta * pow(c, j, p)) % p
        if y in tabla:
            print("Resultado para K: ")
            return j * N + tabla[y]

    # Solucion no hallada
    return print("Solucion no hallada")

if __name__ == '__main__':
    #Ingrese valor de beta, y numero primo
    print("Ingrese alfa: ")
    alfa= int(input())
    print("Ingrese beta: ")
    beta=int(input())
    print("Ingrese numero primo: ")
    p=int(input())

    #PRUEBA TEST alfa y beta pueden no ser numero primo, usaremos valores de 36 bits
    #https://poliformat.upv.es/access/content/group/DOC_34876_2022/Material%20asociado/RetosDL.txt usamos el del ejemplo

    print(bsgs(alfa, beta, p))

    #para test
    #print(bsgs(9536854785, 7596854856, 3094892893)) #res: 1238021729