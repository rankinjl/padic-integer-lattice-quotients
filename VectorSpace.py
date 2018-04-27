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
        intlattice: boolean to represent if this vectorspace is actually
            an integer lattice (true: integer lattice, false: not integer lattice)
    '''

    #Pre: need to create a p-adic vector space with PadicVectors in the
        #spanning set
    #Post: p-adic vector space created
    def __init__(self, padicVectorsList,IntLattice=False):
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
        self.__intlattice = IntLattice
        self.__reducedSpan = self.__findReducedSpan(span)
              
        
    #Pre: need to calculate the vectors in the span in reduced echelon form
    #Post: vectors calculated and returned
    def __findReducedSpan(self, span):
        vectorsInMatrix = PadicMatrix(len(span),span[0].getRows(),span).getReducedEchelonForm(self.__intlattice)
        vectors = []
        length = vectorsInMatrix.getColumns()
        if(length>0):
            zero = PadicNumber([],0)
            zerovector = PadicVector([zero]*length)
            for row in range(vectorsInMatrix.getRows()):
                currentVector = []
                for col in range(length):
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
        if(not isinstance(other,VectorSpace) or self.isIntLattice()!=other.isIntLattice()):
            raise ValueError("Both objects must be the same type!")
        theseVectors = self.getReducedVectors()
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

    #Pre: need to know if this VectorSpace should be treated as an integer lattice
    #Post: if int lattice, return true. else return false
    def isIntLattice(self):
        return self.__intlattice

    #Pre: need to find the intersection between this VectorSpace and
        #otherVectorSpace
    #Post: intersection returned as a VectorSpace. If one or both are
        #integer lattices, the intersection will be an integer lattice
    def getIntersection(self, otherVectorSpace):
        if(not isinstance(otherVectorSpace,VectorSpace)):
            raise ValueError("otherVectorSpace should be a VectorSpace or IntegerLattice!")
        if(self.equals(otherVectorSpace)):
            return self
        otherVectors = otherVectorSpace.getReducedVectors()
        theseVectors = self.getReducedVectors()
        rows = otherVectors[0].getRows() 
        if(rows!=theseVectors[0].getRows()):
            raise ValueError("VectorSpaces must have vectors with the same number of entries!")
        columns = len(otherVectors)+len(theseVectors)
        matrix = PadicMatrix(rows,columns,theseVectors+otherVectors,False).getReducedEchelonForm()

        pivots,nonpivotCols = self.__getPivotLocations(matrix)
        
        nullSpaceVectors = [[]]*len(nonpivotCols)
        zero = PadicNumber([],0)
        one = PadicNumber([1],0)
        for i in range(len(nonpivotCols)):
            nullSpaceVectors[i] = [zero]*columns
            nullSpaceVectors[i][nonpivotCols[i]] = one
            for p in pivots:
                nullSpaceVectors[i][p[1]] = matrix.getValue(p[0],nonpivotCols[i]).getAdditiveInverse()

        lattice = self.__intlattice or otherVectorSpace.isIntLattice()
        if(lattice):
            #scale each nullSpaceVector by PadicNumber with smallest valuation
            for v in nullSpaceVectors:
                curmin = v[0].getPadicValuation()
                for i in range(len(v)):
                    other = v[i].getPadicValuation()
                    if(other<curmin):
                        curmin = other
                for i in range(len(v)):
                    v[i] = v[i].divide(PadicNumber([1],curmin))
        '''for i in nullSpaceVectors:
            for n in i:
                print(n)
            print()'''
        vectors = theseVectors
        flag = lattice and not self.isIntLattice()
        if(flag):
            #otherVectorSpace is lattice but this is not, so use other
            vectors = otherVectors
            
        intersectionVectors = []
        for vector in nullSpaceVectors:
            thisvector = []
            for j in range(rows):
                value = zero
                for i in range(len(vectors)):
                    if(flag):
                        value = value.add(vector[len(vector)-1-i].multiply(vectors[len(vectors)-1-i].getValue(j,0)))
                    else:
                        value = value.add(vector[i].multiply(vectors[i].getValue(j,0)))
                thisvector.append(value)
            intersectionVectors.append(PadicVector(thisvector))

        if(len(intersectionVectors)>0):
            return VectorSpace(self.__findReducedSpan(intersectionVectors),lattice)
        else:
            return VectorSpace([PadicVector([zero]*rows)],lattice)

    #Pre: need to get the locations with pivots in them
    #Post: pivot locations in matrix returned as a list of tuples of integers
    # second thing returned is non-pivot columns returned as list of integers
    def __getPivotLocations(self,matrix):
        rows = matrix.getRows()
        columns = matrix.getColumns()
        pivots = []
        nonpivots = []
        zero = PadicNumber([],0)
        for c in range(columns):
            pivot = (-1,-1)
            for r in range(rows):
                if(not matrix.getValue(r,c).equals(zero)):
                    if(pivot==(-1,-1) and not [item for item in pivots if item[0]==r]):
                        pivot = (r,c)
                    else:
                        #already have "pivot" but another nonzero
                        pivot = (-1,-1)
                        nonpivots.append(c)
                        break
            if(pivot!=(-1,-1)):
                pivots.append(pivot)
        return pivots,nonpivots


    #Pre: need to print this VectorSpace
    #Post: string describing VectorSpace returned
    def __str__(self):
        description = ""
        if(self.__intlattice):
            description = description + "Integer Lattice"
        else:
            description = description + "Vector Space"
        description = description + " spanned by:\n"
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

