#By Jessica Rankins Spring 2018
from PadicNumber import *
from PadicMatrix import *

class PadicVector(PadicMatrix):
    """PadicVector: holds p-adic numbers in a column vector and allows
    different operations to be done on this vector"""

    ''' private instance attributes for a PadicVector inherited from PadicMatrix:
        rows: the (integer) number of rows in the matrix
        columns: the (integer) number of columns in the matrix = 1
        values: the actual PadicNumbers in each row and column represented
            as an array of arrays
            [[]]
            [[]]
             :     
            [[]]
    '''

    #Pre: need to create a vector of p-adic numbers given in valueList
    #Post: PadicVector created
    def __init__(self,valueList):
        if(len(valueList)==0):
            raise ValueError("The list of values for the PadicVector must have something in it")
        PadicMatrix.__init__(self,len(valueList),1,valueList)

    
