#By Jessica Rankins Spring 2018
from PadicNumber import *

class PadicMatrix:
    """PadicMatrix: holds p-adic numbers in an nxm matrix and allows
    different operations to be done on this matrix"""

    ''' private instance attributes for a PadicMatrix:
        rows: the (integer) number of rows in the matrix
        columns: the (integer) number of columns in the matrix
        values: the actual PadicNumbers in each row and column represented
            as an array of arrays
            []->[],[],...,[]
            []->[],[],...,[]
            :       :     
            []->[],[],...,[]
    '''

    #Pre: need to create a rowsXcolumns matrix of p-adic numbers given by
        #valueListRowByRow (listed as row1 elements followed by row2, etc)
    #Post: PadicMatrix created
    def __init__(self, rows, columns, valueListRowByRow=[]):
        if(not isinstance(rows,int) or rows<=0):
            raise ValueError("Rows = "+str(rows)+" is not a positive integer!")
        self.__rows = int(rows)
        if(not isinstance(columns,int) or columns<=0):
            raise ValueError("Columns = "+str(columns)+" is not a positive integer!")
        self.__columns = int(columns)
        self.__values = self.__fillInValues(valueListRowByRow)

    #Pre: need to create a matrix of PadicVectors given by vectorListForRows
        #so that each vector in vectorListForRows is a row in the matrix
    #Post: PadicMatrix created
    def __init__(self, vectorListForRows):
        if(not isinstance(vectorListForRows,list) or len(vectorListForRows)<=0):
            raise ValueError("Must be a list of vectors!")
        self.__rows = len(vectorListForRows)
        if(not isinstance(vectorListForRows[0],PadicVector)):
                raise ValueError("The vectors must be PadicVector instances!")
        self.__columns = vectorListForRows[0].getRows()
        rowsAndCols = [[]]*self.__rows
        #rowsAndCols[r][c] = vectorListForRows[r][c]
        for row in self.__rows:
            currentVector = vectorListForRows[row]
            if(not isinstance(currentVector,PadicVector)):
                raise ValueError("The vectors must be PadicVector instances!")
            if(self.__columns!=currentVector.getRows()):
                raise ValueError("All vectors must have the same number of entries!")
            rowsAndCols[row] = [0]*self.__columns
            for col in len(currentVector):
                if(not isinstance(currentVector[col],PadicNumber)):
                   raise ValueError("Entries in vectors must be PadicNumbers!")
                rowsAndCols[row][col] = currentVector[col]
        self.__values = rowsAndCols

    #Pre: need to fill in the values for this PadicMatrix given in valueList
    #Post: values assigned
    def __fillInValues(self,valueList):
        rowsAndCols = [[]]*self.__rows
        if(len(valueList)==0):
            #fill in with zeros
            for r in range(self.__rows):
                rowsAndCols[r] = [PadicNumber([],0)]*self.__columns
        elif(len(valueList)!=(self.__rows*self.__columns)):
            raise ValueError("The number of values does not match the number of entries in the matrix!")
        else:
            #fill in rowsAndCols with valueList values where
            #rowsAndCols[r][c] = valueList[(r-1)*self.__columns+c]
            for r in range(self.__rows):
                rowsAndCols[r] = [0]*self.__columns
                for c in range(self.__columns):
                    value = valueList[(r-1)*self.__columns+c]
                    if(not isinstance(value,PadicNumber)):
                        raise ValueError("Values must be PadicNumbers!")
                    rowsAndCols[r][c] = value
        return rowsAndCols

    #Pre: need to get the value at this row and this column
    #Post: value at row row and column column returned
    def getValue(self, row, column):
        return self.__values[row][column]

    #Pre: need to get all the values in this PadicMatrix
    #Post: list of lists containing the values returned accessed [r][c]
    def getValues(self):
        return self.__values

    #Pre: need to get the number of rows in this PadicMatrix
    #Post: number of rows returned
    def getRows(self):
        return self.__rows

    #Pre: need to get the number of columns in this PadicMatrix
    #Post: number of columns returned
    def getColumns(self):
        return self.__columns

    #Pre: need to get the reduced echelon form of this PadicMatrix
    #Post: reduced echelon form calculated and returned
    def getReducedEchelonForm(self):
        return self.__values
        #TODO

    #Pre: need to see if this PadicMatrix and other are equivalent
    #Post: if equivalent, True returned. else, False returned
    def equals(self, other):
        if(not isinstance(other,PadicMatrix)):
            return False
        for row in self.__values:
            for col in self.__values[row]:
                if(not other.getValue(row,col).equals(self.getValue(row,col))):
                    return False
        return True
    
    #Pre: need to print this p-adic matrix
    #Post: string describing p-adic matrix returned
    def __str__(self):
        description = "[\n"
        for r in range(self.__rows):
            description = description + " row "+str(r+1)+": [\n"
            for c in range(self.__columns):
                description = description +"\t\t"+str(self.__values[r][c])+"\n"
            description = description + "\t]\n"
        description = description + "]"
        return description
