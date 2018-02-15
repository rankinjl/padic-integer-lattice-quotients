#By Jessica Rankins Spring 2018
from PadicVector import *

class VectorSpace:
    """VectorSpace: takes in one or more PadicVectors to specify the
        spanning vectors and allows different operations to be performed"""

    ''' private instance attributes for a VectorSpace:
        spanningVectors: the list of PadicVectors that specify the spanning
            vectors for this vector space as given by the user
        reducedSpan: the list of PadicVectors that specify the spanning
            vectors for this vector space in reduced form
    '''

    #Pre: need to create a p-adic vector space with PadicVectors in the
        #spanning set
    #Post: p-adic vector space created
    def __init__(self, *padicVectors):
        span = []
        if(len(padicVectors)>0):
            rows = padicVectors[0].getRows()
            for vector in padicVectors:
                if(not isinstance(vector,PadicVector)):
                    raise ValueError("You should only give the VectorSpace PadicVectors!")
                else:
                    if(rows!=vector.getRows()):
                        raise ValueError("All basis vectors should have the same number of entries")
                    span.append(vector)
        else:
            raise ValueError("You must give at least one basis vector!")

        self.__spanningVectors = span
        self.__reducedSpan = self.__findReducedSpan(span)
              
        
    #Pre: need to calculate the vectors in the span in reduced echelon form
    #Post: vectors calculated and returned
    def __findReducedSpan(self, span):
        vectorsInMatrix = PadicMatrix(span).getReducedEchelonForm()
        vectors = []
        length = 1
        if(len(vectorsInMatrix)>0):
            length = vectorsInMatrix[0].getRows()
            zero = PadicVector([0]*length)
            for vector in vectorsInMatrix:
                if(not vector.equals(zero)):
                    vectors.append(PadicVector(vector))
        if(len(vectors)<=0):
            vectors.append(PadicVector([0]*length))
        return vectors

    #Pre: need to see if this VectorSpace is equivalent to other
    #Post: if equivalent, True returned. else, False returned
    def equals(self, other):
        if(not isinstance(other,VectorSpace)):
            return False
        theseVectors = self.getReducedVectors()
        otherVectors = other.getReducedVectors()
        if(len(theseVectors)==len(otherVectors)):
            for vector in theseVectors:
                removed = False
                for other in otherVectors:
                    if(vector.equals(other)):
                        otherVectors.remove(other)
                        removed = True
                if(not removed):
                    return False
            return True
        return False

    #Pre: need to find the intersection between this VectorSpace and
        #otherVectorSpace
    #Post: intersection returned as a VectorSpace
    def getIntersection(self, otherVectorSpace):
        if(not isinstance(otherVectorSpace,VectorSpace)):
            raise ValueError("You should only intersect a VectorSpace with another VectorSpace")
        otherVectors = otherVectorSpace.getBasisVectors()
        theseVectors = self.getBasisVectors()
       #TODO
        
    #Pre: need to get the reduced spanning vectors for this VectorSpace
    #Post: reduced spanning vectors returned
    def getReducedVectors(self):
        return self.__reducedSpan  

    #Pre: need to get the spanning vectors for this VectorSpace as given
    #Post: spanning vectors returned
    def getVectors(self):
        return self.__spanningVectors

