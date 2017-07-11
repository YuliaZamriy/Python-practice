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

#%%

def f(a, b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    
    intersect = {i:f(d1[i],d2[i]) for i in d1 if i in d2}
    
    for i in d1.keys() ^ d2.keys():
        difference[i] = d1.get(i, d2.get(i))

    return (intersect, difference)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
dict_interdiff(d1, d2)

#%%

def f(i):
    return i + 2
def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    for i in L[:]:
        if g(f(i)) is False:
            L.remove(i)
    return -1 if not L else max(L)

# L = [0, -10, 5, 6, -4]
# L = [0, -10, -5, -6, -4]
# L = []
# L = [0, -10, 5, 5, -4]
L = [6, 5, 5]
print(applyF_filterG(L, f, g))
print(L)

#%%

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    aListf = []
    for i in aList:
        if not isinstance(i, list):
            aListf.append(i)
        else:
            for j in flatten(i):
                aListf.append(j)
    
    return(aListf)
    
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# aList = [[1,2,3],[4,5,6], [7], [8,9]]
# aList = [[1],2,3]
flatten(aList)

