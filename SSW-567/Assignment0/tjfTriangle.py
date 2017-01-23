'''
Created on Jan 23, 2017

@author: tjfloyd
'''

def classifyTriangle(a, b, c, thresh = 0.0001):
    '''
    Function returns type of triangle
    a, b, and c are the lengths of each of the sides. Expect real values.
    thresh represents the resolution for comparing two sides to be equal
    '''
    
    # Validate that the entries actually form a triangle
    validT = ((a + b) > c) and ((b + c) > a) and ((a + c) > b)
        
    # Classify the type of triangle based on the
    # relationship of lengths of the sides
    if validT:
        equilateral = (a == b) and (a == c)
        isosceles = ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (a != b))
        scalene = (a != b) and (a != c) and (b != c)
    else:
        equilateral = False
        isosceles = False
        scalene = False
    
    # Determine if the triangle is a right triangle
    # a^2 + b^2 = c^2
    sumofsqr = (a**2 + b**2)
    hypsqr = c**2
    right = (abs((sumofsqr - hypsqr)) <= thresh)
    
    # Print the result of the classification
    if equilateral:
        print("TJF: %s, %s, %s :: equilateral, right: %s" % (a, b, c, right))
    elif isosceles:
        print("TJF: %s, %s, %s :: isosceles, right: %s" % (a, b, c, right))
    elif scalene:
        print("TJF: %s, %s, %s :: scalene, right: %s" % (a, b, c, right))
    else:
        print("TJF: Not a triangle")
    
    return scalene, isosceles, equilateral, right

# Classify some triangles
classifyTriangle(1, 2, 3)
classifyTriangle(1, 1, 1)
classifyTriangle(3, 3, 1)
classifyTriangle(4.5, 1, 4.5)
classifyTriangle(2.7, 3.201, 3.201)
classifyTriangle(1, 1, 1.41421)
