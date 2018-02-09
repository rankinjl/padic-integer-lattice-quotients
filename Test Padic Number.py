#By Jessica Rankins Spring 2018
from PadicNumber import *
'''
#Checking prime detection
try:
    neg_base = PadicNumber(-3,10,[],0)
except ValueError as e:
    print(e)
try:
    zero_base = PadicNumber(0,10,[],0)
except ValueError as e:
    print(e)
try:
    one_base = PadicNumber(1,10,[],0)
except ValueError as e:
    print(e)
try:
    four_base = PadicNumber(4,10,[],0)
except ValueError as e:
    print(e)
#only shows 9 precision!
zero_base3 = PadicNumber(3,10,[],0)
print(zero_base3)
'''
'''
#Checking precision detection
try:
    neg_precision = PadicNumber(3,-3,[],0)
except ValueError as e:
    print(e)
try:
    zero_precision = PadicNumber(2,0,[],0)
except ValueError as e:
    print(e)
'''
'''
#checking coefficient placement
two_base3 = PadicNumber(3,10,[2],0)
print(two_base3)
seven_base2 = PadicNumber(2,10,[1,1,1],0)
print(seven_base2)
eight_base2 = PadicNumber(2,10,[1],3)
print(eight_base2)
leading_zeros = PadicNumber(2,10,[0,0,1,0,1],5)
print(leading_zeros)
all_zeros = PadicNumber(2,10,[0,0,0],1)
print(all_zeros)
try:
    coefficient_over_p = PadicNumber(2,10,[0,1,4,0,1],1)
    print(coefficient_over_p)
except ValueError as e:
    print(e)
approximated = PadicNumber(2,5,[1,1,1,1,1,1,1,0,1],0)
print(approximated) #cuts off later coefficients
'''
'''
#check adding and additive inverses
seven_base2 = PadicNumber(2,10,[1,1,1],0)
six_base2 = PadicNumber(2,10,[1,1],1)
print(six_base2.add(seven_base2))
print()
zero_base3 = PadicNumber(3,10,[],0)
print(zero_base3.getAdditiveInverse())
print(zero_base3.add(zero_base3.getAdditiveInverse()))
print()
two_base3 = PadicNumber(3,10,[2],0)
print(two_base3.getAdditiveInverse())
print(two_base3.getAdditiveInverse().add(two_base3))
print()
six_base2 = PadicNumber(2,10,[0,1,1],0)
two_base3 = PadicNumber(3,8,[2],0)
print(six_base2.add(two_base3))

seven_base2 = PadicNumber(2,30,[1,1,1],0)
print(seven_base2)
'''
'''
#check multiplying
seven_base2 = PadicNumber(2,10,[1,1,1],0)
six_base2 = PadicNumber(2,10,[1,1],1)
print(six_base2.multiply(seven_base2))
print()
zero_base3 = PadicNumber(3,10,[],0)
print(zero_base3.multiply(zero_base3))
print()
two_base3 = PadicNumber(3,10,[2],0)
print(two_base3.multiply(two_base3))
print(two_base3.multiply(zero_base3))
print()
sixteen_base5 = PadicNumber(5,2,[1,3],0)
ninePointEight_base5 = PadicNumber(5,6,[4,4,1],-1)
print(sixteen_base5.multiply(ninePointEight_base5))
neg_one = PadicNumber(3,10,[1],0).getAdditiveInverse()
print(neg_one)
print(neg_one.multiply(neg_one))
'''
#check division and multiplicative inverses
