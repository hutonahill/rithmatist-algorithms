import numpy

from wardingUtility import validatePoint, validatePointList

# Constants
def ACCEPTABLE_DEGREES_ERROR():
    return 10

def FOUR_POINT_KEY():
    return "4-point"

def SIX_POINT_KEY():
    return "6-point"

# Functions
def main(centerPoint:tuple, points:list, circleType = 'unknown'):
    '''given a center a and a list of points determin if the given set of 
    points is valid and what the userError is'''
    # Validate the inputs
    validatePoint(centerPoint, 'centerPoint')

    validatePointList(points)

    # Output format [arePointsValid:Boolean, userError:list, circleType:str]
    arePointsValid = True
    # Cover the cases where the type of circle is known

    # Known 4-point circle
    if circleType == FOUR_POINT_KEY():

        # Generate an error score for each point assuming a 4-point circle
        userError = fourPoint(centerPoint, points)
        
        
        assert type(userError) == list, \
            (f"type(userError) == {type(userError)}, " + 
            f"userError == {userError}")

        # get the total error score of the points and wether or not it is
        # a valid circle. 
        copyData = sumCheckScores(userError)

        arePointsValid = copyData[1]

        # circleType is unchanged.
        
    
    # Known 6-point circle
    elif circleType == SIX_POINT_KEY():
        
        # generate an error score for each point assuming a 6-point circle
        userError = sixPoint(centerPoint, points)

        assert type(userError) == list, \
            (f"type(userError) == {type(userError)}, " + 
            f"userError == {userError}")

        copyData = sumCheckScores(userError)

        arePointsValid = copyData[1]

        # circleType is unchanged.
        

    # if the type of circle is not known try to detect it
    else:

        #save the len of points so we only have to calculate it once
        numPoints = len(points)

        # all circles with only 1 point are valid
        if numPoints == 1:
            arePointsValid = True
            userError = [0.0]
            # circleType is unchanged
        
        # If there are between 2 and 4 points attempt to determin which type
        # the circle is
        elif 2 <= numPoints <= 4:

            # calculate the error of every point assuming a 4-point circle
            fourScoreList = fourPoint(centerPoint, points)
            
            assert type(fourScoreList) == list, \
                (f"type(fourScoreList) == {type(fourScoreList)}, " + 
                f"fourScoreList == {fourScoreList}")

            # get the total error score of the points and wether or not it is
            # a valid circle. 
            copyData = sumCheckScores(fourScoreList)

            # Store the total score of this set of points
            fourScore = copyData[0]
            
            # Store wether or not the circle is valid as a 4-point
            validFourFlag = copyData[1]

            # calculate the error of every point assuming a 4-point circle
            sixScoreList = sixPoint(centerPoint, points)

            assert type(sixScoreList) == list, \
                (f"type(sixScore) == {type(sixScoreList)}, " + 
                f"sixScore == {sixScoreList}")
            
            # get the total error score of the points and wether or not it is
            # a valid circle. 
            copyData = sumCheckScores(sixScoreList)

            #store the total score of this set of points assuming a 6-point circle
            sixScore = copyData[0]
            
            # Store wether or not the circle is valid as a 6-point circle
            validSixFlag = copyData[1]

            # if the four and six scores are the same,
            # dont return a circle type
            if fourScore == sixScore:
                
                # Store the one of the scores as a the user error
                userError = fourScoreList
                
                # Store one fo the flags as the primary valid flag
                arePointsValid = validFourFlag

            # if the user error is lower when the circle is assumed to be a 
            # 4-point, return that the circle is a 4-point
            elif fourScore < sixScore:

                # Store the 4-point error lsit as the userError
                userError = fourScoreList
                
                # Store the 4-point valid flag as the primary valid flag
                arePointsValid = validFourFlag
                
                # Store 4-point circle as the circle type
                circleType = FOUR_POINT_KEY()

            # if the user error is lower when the circle is assumed to be a 
            # 6-point, return that the circle is a 6-point
            else:
                # Store the 6-point error lsit as the userError
                userError = sixScoreList

                # Store the 6-point valid flag as the primary valid flag
                arePointsValid = validSixFlag
                
                # Store 6-point circle as the circle type
                circleType = SIX_POINT_KEY()
        
        # if 5 - 6 points are given, assume its a 6 point
        elif 5 <= numPoints <= 6:

            # generate an error score for each point assuming a 6-point circle
            userError = sixPoint(centerPoint, points)

            assert type(userError) == list, \
                (f"type(userError) == {type(userError)}, " + 
                f"userError == {userError}")

            # Determin wether the circle is valid
            copyData = sumCheckScores(userError)

            arePointsValid = copyData[1]

            # Set circleType to 6-point circle
            circleType = SIX_POINT_KEY()

        # if more than 4 points are given 
        elif (1 <= numPoints <= 6) == False:
            raise ValueError("Points must be a list of points containing between " +
            f"1 and 6 points. The input points has {numPoints} points." + 
            "This function is not designed to test 9-point circles.")

    assert type(arePointsValid) == bool, \
        (f"type(arePointsValid) == {type(arePointsValid)}, " + 
        f"arePointsValid == {arePointsValid}, circleType == {circleType}")

    assert type(userError) == list, \
        (f"type(userError) == {type(userError)}, userError == {userError}, " + 
        f"circleType == {circleType}")
    

    
    assert type(circleType) == str, (f"type(circleType) == {type(circleType)}, " +
        f"circleType == {circleType}")

    # Output format [arePointsValid:Boolean, userError:list, circleType:str]
    output = [arePointsValid, userError, circleType]
    return output

