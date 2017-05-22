#!/usr/bin/python
# coding: utf-8

import math
import numpy as np
import sys
# Just need this for debugging
import time

def isprime(n):
    """ Checks to see if n is prime or not"""
    l=int(math.ceil(math.sqrt(n)))
    primeBool=True
    for factors in range(2,l+1):
        if n%factors==0:
            primeBool=False
    if n==1:
        primeBool=False
    if n==2:
        primeBool=True
    return primeBool


def getFactors(n):
    """Get a list of factors of n (up to srt(n))"""
    factorList=[]
    l=int(math.ceil(math.sqrt(n)))
    for factors in range(2,l+1):
        if n%(factors)==0:
            factorList.append(factors)
    return factorList

def getAllFactors(n):
    """Get a list of factors of n
    Does not include 1 and n
     """
    factorList=[]
    for factors in range(2, n):
        if n%factors == 0:
            factorList.append(factors)
    return factorList


def countAllFactors(n):
    """Merely counts all factors
    of n. This is faster than
    listing them, especially for
    large n
     """
    factorCount=0
    l=int(math.ceil(math.sqrt(n)))
    for factors in range(2, l+1):
        if n%factors == 0:
            factorCount+=1
    # Add 1 (or n)
    factorCount+=1
    # Double for full factors
    factorCount*=2
    # If n is square, then remove one of the dupes
    if n==pow(l,2):
            factorCount-=1
    return factorCount


##################################################
# Problem 2
##################################################

def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#fibonacci(31) is the largest term less than 4 million
#for r in range(32):
#    if fibonacci(r)%2==0:
#        summa+=fibonacci(r)

##################################################

##################################################
# Problem 4
##################################################

def isPalindrome(n):
    nStr=str(n)
    nHalf = int(math.ceil(1.0*len(nStr)/2))
    lStr = nStr[0:nHalf]
    rStr = nStr[-nHalf:]
    revStr = rStr[::-1]
    if lStr == revStr:
        return True
    else:
        return False

# Range for three digit numbers
def getMaxPalindrome(n):
    maxPalindrome=0
    for a in range(n,100,-1):
        for b in range(n,100,-1):
            if isPalindrome(a*b):
                if a*b > maxPalindrome:
                    maxPalindrome=a*b
    return maxPalindrome


##################################################

##################################################
# Problem 5
##################################################

def isEvenlyDivisible(n,r):
    evenlyDivisible = True
    for a in range(r):
        if n%(a+1) != 0:
            evenlyDivisible= False
    return evenlyDivisible

## nmin=69672960; the smallest possible even divisor from 1 to 20 (product of all
## the primes)
#nmin=69672960
#for m in range(nmin, 6*nmin/5):
#    if isEvenlyDivisible(m,20):
#        print(m)



##################################################

##################################################
# Problem 6
##################################################

def sumSquares(n):
    summa = 0
    for a in range(n):
        summa += pow(a+1,2)
    return summa

def squareSum(n):
    return pow(n*(n+1)/2, 2 )

##################################################

##################################################
# Problem 6
##################################################

#import sys
# sys.maxint = 2147483647 but this give us a memory error...
def getNthPrime(n):
    count=0
    for a in range(10000000):
        #if a%100 == 0:
            #print(str(a+1))
        if isprime(a+1):
            count+=1
            if count == n:
                return a+1
                break




##################################################

##################################################
# Problem 8
##################################################

#fixedThousandDigitNumber = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801\
#869478851843858615607891129494954595017379583319528532088055111254069874715852386305071\
#569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362\
#766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797\
#90879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864\
#46706324415722155397536978179778461740649551492908625693219784686224828397224137565705605749026140797296865\
#24145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824\
#5861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984\
#0385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094\

#0507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
#The four adjacent digits in the 1000-digit number above that have the greatest product are 9 × 9 × 8 × 9 = 5832
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def adjacentMultiply(n,r):
    """Takes in a really large number, n,
    and looks for the r-th adjacent digits with
    the largest product"""
    maxProd = 1
    nStr = str(n)
    nStrLen = len(nStr)
    for chunkIdx in range(nStrLen - r + 1):
        subStr= nStr[chunkIdx:chunkIdx+r]
        subProd=1
        for digit in subStr:
            subProd *= int(digit)
            if subProd>maxProd:
                maxProd=subProd
    return maxProd

