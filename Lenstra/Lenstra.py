# # Example P=(0,1) y^2= x^3+x+1, n = 10403
#
from _ast import Mod
from math import factorial
P= [0,1]
a= Mod(1, 10403)

def easy_mult(n,P):
    result = 'O'
    for i in range(n):
        result = g_l( P, result )
    return result

def mult_2(n,P):
    result = 'O'
    pow_2P = P
    while n!=0:
        if (n%2)==1: result = g_l( pow_2P, result )
        n //=2
        pow_2P = g_l( pow_2P, pow_2P )
    return result

def mult_2_l(n,P,a):
    result = [0,1,0]
    pow_2P = P
    while n!=0:
        if (n%2)==1:
            result = g_l_l( pow_2P, result, a )
            n //=2
            pow_2P = g_l_l( pow_2P, pow_2P, a )
    return result

def g_l( P, Q ):
    if P == 'O':
        return Q
    if Q == 'O':
        return P
    if (P[0] == Q[0]) and (P[1] ==-Q[1]):
        return '0'
    if (P[0] == Q[0]) and (P[1] == Q[1]):
        m = (3*P[0]^2+a)/2/P[1]
    else:
        m = (Q[1]-P[1])/(Q[0]-P[0])
        x3 = m^2-P[0]-Q[0]
        return [x3,m*(P[0]-x3)-P[1]]

def g_l_l( P, Q, a ):
    if P[2] != 1:
        if P[1]==1:
            return Q
        return P
        if Q[2] != 1:
            if Q[1]==1:
                return P
            return Q
        if (P[0] == Q[0]) and (P[1] ==-Q[1]):
            return [0,1,0]
        if (P[0] == Q[0]) and (P[1] == Q[1]):
            if P[1].is_unit()==False:
                return [0,0,P[1]]
            m = (3*P[0]^2+a)/2/P[1]
        else:
            if (Q[0]-P[0]).is_unit()==False:
                return [0,0,Q[0]-P[0]]
            m = (Q[1]-P[1])/(Q[0]-P[0])
        x3 = m^2-P[0]-Q[0]
        return [x3,m*(P[0]-x3)-P[1],1]

#LENSTRA
def lenstra(n,bound_a,bound_b):
    if is_prime(n):
        print (n,'is prime' )
        return n
    if n%2==0:
        return 2
    if n%3==0:
        return 3
    # Consider only elliptic curves
    for a in range(bound_a):
    if Mod(4*a^3+27,n)==0:
        continue

    f_point = [Mod(0,n),Mod(1,n),1]
    for b in range(bound_b): # compute factorial
        f_point = mult_2_l(b+1,f_point,a)
        if f_point[2]==0:
            break
        if f_point[2]>1:
            print (a,b)
            return gcd( f_point[2], n)
        print ('Increase the values of bound_a and bound_b’)



if __name__ == '__main__':
    P= [0,1]
    a= Mod(1, 10403)

    print (mult_2( factorial(7), P )