def filler():
    '''no funciton
    \nprvents below functions from expanding every time i make a loop or if.'''
    pass



def fourPoint(center:tuple, points:list):
    '''For calculating the error for a 4 point circle
    \ncenter:tuple, the center of the circle
    \npoints:list, 3 or 4 points around the circle to be tested.
    Returns a list with the degrees of error for each point.'''

    #make sure no more than 4 points were input
    if len(points) != 4 and len(points) != 3:
        raise TypeError("You must include 3 or 4 points.")
    
    validatePointList(points)

    #END LOOP

    pointError = [0.0]


    # calculate the error for each point except the first.
    for i in range(1, (len(points))):

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
    
    validatePointList(points)

    pointError = [0.0]

    # calculat ethe error for each posible 6-point
    for i in range(1, (len(points))):

        line1 = (points[0], center)
        line2 = (points[i], center)
        theta = findAngle(line1, line2)

        # determin which ideal 6-point is closets to input point

        posibleErrorValues = [theta - 60, theta - 120, theta - 180]
        minValue = numpy.abs(posibleErrorValues[0])
        minIndex = 0

        for j in range(1, (len(posibleErrorValues))):
            if numpy.abs(posibleErrorValues[j]) < minValue:
                minValue = numpy.abs(posibleErrorValues[j])
                minIndex = j
        
        pointError.append(posibleErrorValues[minIndex])
    
    assert len(pointError) == len(points), \
        (f"len(pointError) == {len(pointError)}, len(points) == {len(points)}")
    
    return pointError    

def findAngle(line1:list, line2:list):

    # check number of points in each line
    if len(line1) != 2:
        raise TypeError(f"line1 must include 2 points. You included " + 
        f"{len(line1)} points")

    elif len(line2) != 2:
        raise TypeError(f"line2 must include 2 points. You included " + 
        f"{len(line2)} points")
    
    # error check each line as a list of points
    validatePointList(line1, "line1")
    validatePointList(line2, "line2")
    

    m1 = findSlope(line1[0], line1[1])
    assert type(m1) == float, (f"type(m1) == {type(m1)}, m1 == {m1}")

    m2 = findSlope(line2[0], line2[1])
    assert type(m2) == float, (f"type(m2) == {type(m2)}, m2 == {m2}")


    # sorce: https://www.cuemath.com/geometry/angle-between-two-lines/
    theta = float(numpy.arctan((m1-m2)/(1+m1*m2)))

    assert type(theta) == float, \
        (f"type(theta) == {type(theta)}, theta == {theta}")
    
    return theta


