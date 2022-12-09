# This code is owned by Hutonahill who researves all rights related to it.
# Use of this code, without written permition, is prohibited.

# Returns a list of cords of a circle 
# with each point seperated by 1 unit of circomfrence
# returned list will contane a number of items eqle to the
# circumference 

def CENTER_KEY():
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


    circleDict = {CENTER_KEY():(centerX,centerY), CIRCLE_KEY():[]}
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

def pointGen(circle:list, numPoints = 3):
    '''Generates 3 points in an input "circle" with its center at \
        0,0, '''

    import random

    if numPoints < 3:
        raise TypeError(f"numPoints must be greater than or equil to 3." + 
        f"it is currently set to {numPoints}.")


    rand1 = random.randint(0,len(circle))

    randIndexes = [rand1]

    numPoints = numPoints - 1

    for i in range(0, numPoints):


        rand2 = random.randint(0,len(circle)) 

        #make sure there are no duplicates
        while rand2 in randIndexes:
            rand2 = random.randint(0,len(circle)) 
    
        randIndexes.append(rand2)


    random.shuffle(randIndexes)

    output = []
    for i in randIndexes:
        output.append(circle[i])

    return output

def main():
    circleDict = circleGen(5)

    circleList = circleDict[CIRCLE_KEY()]

    points = pointGen(circleList)

    print(points)

if __name__ == "__main__":
    main()