#Solution is adjacentMultiply(fixedThousandDigitNumber, 13)
#23514624000



##################################################

##################################################
# Problem 9
##################################################

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc.

def isPythagoreanTriplet(a,b,c):
    if pow(int(a),2)+pow(int(b),2)-pow(int(c),2)==0:
        return True
    else:
        return False

def findPythagTripletSum(givenSum):
    # This is the absolute max that a can be
    for a in range(1,givenSum):
        for b in range(1,givenSum-a):
            c = givenSum - a - b
            if isPythagoreanTriplet(a,b,c):
                return a,b,c

# Test this:
#>>> findPythagTripletSum(12)
#(3, 4, 5)
# Solution:
#>>> findPythagTripletSum(1000)
#(200, 375, 425)
#>>> 200*375*425
#31875000


##################################################

##################################################
# Problem 10
##################################################
#
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#Find the sum of all the primes below two million.

def sumPrimesBelowN(n):
    summa = 0
    for a in range(1,n):
        if isprime(a):
            summa+=a
    return summa

# This is easy now that I have all the other functions!
# Test:
#>>> sumPrimesBelowN(9)
#17
#>>> sumPrimesBelowN(2000000)
#142913828922L


##################################################



##################################################
# Problem 11
##################################################

#In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
#08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
#49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
#81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
#52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
#22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
#24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
#32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
#67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
#24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
#21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
#78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
#16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
#86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
#19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
#04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
#88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
#04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
#20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
#20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
#01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
#
#The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
#What is the greatest product of four adjacent numbers in the
#same direction (up, down, left, right, or diagonally) in the 20×20 grid?

