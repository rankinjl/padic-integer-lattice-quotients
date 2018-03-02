from PadicNumber import *
from PadicMatrix import *
from PadicVector import *
from VectorSpace import *

#Pre: need to display helpful tips to user
#Post: helpful tips displayed to user
def displayHelp():
    print("Welcome to the p-adic number program!")
    print("To create a p-adic number, use [varName = ] PadicNumber(list_of_coefficients,smallest_power)")
    print("For example, 'one = Padic([1],0)' or 'Padic([1,1,0,0,1),-3)")
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



main()
