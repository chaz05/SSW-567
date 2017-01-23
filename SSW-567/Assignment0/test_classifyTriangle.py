'''
Created on Jan 21, 2017

@author: caadams2
'''
import unittest
import solveTriangle as Tony
import tjfTriangle as Travis
from math import sqrt

class Test(unittest.TestCase):
    members = [Tony,Travis]

    def testNominalScalene(self):
        for member in self.members:
            self.assertEqual(member.classifyTriangle(3, 4, 5, 0), (True, False, False, True))
            
            self.assertEqual(member.classifyTriangle(1, 2, 2.5), (True, False, False, False))
        
    def testNominalIsosceles(self):
        for member in self.members:
            #right
            self.assertEqual(member.classifyTriangle(4,4, 4*sqrt(2)), (False, True, False, True))
            #not right
            self.assertEqual(member.classifyTriangle(2, 2, 3.5), (False, True, False, False))
        
    def testNominalEquilateral(self):
        for member in self.members:
            self.assertEqual(member.classifyTriangle(2, 2, 2), (False, False, True, False))
    
    def testInvalidInputs(self):
        for member in self.members:
            self.assertEqual(member.classifyTriangle(-1, 2, 2.5), (True, False, False, False))
            self.assertEqual(member.classifyTriangle(1, 2, 3), (False, False, False, False))
            self.assertEqual(member.classifyTriangle(5, 4, 3), (True, False, False, True))
            self.assertEqual(member.classifyTriangle(0, 0, 0), (False, False, False, False))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNominalScalene', 'Test.testNominalIsosceles', 'Test.testNominalEquilateral']
    unittest.main()