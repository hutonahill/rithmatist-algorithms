import numpy

ACCEPTABLE_DEGREES_ERROR = 10

def main():
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


    for i in range(1, (len(points)-1)):

        line1 = (points[0], center)
        line2 = (points[i], center)
        theta = findAngle(line1, line2)



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


    for i in range(1, (len(points)-1)):

        line1 = (points[0], center)
        line2 = (points[i], center)
        theta = findAngle(line1, line2)

        # calculate the error assuming each posible ideas 6-point.

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
    
    
    # check the type of each point
    elif type(line1[0]) != tuple:
        raise TypeError("points but be formated as a tuple. " + 
        f"The input point line1[0] is formated as a {type(line1[0])}")

    elif type(line1[1]) != tuple:
        raise TypeError("points but be formated as a tuple. " + 
        f"The input point line1[1] is formated as a {type(line1[1])}")

    elif type(line2[0]) != tuple:
        raise TypeError("points but be formated as a tuple. " + 
        f"The input point line2[0] is formated as a {type(line2[0])}")

    elif type(line2[1]) != tuple:
        raise TypeError("points but be formated as a tuple. " + 
        f"The input point line2[1] is formated as a {type(line2[1])}")

    # check the length of each point
    elif len(line1[0]) != 2:
        raise TypeError("Points are composed of two cordinates. " + 
        f"The input point line1[0] has {len(line1[0])} cordinates")

    elif len(line1[1]) != 2:
        raise TypeError("Points are composed of two cordinates. " + 
        f"The input point line1[1] has {len(line1[1])} cordinates")

    elif len(line2[0]) != 2:
        raise TypeError("Points are composed of two cordinates. " + 
        f"The input point line2[0] has {len(line2[0])} cordinates")

    elif len(line2[1]) != 2:
        raise TypeError("Points are composed of two cordinates. " + 
        f"The input point line2[1] has {len(line2[1])} cordinates")

    # Check the type of each cordinate in line 1
    elif type(line1[0][0]) != float:
        raise TypeError(f"cordinate line1[0][0] has the type " +
        f"{type(line1[0][0])}. It must be a float.")
    
    elif type(line1[0][1]) != float:
        raise TypeError(f"cordinate line1[0][1] has the type " +
        f"{type(line1[0][1])}. It must be a float.")

    elif type(line1[1][0]) != float:
        raise TypeError(f"cordinate line1[1][0] has the type " +
        f"{type(line1[1][0])}. It must be a float.")
    
    elif type(line1[1][1]) != float:
        raise TypeError(f"cordinate line1[1][1] has the type " +
        f"{type(line1[1][1])}. It must be a float.")
    
    # Check the type of each cordinate in line 2
    elif type(line2[0][0]) != float:
        raise TypeError(f"cordinate line2[0][0] has the type " +
        f"{type(line2[0][0])}. It must be a float.")
    
    elif type(line2[0][1]) != float:
        raise TypeError(f"cordinate line2[0][1] has the type " +
        f"{type(line2[0][1])}. It must be a float.")

    elif type(line2[1][0]) != float:
        raise TypeError(f"cordinate line2[1][0] has the type " +
        f"{type(line2[1][0])}. It must be a float.")
    
    elif type(line2[1][1]) != float:
        raise TypeError(f"cordinate line2[1][1] has the type " +
        f"{type(line2[1][1])}. It must be a float.")
    

    m1 = findSlope(line1[0], line1[1])
    assert type(m1) == float, (f"type(m1) == {type(m1)}, m1 == {m1}")

    m2 = findSlope(line2[0], line2[1])
    assert type(m2) == float, (f"type(m2) == {type(m2)}, m2 == {m2}")


    # sorce: https://www.cuemath.com/geometry/angle-between-two-lines/
    theta = numpy.arctan((m1-m2)/(1+m1*m2))

    assert type(theta) == float, \
        (f"type(theta) == {type(theta)}, theta == {theta}")


def findSlope(point1:tuple, point2:tuple):

    #check the number of cordinates in each point
    if len(point1) != 2:
        raise TypeError(f"cordinate point1 has {len(point1)} cordinates. " +
        "It must have 2.")

    elif len(point2) != 2:
        raise TypeError(f"cordinate point2 has {len(point2)} cordinates. " +
        "It must have 2.")
    
    #check the type of each cordinate
    elif type(point1[0]) != float:
        raise TypeError(f"the cordinate point1[0] has the " +
        f"type {type(point1[0])}. it must have the type float.")
    
    elif type(point1[1]) != float:
        raise TypeError(f"the cordinate point1[1] has the " +
        f"type {type(point1[1])}. it must have the type float.")
    
    elif type(point2[0]) != float:
        raise TypeError(f"the cordinate point2[0] has the " +
        f"type {type(point2[0])}. it must have the type float.")
    
    elif type(point2[1]) != float:
        raise TypeError(f"the cordinate point2[1] has the " +
        f"type {type(point2[1])}. it must have the type float.")

    # sorce: https://www.physicsclassroom.com/class/1DKin/Lesson-3/Determining-the-Slope-on-a-p-t-Graph
    slope = (point2[1] - point1[1])/(point2[0]-point1[0])

    assert type(slope) == float, (f"type(slope) == {type(slope)}, " + 
    f"slope == {slope}")

    return slope

if __name__ == "__main__":
    main()