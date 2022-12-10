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
        userError = fourPoint(centerPoint, points)

        if userError <= ACCEPTABLE_DEGREES_ERROR():
            arePointsValid = True
        else:
            arePointsValid = False
    
    # Known 6-point circle
    elif circleType == SIX_POINT_KEY():
        userError = sixPoint(centerPoint, points)

        if userError <= ACCEPTABLE_DEGREES_ERROR():
            arePointsValid = True
        else:
            arePointsValid = False

    # if the type of circle is not known try to detect it
    else:

        #save the len of points so we only have to calculate it once
        numPoints = len(points)

        # all circles with only 1 point are valid
        if numPoints == 1:
            arePointsValid = True
            userError = [0.0]
        
        # If there are between 2 and 4 points attempt to determin which type
        # the circle is
        elif 2 <= numPoints <= 4:
            fourScoreList = fourPoint(centerPoint, points)
            
            assert type(fourScoreList) == list, \
                (f"type(fourScoreList) == {type(fourScoreList)}, " + 
                f"fourScoreList == {fourScoreList}")

            copyData = sumCheckScores(fourScoreList)

            fourScore = copyData[0]

            validFourFlag = copyData[1]


            sixScoreList = sixPoint(centerPoint, points)

            assert type(sixScoreList) == list, \
                (f"type(sixScore) == {type(sixScoreList)}, " + 
                f"sixScore == {sixScoreList}")
            
            copyData = sumCheckScores(sixScoreList)

            sixScore = copyData[0]

            validSixFlag = copyData[1]

            # if the four and six scores are the same,
            # dont return a circle type
            if fourScore == sixScore:

                userError = fourScoreList

                arePointsValid = validFourFlag

            # if the user error is lower when the circle is assumed to be a 
            # 4-point, return that the circle is a 4-point
            elif fourScore < sixScore:
                userError = fourScoreList

                arePointsValid = validFourFlag
                
                circleType = FOUR_POINT_KEY()

            # if the user error is lower when the circle is assumed to be a 
            # 6-point, return that the circle is a 6-point
            else:
                userError = sixScoreList

                arePointsValid = validSixFlag
                
                circleType = SIX_POINT_KEY()
        
        # if 5 - 6 points are given, assume its a 6 point
        elif 5 <= numPoints <= 6:
            sixScoreList = sixPoint(centerPoint, points)

            assert type(sixScoreList) == list, \
                (f"type(sixScore) == {type(sixScoreList)}, " + 
                f"sixScore == {sixScoreList}")
            
            copyData = sumCheckScores(sixScoreList)

            sixScore = copyData[0]

            validSixFlag = copyData[1]

            userError = sixScoreList

            arePointsValid = validSixFlag
            
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

    for i in range(0, 5):
        testPoints = pointGen(circleList, 3)

        testInputs = [testPoints, 'unknown']
        inputs.append(testInputs)
    
    for i in range(0, 5):
        testPoints = pointGen(circleList, 5)

        testInputs = [testPoints, 'unknown']
        inputs.append(testInputs)
    

    print()
    for i in range(len(inputs)):
        currentInput = inputs[i]
        testOutput = main(centerPoint, currentInput[0], currentInput[1])

        print(f"{i}: "+
            f"\n   arePointsValid == {testOutput[0]}" +
            f"\n   userError == {testOutput[1]}" +
            f"\n   circleType == {testOutput[2]}" + 
            "\n")
    print()