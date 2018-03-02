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
    def __init__(self, padicVectorsList):
        span = []
        if(not isinstance(padicVectorsList,list)):
            raise ValueError("padicVectorsList must be a list!")
        if(len(padicVectorsList)>0):
            rows = padicVectorsList[0].getRows()
            for vector in padicVectorsList:
                if(not isinstance(vector,PadicVector)):
                    raise ValueError("You should only give the VectorSpace PadicVectors!")
                else:
                    if(rows!=vector.getRows()):
                        raise ValueError("All vectors should have the same number of entries")
                    span.append(vector)
        else:
            raise ValueError("You must give at least one basis vector!")

        self.__spanningVectors = span
        self.__reducedSpan = self.__findReducedSpan(span)
              
        
    #Pre: need to calculate the vectors in the span in reduced echelon form
    #Post: vectors calculated and returned
    def __findReducedSpan(self, span):
        vectorsInMatrix = PadicMatrix(len(span),span[0].getRows(),span).getReducedEchelonForm()
        vectors = []
        length = vectorsInMatrix.getRows()
        if(length>0):
            zero = PadicNumber([],0)
            zerovector = PadicVector([zero]*length)
            for row in range(length):
                currentVector = []
                for col in range(vectorsInMatrix.getColumns()):
                    currentVector.append(vectorsInMatrix.getValue(row,col))
                vector = PadicVector(currentVector)
                if(not vector.equals(zerovector)):
                    vectors.append(vector)
        if(len(vectors)<=0):
            vectors.append(zerovector)
        return vectors

    #Pre: need to see if this VectorSpace is equivalent to other
    #Post: if equivalent, True returned. else, False returned
    def equals(self, other):
        if(not isinstance(other,VectorSpace)):
            raise ValueError("Both objects must be VectorSpaces!")
        theseVectors = []
        for vector in self.getReducedVectors():
            theseVectors.append(vector.copy())
        otherVectors = []
        for vector in other.getReducedVectors():
            otherVectors.append(vector.copy())
        if(len(theseVectors)==len(otherVectors)):
            for vector in theseVectors:
                removed = False
                for otherVector in otherVectors:
                    if(vector.equals(otherVector)):
                        otherVectors.remove(otherVector)
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
        if(self.equals(otherVectorSpace)):
            return self
        otherVectors = otherVectorSpace.getReducedVectors()
        theseVectors = self.getReducedVectors()
        matrix = PadicMatrix(otherVectors+theseVectors,False).getReducedEchelon()

        #get list of free columns without pivots
        #for each free variable/column:
            #make vector of values corresponding to this variable
            #with this vector, plug values in for first len(span) vectors
        
       #TODO


    #Pre: need to print this VectorSpace
    #Post: string describing VectorSpace returned
    def __str__(self):
        description = "Vector Space spanned by:\n"
        vectors = self.getVectors()
        for v in range(len(vectors)):
            description = description + "vector "+str(v)+":\n"+str(vectors[v])+"\n"
        return description
        
    #Pre: need to get the reduced spanning vectors for this VectorSpace
    #Post: reduced spanning vectors returned
    def getReducedVectors(self):
        return self.__reducedSpan  

    #Pre: need to get the spanning vectors for this VectorSpace as given
    #Post: spanning vectors returned
    def getVectors(self):
        return self.__spanningVectors

