import numpy

ACCEPTABLE_DEGREES_ERROR = 10

def main(circle:dict, points:list):
    pass

def fourPoint(center:tuple, points:list):
    '''For calculating the error for a 4 point circle
    \ncenter:tuple, the center of the circle
    \npoints:list, 3 or 4 points around the circle to be tested.
    Returns a list with the degrees of error for each point.'''

    #make sure no more than 4 points were input
    if len(points) != 4 and len(points) != 3:
        raise TypeError("You must include 3 or 4 points.")
    
    # make sure points have the proper type and are in circle.
    for i in points:
        if type(i) != tuple:
            raise TypeError("All point but be in the form of tuples")

    #END LOOP

    pointError = [0.0]


    # calculate the error for each point except the first.
    for i in range(1, (len(points)-1)):

        line1 = (points[0], center)
        line2 = (points[i], center)
        theta = findAngle(line1, line2)


        # Determin whitch ideal 4-point is closest
        if numpy.abs(theta-90) > numpy.abs(theta-180):
            pointError.append(theta-180)
        
        else:
            pointError.append(theta - 180)
    
    assert len(pointError) == len(points), \
        (f"len(pointError) == {len(pointError)}, len(points) == {len(points)}")
    
    return pointError

def sixPoint(center:tuple, points:list):
    '''For calculating the error for a 6 point circle
    \ncenter:tuple, the center of the circle.
    \npoints:list, 3 to 6 points around the circle to be tested.
    \nReturns a list with the degrees of error for each point.
    \nThe first point never has any error.'''

    #make sure no more than 4 points were input
    if (3 <= len(points) <= 6) == False:
        raise TypeError("You must include 3 to 6 points.")
    
    # make sure points have the proper type and are in circle.
    for i in points:
        if type(i) != tuple:
            raise TypeError("All point but be in the form of tuples")

    #END LOOP

    pointError = [0.0]

    # calculat ethe error for each posible 6-point
    for i in range(1, (len(points)-1)):

        line1 = (points[0], center)
        line2 = (points[i], center)
        theta = findAngle(line1, line2)

        # determin which ideal 6-point is closets to input point

        posibleErrorValues = [theta - 60, theta - 120, theta - 180]
        minValue = numpy.abs(posibleErrorValues[0])
        minIndex = 0

        for j in range(1, (len(posibleErrorValues)-1)):
            if numpy.abs(posibleErrorValues[j]) < minValue:
                minValue = numpy.abs(posibleErrorValues[j])
                minIndex = j
        
        pointError.append(posibleErrorValues[minIndex])
    
    assert len(pointError) == len(points), \
        (f"len(pointError) == {len(pointError)}, len(points) == {len(points)}")
    
    return pointError
    

def filler():
    '''no funciton
    \nprvents findAngle() form expanding every time i make a loop or if.'''
    pass

def findAngle(line1:list, line2:list):

    # check number of points in each line
    if len(line1) != 2:
        raise TypeError(f"line1 must include 2 points. You included " + 
        f"{len(line1)} points")

    elif len(line2) != 2:
        raise TypeError(f"line2 must include 2 points. You included " + 
        f"{len(line2)} points")
    
    # error check each line as a list of points
    validatePoints(line1)
    validatePoints(line2)
    

    m1 = findSlope(line1[0], line1[1])
    assert type(m1) == float, (f"type(m1) == {type(m1)}, m1 == {m1}")

    m2 = findSlope(line2[0], line2[1])
    assert type(m2) == float, (f"type(m2) == {type(m2)}, m2 == {m2}")


    # sorce: https://www.cuemath.com/geometry/angle-between-two-lines/
    theta = numpy.arctan((m1-m2)/(1+m1*m2))

    assert type(theta) == float, \
        (f"type(theta) == {type(theta)}, theta == {theta}")


def findSlope(point1:tuple, point2:tuple):

    # Error check the points
    validatePoints([point1, point2])

    # sorce: https://www.physicsclassroom.com/class/1DKin/Lesson-3/Determining-the-Slope-on-a-p-t-Graph
    slope = (point2[1] - point1[1])/(point2[0]-point1[0])

    assert type(slope) == float, (f"type(slope) == {type(slope)}, " + 
    f"slope == {slope}")

    return slope


def validatePoints(points:list):
    # Check for a length of 0
    numPoints = len(points)
    if numPoints == 0:
        raise TypeError (f"the list of points must have at least one point")
    
    

    for i in range(numPoints):
        testValue = points[i]

        if type(testValue) != tuple:
            raise TypeError (f"points must have the type tuple. point[{i}] " + 
            f"has the type type(testValue)")
        
        elif len(testValue) != 2:
            raise TypeError(f"Cordinates are made up of two points. " + 
            f"the cordinate point[{i}] has {len(testValue)} point(s)")
        
        elif type(testValue[0]) == float:
            raise TypeError("Cordinates are made up of two floats. " + 
            f"the value points[{i}][0] is a {type(testValue[0])}.")
        
        elif type(testValue[1]) == float:
            raise TypeError("Cordinates are made up of two floats. " + 
            f"the value points[{i}][0] is a {type(testValue[1])}.")

if __name__ == "__main__":
    main()