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

        """ With each run through the while initialize a list to hold remainder from each division"""
        control = []

        """ Divide current x by each element of the prime list and store the remainder in the control list """
        for i in p:
            control.append(x%i)
        
        """ If control list doesn't contain any zeroes
            (x divides by all previously generated prime numbers with non-zero remainder)
            x is a prime number. Yield this new prime number with call to next()
        """
        if min(control) > 0:
            p.append(x)
            yield x

primes = genPrimes()