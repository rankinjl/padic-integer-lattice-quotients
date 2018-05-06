#By Jessica Rankins Spring 2018
import copy
import math

class PadicNumber:
    """PadicNumber: holds information pertaining to a p-adic number and
    allows different operations to be done with this number"""

    ''' private class attributes for PadicNumber:
        prime: the (integer, prime) base p for the padic number
        precision: the (integer) number of "digits" to keep track of in this padic
            number starting from the smallest power with non-zero coefficient
    '''
    ''' private instance attributes for a padic number:
        smallestPower: the smallest integer power in the padic number 
            containing a non-zero coefficient
        coefficients: the actual integers in front of the p^i terms starting
            with the smallest power coefficients and working up, each
            having 0,1,...(p-1) values
    '''

    @classmethod
    #Pre: need to set the prime and precision for this session of padics
    #Post: prime and precision set
    def setPrimePrecision(cls, prime, precision):
        cls.__prime = prime
        cls.__precision = precision
        print("Set!")

    #Pre: create a p-adic number with precision places starting with the
        #first non-zero coefficient in coefficientList corresponding to
        #the coefficient on the smallestPower
    #Post: p-adic number created
    def __init__(self, coefficientList, smallestPower):
        if(not isinstance(smallestPower,int)):
            raise ValueError(str(smallestPower)+" is not an integer power!")
        for coefficient in coefficientList:
            if(not isinstance(coefficient,int) or coefficient>=self.__prime or coefficient<0):
                #print(coefficientList)
                raise ValueError("Coefficient(s) are not in the range 1,...,(p-1) for prime p!")
        self.__coefficients = self.__fillInCoefficients(coefficientList, smallestPower)

    #Pre: need to assign the coefficients for this padic number from the
        #coefficientList starting at smallestPower
    #Post: coefficients for this padic number are set
    def __fillInCoefficients(self, coefficientList, smallestPower):
        coefficients = {} #dictionary with keys as exponents and values
                            #as the corresponding coefficients
        index = 0 #corresponds to smallest power
        currentPower = smallestPower
        numberSkipped = 0
        if(len(coefficientList)>0):
            while(index<len(coefficientList) and coefficientList[index]==0):
                #change smallest power if zero coefficient
                index = index+1
                numberSkipped = numberSkipped+1
                currentPower = currentPower+1
            if(index==len(coefficientList)):
                #all zeros in the coefficientList
                currentPower = smallestPower
            self.__smallestPower = currentPower
            while(index<len(coefficientList) and self.__precision!=(index-numberSkipped)):
                coefficients[currentPower] = coefficientList[index]
                index = index+1
                currentPower = currentPower+1
            if(currentPower == smallestPower):
                #all zeros in coefficientList
                index = 0
        else: #want all zeros
            self.__smallestPower = smallestPower
        if(self.__precision!=(index-numberSkipped)): #went through all coefficients
            #fill remaining coefficients with 0s
            while(len(coefficients)<self.__precision):
                coefficients[currentPower] = 0
                currentPower = currentPower+1
        return coefficients

    #Pre: need to get a deep copy of this PadicNumber
    #Post: deep copy returned
    def copy(self):
        newcoefs = []
        originals = self.getCoefficients()
        for i in range(len(originals)):
            newcoefs.append(originals[self.getSmallestPower()+i])
        return PadicNumber(newcoefs,self.getSmallestPower())

    #Pre: need to get the absolute value of this p-adic number
    #Post: p-adic absolute value returned
    def getPadicAbsoluteValue(self):
        if(self.__zero()):
            return 0
        else:
            return self.__prime**(-self.__smallestPower)

    #Pre: need to get the p-adic valuation of this p-adic number
    #Post: p-adic valuation returned
    def getPadicValuation(self):
        if(self.__zero()):
            return math.inf
        else:
            return self.__smallestPower

    #Pre: need the precision of the p-adic number
    #Post: precision returned
    def getPrecision(self):
        return self.__precision

    #Pre: need the prime for this p-adic number
    #Post: prime returned
    def getPrime(self):
        return self.__prime

    #Pre: need the smallest exponent of the p-adic number
    #Post: smallest power (aka exponent) returned
    def getSmallestPower(self):
        return self.__smallestPower

    #Pre: need the list of coefficients of the p-adic number
    #Post: coefficients returned with keys as exponents, values as coefficients
    def getCoefficients(self):
        return self.__coefficients

    #Pre: need to check if these this PadicNumbers is a zero
    #Post: true returned if zero, false otherwise
    def __zero(self):
        these = self.getCoefficients()
        smallest = self.getSmallestPower()
        zero = True
        for i in range(len(these)):
            if(these[smallest+i]!=0):
                zero = False
        return zero

    #Pre: need to check if these two PadicNumbers are zero
    #Post: true returned if both zeros, false otherwise
    def __zeros(self, other):
        these = self.getCoefficients()
        others = other.getCoefficients()
        smallest = self.getSmallestPower()
        othersmallest = other.getSmallestPower()
        
        #check if they are both zero
        zero = True
        for i in range(len(these)):
            if(these[smallest+i]!=0):
                zero = False
        if(zero):
            for i in range(len(others)):
                if(others[othersmallest+i]!=0):
                    zero = False
        return zero

    #Pre: need to see if this PadicNumber is equivalent to other
    #Post: if equivalent, True returned. else, False returned
    def equals(self, other):
        if(not isinstance(other,PadicNumber)):
            return False
        if(self.getPrime()!=other.getPrime() or self.getPrecision()!=other.getPrecision()):
            return False
        if(self.__zeros(other)):
            return True
        these = self.getCoefficients()
        others = other.getCoefficients()
        smallest = self.getSmallestPower()
        othersmallest = other.getSmallestPower()
        if(smallest!=othersmallest):
            return False
        for i in range(len(these)):
            if(these[smallest+i]!=others[smallest+i]):
                return False
        return True

    #Pre: need to print this p-adic number
    #Post: string describing p-adic number returned
    def __str__(self):
        p = str(self.__prime)
        description = p+"-adic Number:"
        for exponent,coef in self.__coefficients.items():
            description = description+" "+str(coef)+"*"+str(p)+"^"+str(exponent)
        return description

    #Pre: need to know the additive inverse of this padic number
    #Post: additive inverse of padic number returned
    def getAdditiveInverse(self):
        newCoefficients = []
        currentPower = self.__smallestPower
        try:
            coefficient = self.__coefficients[currentPower] 
            if(coefficient == 0):
                #the padic number must be all zeros
                return PadicNumber(newCoefficients,currentPower)
            else:
                newCoefficients.append(self.__prime - coefficient)
        except KeyError:
            pass

        currentPower = currentPower + 1
        try:
            while((currentPower - self.__smallestPower)<self.__precision):
                newCoefficients.append(self.__prime - self.__coefficients[currentPower] - 1)
                currentPower = currentPower + 1
        except KeyError:
            pass
        return (PadicNumber(newCoefficients, self.__smallestPower))
       
    #Pre: need to know the multiplicative inverse of this padic number
    #Post: multiplicative inverse of this padic number returned
    def getMultiplicativeInverse(self):
        newCoefficients = []
        p = self.__prime
        theseCoefficients = self.__coefficients
        currentPower = self.__smallestPower
        newSmallestExponent = 0 - currentPower
        carry = 0
        if(self.__zero()):
            #this number is 0, so it does not have a multiplicative inverse
            raise ZeroDivisionError("The multiplicative inverse of 0 does not exist!")
        else:
            thisFirstTermInverse = (theseCoefficients[currentPower]**(p-2))%p
            newCoefficients.append(thisFirstTermInverse)
            carry = (thisFirstTermInverse*theseCoefficients[currentPower])//p

            #find rest of coefficients to multiply to 0
            for i in range(self.__precision-1):
                newnumber = 0
                currentPower = self.__smallestPower+1
                for newcoef in range(len(newCoefficients)):
                    newnumber = newnumber - theseCoefficients[currentPower]*newCoefficients[len(newCoefficients)-1-newcoef]
                    currentPower = currentPower+1
                newnumber = (newnumber-carry)
                goingToAdd = (newnumber*thisFirstTermInverse)%p
                carry = (goingToAdd*theseCoefficients[self.__smallestPower]-newnumber)//p
                newCoefficients.append(goingToAdd)
        return PadicNumber(newCoefficients,newSmallestExponent)

    #Pre: need to find the padic number resulting from the addition of
        #this padic number and other
    #They must be in the same base and the precision will be the
        #larger of the two
    #Post: this padic number and other are added and the sum is returned
    def add(self, other):
        if(not isinstance(other,PadicNumber)):
            raise ValueError("You must add two PadicNumbers!")
        smallestPower = min(other.getSmallestPower(),self.getSmallestPower())
        p = self.__prime
        totalprecision = self.getPrecision()*2
        currentPower = smallestPower
        otherCoefficients = other.getCoefficients().copy()
        thisCoefficients = self.getCoefficients().copy()
        newCoefficients = []
        carry = 0
        index = 0
        
        while((otherCoefficients or thisCoefficients) and index<totalprecision):
            #while at least one of the dictionaries is not empty
            try:
                othernum = otherCoefficients[currentPower]
                otherCoefficients.pop(currentPower)
            except KeyError as e:
                othernum = 0
            try:
                thisnum = thisCoefficients[currentPower]
                thisCoefficients.pop(currentPower)
            except KeyError as e:
                thisnum = 0

            newnum = othernum+thisnum+carry
            if(newnum>=p):
                carry = newnum//p
                newnum = newnum%p
            else:
                carry = 0
            newCoefficients.append(newnum)
            currentPower = currentPower+1
            index = index+1
        while(carry!=0):
            newCoefficients.append(carry%p)
            carry = carry//p
        while(len(newCoefficients)>0 and newCoefficients[0] == 0):
            newCoefficients.remove(0)
            smallestPower = smallestPower +1
        return PadicNumber(newCoefficients,smallestPower)
            
    #Pre: need to subtract other from self
    #Post: self-other returned
    def subtract(self, other):
        if(not isinstance(other,PadicNumber)):
            raise ValueError("You must subtract two PadicNumbers!")
        return self.add(other.getAdditiveInverse())


    #Pre: need to multiply this padic number to other
    #They must be in the same base and the precision will be the
        #larger of the two
    #Post: the product of this and other is returned
    def multiply(self, other):
        if(not isinstance(other,PadicNumber)):
            raise ValueError("You must multiply two PadicNumbers!")
        p = self.__prime
        smallestExponent = self.getSmallestPower()+other.getSmallestPower()
        currentPower = smallestExponent
        carry = 0
        newCoefficients = []

        #newCoefficients[index] will consist of index+1 addends
        for i in range(self.__precision):
            currentCoefficient = 0
            selfCurrentPower = self.getSmallestPower()
            #must have i+1 terms starting with self's smallestExponent
            for j in range(i+1): #0,...,i
                try:
                    selfnum = self.getCoefficients()[selfCurrentPower]
                except KeyError:
                    selfnum = 0
                try:
                    othernum = other.getCoefficients()[currentPower-selfCurrentPower]
                except KeyError:
                    othernum = 0
                currentCoefficient = currentCoefficient+(selfnum*othernum)
                selfCurrentPower = selfCurrentPower+1

            currentCoefficient = currentCoefficient + carry
            carry = currentCoefficient//p    
            newCoefficients.append(currentCoefficient%p)    
            currentPower = currentPower+1

        return PadicNumber(newCoefficients,smallestExponent)
            
    #Pre: need to divide self by other
    #Post: self/other returned
    def divide(self, other):
        if(not isinstance(other,PadicNumber)):
            raise ValueError("You must divide two PadicNumbers!")
        return self.multiply(other.getMultiplicativeInverse())
