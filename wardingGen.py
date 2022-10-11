# This code is owned by Hutonahill who researves all rights related to it.
# Use of this code, without written permition, is prohibited.

# Returns a list of cords of a circle 
# with each point seperated by 1 unit of circomfrence
# returned list will contane a number of items eqle to the
# circumference 

def circleGen(radius, centerX =0, centerY=0):
    '''radius: the radius of the intended sample circle
    \ncenterX: the x cordinate of the center of the intended sample circle
    \ncenterY: the y cordinate of the center of the intended sample circle
    \nReturn: a list of points, 1/2 unit appart around the sample circle'''
    import numpy

    # Calculate circumference
    circumference = 2 * numpy.pi * radius

    #calculate the num of radians
    rad = 2 * numpy.pi

    #calculate the radians per unit in the circumference
    radPerUnit = rad/(circumference*2)


    cordList = []
    for theta in numpy.arange(0,rad,radPerUnit):

        # Calculate xy cords assuming center is 0,0.
        x = radius * numpy.cos(theta)
        y = radius * numpy.sin(theta)

        # Shift cords to account for posible difrent center.
        cords = (x + centerX, y + centerY)

        cordList.append(cords)
    
    return cordList

def circleGenTesting(radius, centerX = 0, centerY = 0):
    '''prints our the strength of each segment in a circle then 
    prints out the max and min segment strengths and the difrance 
    between max and min and the asoceated error'''
    testCircle = circleGen(radius, centerX, centerY)
    for i in range(len(testCircle)):
        print(f"{i}: {testCircle[i]}")
        