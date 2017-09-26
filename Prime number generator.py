# -*- coding: utf-8 -*-
"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls 
to its next() method: 2, 3, 5, 7, 11, ...

Hint: Have the generator keep a list of the primes it's generated. 
A candidate number x is prime if (x % p) != 0 for all earlier primes p

@author: yzamriy
"""

def genPrimes():
    
    """ Initialize the first prime number and add it to a list"""
    x = 2
    p = [x]
    
    """ Yield first prime number with first call to next() """
    yield x
    
    while True:

        """ With each run through the while loop increment x by 1"""

        x += 1

        """ Initiate control flag with True """
        is_Prime = True

        """ If the number doesn't pass prime number check, 
            set control flag to False and break the loop 
        """
        for i in p:
            if x%i == 0:
                is_Prime = False
                break
        
        """ If the number retained control flag at True, it's real prime
            Append it to the list of primes, and yield it
        """
        if is_Prime:
            p.append(x)
            yield x


primes = genPrimes()