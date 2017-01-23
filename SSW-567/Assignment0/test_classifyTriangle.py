'''
Created on Jan 21, 2017

@author: caadams2
'''
import unittest
from solveTriangle import classifyTriangle
from math import sqrt

class Test(unittest.TestCase):


    def testNominalScalene(self):
        self.assertEqual(classifyTriangle(3, 4, 5, 0), (True, False, False, True))
        
        self.assertEqual(classifyTriangle(1, 2, 3), (True, False, False, False))
        
    def testNominalIsosceles(self):
        #right
        self.assertEqual(classifyTriangle(4,4, 4*sqrt(2)), (False, True, False, True))
        #not right
        self.assertEqual(classifyTriangle(2, 2, 5), (False, True, False, False))
        
    def testNominalEquilateral(self):
        self.assertEqual(classifyTriangle(2, 2, 2), (False, False, True, False))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNominalScalene', 'Test.testNominalIsosceles', 'Test.testNominalEquilateral']
    unittest.main()