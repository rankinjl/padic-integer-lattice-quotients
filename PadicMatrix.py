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
        #or valueListRowByRow is list of PadicMatrix(Vector)s that need to
        #be put in this matrix as rows (rows=True) or columns (rows=False)
    #Post: PadicMatrix created
    def __init__(self, rows, columns, valueListRowByRow=[],putInRows=True):
        if(not isinstance(rows,int) or rows<=0):
            raise ValueError("Rows = "+str(rows)+" is not a positive integer!")
        self.__rows = int(rows)
        if(not isinstance(columns,int) or columns<=0):
            raise ValueError("Columns = "+str(columns)+" is not a positive integer!")
        self.__columns = int(columns)
        if(len(valueListRowByRow)==0 or isinstance(valueListRowByRow[0],PadicNumber)):
            self.__values = self.__fillInValues(valueListRowByRow)
        elif(isinstance(valueListRowByRow[0],PadicMatrix)):
            if(putInRows):
                self.__values = self.__fillInVectorsByRow(valueListRowByRow)
            else:
                self.__values = self.__fillInVectorsByColumn(valueListRowByRow)
        else:
            raise ValueError("ValueList must be PadicMatrix/PadicVector or PadicNumbers!")


    #Pre: need to fill in this PadicMatrix with vectors from vectorList
        # so that each vector is a row in the matrix
    #Post: PadicMatrix illed in 
    def __fillInVectorsByRow(self,vectorList):
        if(not isinstance(vectorList,list) or len(vectorList)<=0):
            raise ValueError("Must be a list of vectors!")
        if(not isinstance(vectorList[0],PadicMatrix)):
            raise ValueError("The vectors must be PadicVector instances!")
        if(len(vectorList)!=self.__rows):
            raise ValueError("The number of vectors does not match the number of rows!")
        rowsAndCols = [[]]*self.__rows
        for row in range(self.__rows):
            currentVector = vectorList[row]
            if(not isinstance(currentVector,PadicMatrix) or currentVector.getColumns()!=1):
                raise ValueError("The vectors must be PadicVector instances!")
            if(self.__columns!=currentVector.getRows()):
                raise ValueError("All vectors must have the same number of entries!")
            rowsAndCols[row] = [0]*self.__columns
            for col in range(self.__columns):
                if(not isinstance(currentVector.getValue(col,0),PadicNumber)):
                   raise ValueError("Entries in vectors must be PadicNumbers!")
                rowsAndCols[row][col] = currentVector.getValue(col,0)
        return rowsAndCols

    #Pre: need to fill in this PadicMatrix with vectors from vectorList
        #so that each vector is a column in the matrix
    #Post: PadicMatrix filled in
    def __fillInVectorsByColumn(self,vectorList):
            if(not isinstance(vectorList[0],PadicMatrix)):
                raise ValueError("The vectors must be PadicVector instances!")
            if(len(vectorList)!=self.__columns):
                raise ValueError("The number of vectors does not match the number of columns!")
            rowsAndCols = [[]]*self.__rows
            for i in range(self.__rows):
                rowsAndCols[i] = [0]*self.__columns
            for i in range(self.__columns):
                currentVector = vectorList[i]
                if(not isinstance(currentVector,PadicMatrix) or currentVector.getColumns()!=1):
                    raise ValueError("The vectors must be PadicVector instances!")
                if(self.__rows!=currentVector.getRows()):
                    raise ValueError("All vectors must have the same number of entries!")
                for row in range(self.__rows):
                    if(not isinstance(currentVector.getValue(row,0),PadicNumber)):
                       raise ValueError("Entries in vectors must be PadicNumbers!")
                    rowsAndCols[row][i] = currentVector.getValue(row,0)
            return rowsAndCols

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
                    value = valueList[r*self.__columns+c]
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

    #Pre: need to make a deep copy of this PadicMatrix
    #Post: deep copy returned
    def copy(self):
        values = self.getValues()
        newValues = []
        for row in range(self.getRows()):
            for col in range(self.getColumns()):
                newValues.append(values[row][col].copy())
        return PadicMatrix(self.getRows(),self.getColumns(),newValues)

    #Pre: need to get the reduced echelon form of this PadicMatrix
    #Post: reduced echelon form calculated and returned
    def getReducedEchelonForm(self,intlattice=False):
        #make new Matrix object so not change self
        matrix = self.copy()
        #For each row:
            #put largest pivot (this vs underneath) in current row
            #if all zero beneath, skip to next col
            #use this pivot to zero entries beneath it
            #use this pivot to zero out entries above it
        pivotCol = 0
        pivotRow = 0
        #additionalRowsToCheck = []
        row = 0
        while(row<self.getRows() and pivotCol<self.getColumns()):
            curPivotRow = pivotRow
            curmax = matrix.getValue(row,pivotCol)
            #get the largest pivot in this pivot column
            for i in range(row+1,self.getRows()):
                #"largest" p-adic number is the largest absolute value
                if(matrix.getValue(i,pivotCol).getPadicAbsoluteValue()>curmax.getPadicAbsoluteValue()):
                    curmax = matrix.getValue(i,pivotCol)
                    #additionalRowsToCheck.append(curPivotRow)
                    curPivotRow = i
            if(curmax.getPadicAbsoluteValue()==0):
                pivotCol = pivotCol+1
            else:
                #move curPivotRow to pivotRow
                if(curPivotRow!=pivotRow):
                    matrix.swapRows(curPivotRow,pivotRow)
                #zero out all numbers beneath this pivot and above this pivot
                    #located at pivotCol, pivotRow with value curmax
                for i in range(self.getRows()):
                    if(i!=pivotRow):
                        value = matrix.getValue(i,pivotCol)
                        if(not value.equals(PadicNumber([],0))):
                            scalar = value.divide(curmax).getAdditiveInverse()
                            if(intlattice):
                                if(scalar.getPadicAbsoluteValue()<=1):
                                    #scalar is padic integer, so has additive inverse also integer => invertible
                                    matrix.addScalarRows(i,scalar,pivotRow)
                            else:
                                matrix.addScalarRows(i,scalar,pivotRow)
                
                if(intlattice):
                    scalar = PadicNumber([1],curmax.getPadicValuation()).divide(curmax)
                    matrix.scaleRow(pivotRow,scalar)
                else:
                    inverse = curmax.getMultiplicativeInverse()
                    matrix.scaleRow(pivotRow,inverse)
                pivotRow = pivotRow+1
                pivotCol = pivotCol+1
                row=row+1
           
        return matrix

    #Pre: need to do value*rowToUse+rowToManipulate = rowToManipulate
    #Post: row addition done
    def addScalarRows(self, rowToManipulate, value, rowToUse):
        if(not isinstance(rowToManipulate,int) or not isinstance(rowToUse,int) or not(isinstance(value,PadicNumber))):
            raise ValueError("rows must be integers and value must be PadicNumber!")
        if(rowToManipulate<0 or rowToManipulate>=self.getRows() or rowToUse<0 or rowToUse>=self.getRows() or value.equals(PadicNumber([0],0))):
            raise ValueError("rows must be in correct range and value cannot be zero!")
        thisrow = self.getValues()[rowToManipulate]
        useRow = self.getValues()[rowToUse]
        zero = PadicNumber([],0)
        for i in range(len(thisrow)):
            if(not useRow[i].equals(zero)):
                thisrow[i] = thisrow[i].add(useRow[i].multiply(value))
        self.getValues()[rowToManipulate] = thisrow

    #Pre: need to multiply row rowToScale by scalar
    #Post: row multiplied by scalar
    def scaleRow(self, rowToScale,scalar):
        if(not isinstance(rowToScale,int) or not(isinstance(scalar,PadicNumber))):
            raise ValueError("Row must be an integer and scalar must be PadicNumber!")
        if(rowToScale<0 or rowToScale>=self.getRows() or scalar.equals(PadicNumber([],0))):
            raise ValueError("rowToScale must be in correct range and scalar cannot be zero!")
        thisrow = self.getValues()[rowToScale]
        zero = PadicNumber([],0)
        for i in range(len(thisrow)):
            if(not thisrow[i].equals(zero)):
                thisrow[i] = thisrow[i].multiply(scalar)
        self.getValues()[rowToScale] = thisrow

    #Pre: need to swap two rows in matrix
    #Post: row a and row b swapped in matrix
    def swapRows(self, a, b):
        if(not isinstance(a,int) or not isinstance(b,int)):
            raise ValueError("a and b must be integers!")
        if(a<0 or b<0 or a>=self.getRows() or b>=self.getRows()):
            raise ValueError("a and be must be in the correct range!")
        temp = self.getValues()[a]
        self.getValues()[a] = self.getValues()[b]
        self.getValues()[b] = temp

    #Pre: need to see if this PadicMatrix and other are equivalent
    #Post: if equivalent, True returned. else, False returned
    def equals(self, other):
        if(not isinstance(other,PadicMatrix)):
            return False
        if(self.getRows()!=other.getRows() or self.getColumns()!=other.getColumns()):
            return False
        for row in range(len(self.__values)):
            for col in range(len(self.__values[row])):
                if(not other.getValue(row,col).equals(self.getValue(row,col))):
                    return False
        return True
    
    #Pre: need to print this p-adic matrix
    #Post: string describing p-adic matrix returned
    def __str__(self):
        description = "[\n"
        for r in range(self.__rows):
            description = description + " row "+str(r)+": [\n"
            for c in range(self.__columns):
                description = description +"\t\t"+str(self.__values[r][c])+"\n"
            description = description + "\t]\n"
        description = description + "]"
        return description
