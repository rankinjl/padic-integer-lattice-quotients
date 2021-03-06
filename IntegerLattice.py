#By Jessica Rankins Spring 2018
from VectorSpace import *
from PadicVector import *

class IntegerLattice(VectorSpace):
    """IntegerLattice: takes in one or more PadicVectors to specify the
        spanning vectors and allows diferent operations to be performed"""

    ''' private instance attributes for a IntegerLattice inherited from VectorSpace:
        spanningVectors: the list of PadicVectors that specify the spanning
            vectors for this vector space as given by the user
        reducedSpan: the list of PadicVectors that specify the spanning
            vectors for this vector space in reduced form
    '''

    #Pre: need to create a p-adic integer lattice with PadicVectors in the
        #spanning set
    #Post: p-adic integer lattice created
    def __init__(self, padicVectorsList):
        if(len(padicVectorsList)==0):
            raise ValueError("The list of PadicVectors must have at least one thing in it!")
        VectorSpace.__init__(self,padicVectorsList,True)
