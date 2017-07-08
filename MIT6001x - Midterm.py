# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation of integers starting from 1. 
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    
    if k == 1:
        return True
    
    i = 2
    j = 1
    
    while j < k:
        j = j + i
        if j == k:
            return True
        elif j > k:
            return False
        else:
            i += 1

print(is_triangular(10))

#%%

s = "This is great!"
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sNoVow = s
    
    for vow in vowels:
        if vow in s:
             sNoVow = sNoVow.replace(vow, '', sNoVow.count(vow))
    
    print(sNoVow)

print_without_vowels(s)


#%%

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    vowels =  ['a', 'e', 'i', 'o', 'u']
    
    sNoVow = s
    
    for letter in s:
        if letter in vowels or letter.lower() in vowels:
            sNoVow = sNoVow.replace(letter, '', sNoVow.count(letter))
    
    print(sNoVow)

print_without_vowels(s)
print_without_vowels('')
print_without_vowels('a')
print_without_vowels('b')
print_without_vowels('aaaa')
print_without_vowels('bbbb')
print_without_vowels('abab')
print_without_vowels('bababa')
print_without_vowels('Hello, testing capital letters')
print_without_vowels("aNd, nOW! I'm --so-- t35t1n@ those special chars!!")
print_without_vowels('Here is a simple sentence that makes sense. BYE.')

#%%

def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    """
    
    l = []
    for i in set(L):
        if L.count(i) % 2 > 0:
            l.append(i)
    
    if l:
        return max(l)

print(largest_odd_times([2,2,4,4]))

#%%

d = {1:10, 2:20, 3:30}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    new_d = {}

    for k, v in zip(d.keys(), d.values()):
        if v not in new_d:
            new_d[v] = [k]
        else:
            new_d[v].append(k)
            new_d[v].sort()
        
    return new_d
    
dict_invert(d)

#%%

def general_poly (L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    def inside(x):
        result = 0
        pwr = len(L) - 1
        for l in L:
            result = result + l * x ** pwr
            pwr -= 1
        return result
    return inside
    
    
general_poly([1, 2, 3, 4])(10)

#%%

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']

L1 = ['a', 'a', 'b'] 
L2 = []

L1 = [] 
L2 = []

#%%

## Submitted version

L1 = [] 
L2 = []

def create_dict(L):
    
    d = {}
    for l in L:
        d[l] = L.count(l)
    return d

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    if not L1 and not L2:
        return (None, None, None)
    
    if create_dict(L1) == create_dict(L2):
        
        max_el = 0
        max = 0 
        
        for i in create_dict(L1):
            if create_dict(L1)[i] > max:
                max_el = i
                max = create_dict(L1)[i]
        return (max_el, max, type(max_el))
    else:
        return False

print(is_list_permutation(L1, L2))


