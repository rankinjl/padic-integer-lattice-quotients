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


def RowReductionExample():
    #Let p = 3
    zero = PadicNumber([],0)
    one = PadicNumber([1],0)
    a = PadicNumber([1],-2)
    twelve = PadicNumber([1,1],1)
    v1 = PadicVector([twelve,a,one])
    v2 = PadicVector([a.getMultiplicativeInverse(),zero,one])
    v3 = PadicVector([zero,a.getMultiplicativeInverse(),one])
    v = IntegerLattice([v1,v2,v3])
    for i in (v.getReducedVectors()):
        print(i)
    #whereas VectorSpace would result in Identity matrix

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
    a = PadicNumber([1],-2)
    two = PadicNumber([2],0)
    three = PadicNumber([3],0)
    v1 = PadicVector([one,a,zero])
    v2 = PadicVector([a.getMultiplicativeInverse(),zero,one])
    w1 = PadicVector([zero,two,two])
    w2 = PadicVector([one,zero,zero])
    v = IntegerLattice([v1,v2])
    w = IntegerLattice([w1,w2])
    print(v.getIntersection(w))
    #print()
    #vspace = VectorSpace([v1,v2])
    #wspace = VectorSpace([w1,w2])
    #print(vspace.getIntersection(wspace))
'''
    

def testIL():
    '''
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
    
    one = PadicNumber([1],0)
    cubed = PadicNumber([1],3)
    v = IntegerLattice([PadicVector([one,PadicNumber([1],1)]),PadicVector([PadicNumber([1],2),one])])
    w = IntegerLattice([PadicVector([one,cubed]),PadicVector([cubed,one])])
    print(v.getIntersection(w))
    '''
    
    '''
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

    #RowReductionExample()
    #testIL()
    #testVSIntersection()

main()
