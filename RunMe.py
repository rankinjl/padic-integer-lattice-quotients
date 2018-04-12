from PadicNumber import *
from PadicMatrix import *
from PadicVector import *
from VectorSpace import *
from IntegerLattice import *

#Pre: need to display helpful tips to user
#Post: helpful tips displayed to user
def displayHelp():
    print("Welcome to the p-adic number program!")
    print()

    
#Pre: need to know if number is prime
#Post: True returned if number is prime, false otherwise
def isPrime(number):
    if(number<=1):
        return False
    else:
        flag = True
        for i in range(2,number):
            if number%i==0:
                flag = False
        return flag

def testVSIntersection():
    '''
    one = PadicNumber([1],0)
    zero = PadicNumber([],0)
    v1 = PadicVector([one,zero,zero])
    v2 = PadicVector([zero,one,zero])
    v = VectorSpace([v1,v2])
    w = VectorSpace([v2,v1])
    print(v.getIntersection(w))
    
    one = PadicNumber([1],0)
    zero = PadicNumber([],0)
    v1 = PadicVector([one,zero,zero,zero])
    v2 = PadicVector([zero,one,zero,zero])
    v3 = PadicVector([zero,zero,one,zero])
    v4 = PadicVector([zero,zero,zero,one])
    v = VectorSpace([v1,v2,v3])
    w = VectorSpace([v2,v3,v4])
    print(v.getIntersection(w))

    zero = PadicNumber([],0)
    one = PadicNumber([1],0)
    two = PadicNumber([2],0)
    three = PadicNumber([3],0)
    v1 = PadicVector([one,one,zero])
    v2 = PadicVector([zero,one,one])
    w1 = PadicVector([zero,two,two])
    w2 = PadicVector([one,zero,three])
    v = VectorSpace([v1,v2])
    w = VectorSpace([w1,w2])
    print(v.getIntersection(w))
    '''

def testIL():
    
    one = PadicNumber([1],0)
    zero = PadicNumber([],0)
    v1 = PadicVector([one,zero,zero,zero])
    v2 = PadicVector([zero,one,zero,zero])
    v3 = PadicVector([zero,zero,one,zero])
    v4 = PadicVector([zero,zero,zero,one])
    v = IntegerLattice([v1,v2,v3])
    w = IntegerLattice([v2,v3,v4])
    print(v.getIntersection(w))
    print("\n")
    #want [0,1,0,0] and [0,0,1,0]

    v1 = PadicVector([PadicNumber([2],0),one])
    w1 = PadicVector([PadicNumber([1],1),PadicNumber([1],1).divide(PadicNumber([2],0))])
    v = IntegerLattice([v1])
    w = IntegerLattice([w1])
    print(v.getIntersection(w))
    #get [1,5/2] since 5/2 is an integer
    '''

    It chose 1 to have the minimum valuation (they both had valuation 1)
    What if it chose 5/2 instead???? We would get a negative valuation for 1

    Do we want to divide by the number with the minimum valuation, or
    divide by p^minvaluation for the minvaluation*******

    v1 = PadicVector([PadicNumber([1],-2),PadicNumber([1],0)])
    w1 = PadicVector([PadicNumber([1],0),PadicNumber([],0)])
    m = PadicMatrix(2,2,[v1,w1],True)
    print(m.getReducedEchelonForm(True))
    '''

#Pre: introduce the user to the p-adic program and allow them to set prime
    #and precision
#Post: help displayed, prime and precision set
def main():    
    displayHelp()
    prime = 0
    precision = 0
    while(not isPrime(prime)):
        try:
            prime = int(input("What prime would you like to use?"))
        except:
            pass
    while(precision<=0):
        try:
            precision = int(input("What precision would you like to use?"))
        except:
            pass
    PadicNumber.setPrimePrecision(prime,precision)

    
    testIL()
    testVSIntersection()

main()
