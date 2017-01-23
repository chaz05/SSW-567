'''
Created on Jan 21, 2017

@author: caadams2
'''
def classifyTriangle(a, b, c, res = 0.000005):
    '''
    Constructor
    '''
    longest = [a, b, c]
    longest.sort()
    a = longest[0]
    b = longest[1]
    c = longest[2]


    scalene = a != b and a != c and b != c
    isosceles = ((a == b) or (a == c) or (b == c)) and not (a == b and a == c)
    equilateral = (a == b and a == c)
    rightTriangle = (a**2 + b**2)+res >= c**2 and (a**2 + b**2)-res <= c**2
    
    print("Scalene: %s,\tIsosceles %s, \tEquilateral: %s,\tRight Triangle: %s" % (scalene, isosceles, equilateral, rightTriangle))
    return scalene, isosceles, equilateral, rightTriangle


