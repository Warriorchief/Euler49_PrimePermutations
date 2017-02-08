#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 16:21:17 2017

@author: christophergreen

Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
 is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the
 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
"""


#1)ASSEMBLE ALL 3-TERM ARITHMETIC SEQS WHERE THIRD TERM IS UNDER 1000 AND ALL TERMS ARE PRIME
#2)CHECK EACH OF THESE TO SEE WHETHER ALL 3 ITEMS ARE PERMS OF ONE ANOTHER

import math

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def list_primes(max):
    primes=[]; 
    j=2
    while j<=max:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;
    
def is_permutation(x,y):
    if len(str(x))!=len(str(y)):
        return False
    chars=[];
    i=0;
    while i<len(str(x)):
        chars.append(str(x)[i]);
        i+=1;
    #print("from",x,"we have made the chars",chars);
    j=0;
    while j<len(str(y)):
        if str(y)[j] in chars:
            del chars[chars.index(str(y)[j])];  #find the first instance of the char in str(x) and deletes it
        else:
            return False;
        j+=1;
    #print("having removed matches one at a time, x still has the chars:",chars);
    if len(chars)==0:
        return True;
    else:
        return False;
      
def assemble_and_find():
    poss=[];
    i=1001
    while i<9998:
        step=1;
        while True:
            if (i+(2*step))<10000:
                poss.append([i,i+step,i+2*step]);
                step+=1;
            else:
                break;
        i+=2;
    print("length of poss is",len(poss)); #--> 10122750  that is, over ten million
    bett=[];
    j=0;
    while j<10122750:
        if is_prime(poss[j][0]) and is_prime(poss[j][1]) and is_prime(poss[j][2]):
            bett.append(poss[j]);
        j+=1
    print("length of bett is",len(bett)); #--> 42994
    answ=[];
    k=0;
    while k<42994:
        if is_permutation(bett[k][0],bett[k][1]) and is_permutation(bett[k][1],bett[k][2]):
            answ.append(bett[k]);
        k+=1
    print("the",len(answ),"triplets that work are:",answ); #-->[[1487, 4817, 8147], [2969, 6299, 9629]]
    return answ;

output=assemble_and_find();

#this makes the concat string 296962999629 CORRECT
  