T=np.array([
[ 8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[ 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
])

def adjProd(T,r):
    """Finds the product of r adjacent entries
    in a nxn grid of numbers, T.
    Easier to use numpy array"""
    L=len(T)
    maxProd = 1
    for xIdx in range(L-r):
        print("x= "+ str(xIdx))
        for yIdx in range(L-r):
            print("y= " + str(yIdx))
            subProd_x = 1
            subProd_y = 1
            subProd_b = 1
            subProd_f = 1
            for rIdx in range(r):
                print("r index: "+ str(rIdx))
                subProd_x *= T[xIdx+rIdx,yIdx]
                subProd_y *= T[xIdx,yIdx+rIdx]
                subProd_b *= T[xIdx+rIdx,yIdx+rIdx]
                subProd_f *= T[xIdx+r-rIdx,yIdx+r-rIdx]
                if subProd_x >maxProd:
                    print("max: "+ str(maxProd))
                    maxProd=subProd_x
                    x=xIdx
                    y=yIdx
                if subProd_y >maxProd:
                    print("max: "+ str(maxProd))
                    maxProd=subProd_y
                    x=xIdx
                    y=yIdx
                if subProd_b >maxProd:
                    print("max: "+ str(maxProd))
                    maxProd=subProd_b
                    x=xIdx
                    y=yIdx
                if subProd_f >maxProd:
                    print("max: "+ str(maxProd))
                    maxProd=subProd_f
                    x=xIdx
                    y=yIdx
    return maxProd, x, y


##################################################



##################################################
# Problem 12
##################################################


#The sequence of triangle numbers is generated by adding the natural numbers.
#So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#The first ten terms would be:
#
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#Let us list the factors of the first seven triangle numbers:
#
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
#
#We can see that 28 is the first triangle number to have over five divisors.
#
#What is the value of the first triangle number to have over five hundred divisors?

def triangleNum(n):
    summa = 0
    for a in range(n+1):
        summa+=a
    return summa

def numFactorsTriangleNum(n):
    tNum = triangleNum(n)
    #numFactors = len( getAllFactors(tNum))+2
    numFactors = countAllFactors(tNum)
    return numFactors, tNum



def firstTriangleNDiv(n):
    start_time = time.clock()
    for a in range(10000):
        q,w=numFactorsTriangleNum(a)
        if q>n:
            end_time = time.clock()
            print("Time taken : " + str( end_time - start_time ) + " sec")
            return q,w, end_time-start_time
            break

# Answer: I did this in C because of the overflow
# It is the 12375th triangle number,
# 76576500
# With 576 divisors

##################################################


##################################################
# Problem 13
##################################################

#Work out the first ten digits of the sum of one-hundred 50-digit numbers (given).

def getFirstNdigits(n):
    summa1 = 0
    summa2 = 0
    with open("FiftydigitNumber_Prob13.txt", 'rb') as fileName:
        for eachLine in fileName.readlines():
            summa1 += int(eachLine[0:30])
            #summa2 += int(eachLine[10:20])
    #carryDigits = str(summa2)[0]
    #summa1 += int( carryDigits )
    return str(summa1)[0:10]

# Answer:
#>>> getFirstNdigits(10)
#'5537376230'

##################################################


##################################################
# Problem 14
##################################################

#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


# Answer:
# I did this in C
# The MFing answer is supposedly 837799
# Yet I get:
# The largest chain is 476, from 910107


##################################################



##################################################
# Problem 15
##################################################

#Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Answer:
# This one was easy and I love it!
# You can see that the l1-norm is double the lattice size.
# i.e. the number of moves to get from the beginning to the end
# is a constant (double the side length) for any square lattice.
# ||d(n)||_1 = 2*n
# Now the number of ways you can traverse the lattice is
# just the combinatorics, ^(2*n)C_n
# So the answer for n=20 is ^{40}C_{20} = 137846528820

def nCr(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

##################################################

##################################################
# Problem 16
##################################################

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#What is the sum of the digits of the number 2^1000 ?

# Answer
# Thankfully 2^1000 is handled by Python apparently fine
# To add digits, just convert between int and str
# >>> z=pow(2,1000)
# >>> len(str(z))
# 302
# >>> summa=0
# >>> for i in str(z):
#     ...     summa+=int(i)
#     ...
# >>> summa
# 1366


##################################################


##################################################
# Problem 17
##################################################


# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when
# writing out numbers is in compliance with British usage.

def countLettersInNumbers():
    summa = 0
    numStr1=[ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" ]
    numStrTeen=[ "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
    numStrTens=[ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    numStrHundred = "hundred"
    numStrThousand = "thousand"
    numStrAnd = "and"
    for numIdx in range(10):
        print(numStr1[numIdx]+"\n")
        summa+=len(numStr1[numIdx])
    for numIdx in range(10, 19):
        print(numStrTeen[numIdx-10]+"\n")
        summa+=len(numStrTeen[numIdx-10])
    for numIdx in range(20, 100):
        tensDigit = numStrTens[int(str(numIdx)[0])-2]
        onesDigit = ""
        if int(str(numIdx)[1]):
            onesDigit = numStr1[int(str(numIdx)[1])-1]
        print(tensDigit+" " +onesDigit+"\n")
        summa+=len(tensDigit+onesDigit)
    for numIdx in range(100, 1000):
        hundredsDigit = numStr1[int(str(numIdx)[0])-1] + numStrHundred
        tensDigit = ""
        onesDigit = ""
        # TODO take care of teens edge case
        if int(str(numIdx)[1]):
            if (int(str(numIdx)[1]) == 1):
                tensDigit = numStrAnd + numStrTeen[int(str(numIdx)[2])-1]
                onesDigit = ""
            else:
                tensDigit = numStrAnd + numStrTens[int(str(numIdx)[1])-2]
                if int(str(numIdx)[2]):
                    onesDigit = numStr1[int(str(numIdx)[2])-1]
        else:
            if int(str(numIdx)[2]):
                onesDigit = numStrAnd + numStr1[int(str(numIdx)[2])-1]
        print(hundredsDigit+ " "  + tensDigit+" " +onesDigit+"\n")
        summa+=len(hundredsDigit+ tensDigit +onesDigit)
    print
    return summa



# Answer:
# This code doesn't quite handle "x hundred and ten"
# instead giving "x hundred and nineteen" instead.
# Also, I just decided to manually add "one thousand" (i.e. 11)
# so I just adjusted the result of the function, 21158,
# by taking away 45=9*(8-3) and adding 11, giving:
# 21124



##################################################


##################################################
# Problem 18
##################################################

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67, is the same challenge with a triangle
#containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


# The following is inspired by a treatment of the shortest path in
# weighted Directed Acyclic Graphs (DAGs) by using topological sorting
# As in:
# http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/
# And:
# http://www.utdallas.edu/~sizheng/CS4349.d/l-notes.d/L17.pdf
# However, I'm looking for the *longest* path to the bottom entries (and don't
# care about the rest).


edgeVals = [
75,
95, 64,
17, 47, 82,
18, 35, 87, 10,
20,4, 82, 47, 65,
19,1, 23, 75,3, 34,
88,2, 77, 73,7, 63, 67,
99, 65,4, 28,6, 16, 70, 92,
41, 41, 26, 56, 83, 40, 80, 70, 33,
41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
63, 66,4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
4, 62, 98, 27, 23,9, 70, 98, 73, 93, 38, 53, 60,4, 23,
]

def graphEdges(n, edgeVals):
    """Get allowable edges in number pyramid graph"""
    graphEdges = []
    for i in range(1, n):
        l1 = i*(i-1)/2
        l2 = i*(i+1)/2
        print("Level: " + str(l2))
        for j in range(l1,l2):
            for k in range(2):
                #graphEdges.append([l1+j+k,l2+j+k,edgeVals[l2+j+k] ])
                print("Node " + str(j) + " can go to " + str(l2+j+k))
    return graphEdges









##################################################




##################################################
# Problem 19
##################################################


#You are given the following information, but you may prefer to do some research for yourself.
#
#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



##################################################


##################################################
# Problem 20
##################################################

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# Answer:
# Unfortunately just brute-forced this one...
# >>> z=math.factorial(100)
# >>> z
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
# >>> summa=0
# >>> for i in range( len(str(z))):
#     ...     summa+=int(str(z)[i])
#     ...
#  >>> summa
#  648


##################################################



##################################################
# Problem 21
##################################################

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.



##################################################

##################################################
# Problem 87
##################################################



#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
#    28 = 2^2 + 2^3 + 2^4
#    33 = 3^2 + 2^3 + 2^4
#    49 = 5^2 + 2^3 + 2^4
#    47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?




def sumPowerTripleMax(n):
    return pow(n,2)+pow(n,3)+pow(n,4)

def sumPowerTriple(a,b,c):
    return pow(a,2)+pow(b,3)+pow(c,4)

def getSumPowerTriplesUpToN(summa):
    counter=0
    #outPutStr=""
    #nmax=int( 5*math.ceil((math.sqrt(1+4*math.sqrt(summa))-1)/(2)) )+1
    # Had to set this manually for summa=50000000
    nmax=1000
    print("Nmax:" + str(nmax))
    for c in range(2,nmax+1):
        for b in range(2, nmax+1):
            for a in range(2, nmax+1):
                if sumPowerTriple(a,b,c) < summa:
                    #print(str(a)+", " +str(b) + ", " + str(c))
                    if (isprime(a) and isprime(b) and isprime(c)):
                        outPutStr = str(a) + ", " + str(b) + ", " + str(c) + " make: " +str(sumPowerTriple(a,b,c)) + " \n"
                        #rint(outPutStr)
                        counter += 1
    return counter

#getSumPowerTriplesUpToN(50)


def getSumPowerTriples(nmax):
    counter=0
    #outPutStr=""
    for a in range(2,nmax+1):
        for b in range(2, a+1):
            for c in range(2, b+1):
                if sumPowerTriple(a,b,c) < pow(nmax,2):
                    #print(str(a)+", " +str(b) + ", " + str(c))
                    if (isprime(a) and isprime(b) and isprime(c)):
                        outPutStr = str(a) + ", " + str(b) + ", " + str(c) + " make: " +str(sumPowerTriple(a,b,c)) + " \n"
                        print(outPutStr)
                        counter += 1
    return counter

##################################################

##################################################
# Problem 88
##################################################

# This isn't quite right---need to account for multiple instances of members
def isProdSumNum(n):
    allFactors=getAllFactors(n)
    allFactors.append(1)
    if sum(allFactors) == n:
        return True
    else:
        return False



##################################################

##################################################
# Problem 561 (Solved by 92)
##################################################

# 1) Let S(n) be the number of pairs (a,b) of distinct divisors of n such that a divides b.
# For n=6 we get the following pairs: (1,2),(1,3),(1,6),(2,6) and (3,6). So S(6)=5.
# 2) Let pm# be the product of the first m prime numbers, so p2#=2∗3=6.
# 3) Let E(m,n) be the highest integer k such that 2^k divides S((pm#)^n).
# E(2,1) = 0 since 20 is the highest power of 2 that divides S(6)=5.
# 4) Let Q(n) = ∑{i->n} E(904961,i)
# Q(8)=2714886
# Evaluate Q(10^12)



def numPairDistinctDivisors(n):
    factors= getAllFactors(n)





##################################################
