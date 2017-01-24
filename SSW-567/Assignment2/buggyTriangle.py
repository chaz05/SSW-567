# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.
1/24/2017 5:30:03 AM - Rak, Travis, Tony, Courtney
Corrected issues and added tests.

@author: jrr
"""

import unittest     # this makes Python unittest module available
from math import sqrt
from sys import float_info
FLOAT_MIN = float_info.min
FLOAT_MAX = float_info.max

def classifyTriangle(a,b,c,res = 0.00001):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      
      BEWARE: there may be a bug or two in this code
        
    """
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,(float,int)) and isinstance(b,(float,int)) and isinstance(c,(float,int)) and isinstance(res,(float,int))):
        return 'InvalidInput';
    
    # restrict all sides to being positive non-zero values
    # non-zero in this case must be within the selected resolution 
    if res > 0 and (a <= res or b <= res or c <= res):
        return 'InvalidInput'
    
    # order the sides to validate the assumption that the potential hypotenuse is side c
    # this simplifies the check for the right angle (a^2 + b^2 = c^2)
    longest = [a, b, c]
    longest.sort()
    a = longest[0]
    b = longest[1]
    c = longest[2]
    
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif (a**2 + b**2)+res >= c**2 and (a**2 + b**2)-res <= c**2:
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
        
        
def runClassifyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,b),sep="")

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testInvalid1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 is not a triangle')
    def testInvalid2(self): # test invalid inputs
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 is invalid input')
    def testInvalid3(self): # test invalid inputs
        self.assertEqual(classifyTriangle(-2,3,4),'InvalidInput','-2,3,4 is invalid input')
    def testInvalid4(self): # test invalid inputs
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,c is invalid input')
    def testInvalid5(self): # test invalid inputs
        with self.assertRaises(TypeError, msg='1,2,3,4,5 is invalid input'):
            classifyTriangle(1,2,3,4,5)
        
    def testValid1(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,2,2.5),'Scalene','1,2,2.5 should be Scalene')
    def testValid2(self): 
        self.assertEqual(classifyTriangle(2,2,3.999),'Isoceles','2,2,3.999 should be Isoceles')
    def testValid3(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be Equilateral')
    def testValid4(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 should be Right')
    def testValid5(self): 
        self.assertEqual(classifyTriangle(1,1,sqrt(2)),'Right','1,1,sqrt(2) should be Right')

    def testRange1(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(150, 220, 100),'Scalene','150,220,100 should be Scalene')
    def testRange2(self):
        self.assertEqual(classifyTriangle(FLOAT_MAX, FLOAT_MAX, FLOAT_MAX),'Equilateral',' FLOAT_MAX, FLOAT_MAX, FLOAT_MAX should be Equilateral')
    def testRange3(self):
        self.assertEqual(classifyTriangle(FLOAT_MIN, FLOAT_MIN, FLOAT_MIN),'InvalidInput',' FLOAT_MIN, FLOAT_MIN, FLOAT_MIN should be InvalidInput')
                
    def testRobust1(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','10,10,10 Should be Equilateral')
    def testRobust2(self): 
        self.assertEqual(classifyTriangle(FLOAT_MAX,FLOAT_MAX,FLOAT_MAX*sqrt(2)),'NotATriangle','FLOAT_MAX,FLOAT_MAX,FLOAT_MAX*sqrt(2) Should be Right Triangle')
    def testRobust3(self): 
        with self.assertRaises(OverflowError, msg='sqrt(FLOAT_MAX),sqrt(FLOAT_MAX),sqrt(FLOAT_MAX)*sqrt(2) Should be Overflow'):
            classifyTriangle(sqrt(FLOAT_MAX),sqrt(FLOAT_MAX),sqrt(FLOAT_MAX)*sqrt(2))
    def testRobust4(self):
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 Should be Right Triangle')
    def testRobust5(self): 
        self.assertEqual(classifyTriangle(sqrt(FLOAT_MAX)/2,sqrt(FLOAT_MAX)/2,sqrt(((sqrt(FLOAT_MAX)/2)**2)*2)),'Right','sqrt(FLOAT_MAX)/sqrt(2),sqrt(FLOAT_MAX)/sqrt(2),sqrt(FLOAT_MAX) Should be Right Triangle')

if __name__ == '__main__':
    # examples of running the  code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    
    print('Begin UnitTest')
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       