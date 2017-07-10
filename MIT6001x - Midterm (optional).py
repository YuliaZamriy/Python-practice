from math import log

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    e1 = int(log(num,base))
    e2 = e1 + 1
    return e1 if abs(base**e1 - num) <= abs(base**e2 - num) else e2

#   Solution version #1:
#   e = int(log(num,base))
#   min_e = {}
#   for i in (e-1,e, e+1):
#       min_e[i] = (abs(base**i - num), base**i - num)
#   return min(min_e, key=min_e.get)

#closest_power(82, 1)
print(closest_power(20, 210.0))

#%%

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    product = 0
    for i, j in zip(listA, listB):
        product += i*j
    return product

listA = [1, 2, 3] 
listB = [4, 5, 6]
dotProduct(listA, listB)

#%%

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in L[::-1]:
        L.remove(i)
        L.append(i[::-1])
    
#L = [[1, 2], [3, 4], [5, 6, 7]]
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)