def findSlope(point1:tuple, point2:tuple):

    # Error check the points
    validatePointList([point1, point2], "slopeInputs")

    # sorce: https://www.physicsclassroom.com/class/1DKin/Lesson-3/Determining-the-Slope-on-a-p-t-Graph
    slope = float((point2[1] - point1[1])/(point2[0]-point1[0]))

    assert type(slope) == float, (f"type(slope) == {type(slope)}, " + 
    f"slope == {slope}")

    return slope

def sumCheckScores(scores:list):
    
    totalScore = 0
    validCircle = True
    
    for i in scores:
        totalScore = float(totalScore + numpy.abs(i))

        if  numpy.abs(i) > 10:
            validCircle = False
        
    return [totalScore, validCircle]


if __name__ == "__main__":
    from wardingUtility import circleGen, pointGen, CENTER_KEY, CIRCLE_KEY

    circleDict = circleGen(10)

    circleList = circleDict[CIRCLE_KEY()]

    centerPoint = circleDict[CENTER_KEY()]
    
    inputs = []
    
    num3PointTests = 5

    num5PointTests = 5

    #generate values for the 3 point test
    for i in range(0, num3PointTests):
        inputs.append(pointGen(circleList, 3))

    print()
    print(" === 3 Points, unknown type === ")
    for i in range(0, num3PointTests):
        testPoints = inputs[i].copy()

        testOutput = main(centerPoint, testPoints)

        print(f"   {i+1}: "+
            f"\n      arePointsValid == {testOutput[0]}" +
            f"\n      userError == {testOutput[1]}" +
            f"\n      circleType == {testOutput[2]}")

    print()
    print(" === 3 Points, known 4-point === ")
    for i in range(0, num3PointTests):
        testPoints = inputs[i].copy()

        testOutput = main(centerPoint, testPoints, FOUR_POINT_KEY())

        print(f"   {i+1}: "+
            f"\n      arePointsValid == {testOutput[0]}" +
            f"\n      userError == {testOutput[1]}" +
            f"\n      circleType == {testOutput[2]}")

    print()
    print(" === 3 Points, known 6-point === ")
    for i in range(0, num3PointTests):
        testPoints = inputs[i].copy()

        testOutput = main(centerPoint, testPoints, SIX_POINT_KEY())

        print(f"   {i+1}: "+
            f"\n      arePointsValid == {testOutput[0]}" +
            f"\n      userError == {testOutput[1]}" +
            f"\n      circleType == {testOutput[2]}")

    print("\n ==== Generating new points ==== \n")

    inputs = []
    
    

    #generate values for the 3 point test
    for i in range(0, num5PointTests):
        inputs.append(pointGen(circleList, 5))

    print()
    print(" === 5 Points, unknown type === ")
    for i in range(0, num5PointTests):
        testPoints = pointGen(circleList, 5)

        testOutput = main(centerPoint, testPoints)

        print(f"   {i+1}: "+
            f"\n      arePointsValid == {testOutput[0]}" +
            f"\n      userError == {testOutput[1]}" +
            f"\n      circleType == {testOutput[2]}")

    print()
    print(" === 5 Points, known 6-point === ")
    for i in range(0, num5PointTests):
        testPoints = pointGen(circleList, 5)

        testOutput = main(centerPoint, testPoints, SIX_POINT_KEY())

        print(f"   {i+1}: "+
            f"\n      arePointsValid == {testOutput[0]}" +
            f"\n      userError == {testOutput[1]}" +
            f"\n      circleType == {testOutput[2]}")
    
    print()
    
