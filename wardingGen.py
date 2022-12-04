# This code is owned by Hutonahill who researves all rights related to it.
# Use of this code, without written permition, is prohibited.

# Returns a list of cords of a circle 
# with each point seperated by 1 unit of circomfrence
# returned list will contane a number of items eqle to the
# circumference 

def RADIUS_KEY():
    return "radius"

def CIRCLE_KEY():
    return "circle"

def circleGen(radius, centerX =0, centerY=0):
    '''radius: the radius of the intended sample circle
    \ncenterX: the x cordinate of the center of the intended sample circle
    \ncenterY: the y cordinate of the center of the intended sample circle
    \nReturn: a dictionary wiht the radius and a \
    list of points, 1/2 unit appart around the sample circle'''
    import numpy

    # Calculate circumference
    circumference = 2 * numpy.pi * radius

    #calculate the num of radians
    rad = 2 * numpy.pi

    #calculate the radians per unit in the circumference
    radPerUnit = rad/(circumference*2)


    circleDict = {RADIUS_KEY():radius, CIRCLE_KEY():[]}
    copyData = []
    for theta in numpy.arange(0,rad,radPerUnit):

        # Calculate xy cords assuming center is 0,0.
        x = radius * numpy.cos(theta)
        y = radius * numpy.sin(theta)

        # Shift cords to account for posible difrent center.
        cords = (x + centerX, y + centerY)

        copyData.append(cords)
    
    circleDict[CIRCLE_KEY()] = copyData
    
    return circleDict.copy()

def circleGenTesting(radius, centerX = 0, centerY = 0):
    '''prints our the strength of each segment in a circle then 
    prints out the max and min segment strengths and the difrance 
    between max and min and the asoceated error'''
    testCircleDict = circleGen(radius, centerX, centerY)

    testCircle = testCircleDict[CIRCLE_KEY()]

    for i in range(len(testCircle)):
        print(f"{i}: {testCircle[i]}")

def threePointGen(circle:list):
    '''Generates 3 point in an input "circle" with its center at \
        0,0, two of which will be 
    directly across from each other'''

    import random

    rand1 = random.randint(0,len(circle))

    output = [circle[rand1]]

    rand2 = random.randint(0,len(circle)) 

    while rand1 == rand2:
        rand2 = random.randint(0,len(circle)) 
    
    output.append(circle[rand2])

    copydata = circle[rand2]

    copydata = (copydata[0]*-1, copydata[1]*-1)

    output.append(copydata)

    random.shuffle(output)

    return output


        