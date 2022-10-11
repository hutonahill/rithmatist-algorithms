# Accept the cords of a line of warding that re attaches to itslef 
# and a power moddifer.
def main(circleCords:list, powerMod = 1):
    '''circleCords: The coordinates for points on a line of warding.
    \npowerMod: a power modifier for the line of warding.
    \nReturn: a list of strengths of segments of the line of warding starting 
    with the second full segment counterclockwise from the first point in the 
    input list.'''

    # Loop through the circle cords and get the each arc group strength.
    groupStr = []
    for i in range(len(circleCords)):
        
        # Calculate group strength
        copyData = calculateCurveHeight(circleCords[i-2], circleCords[i-1], 
        circleCords[i])
        
        # Append data to list
        groupStr.append(copyData)
    
    # Loop through agean to get combine two arc strengths to 
    # get the arc strength of every segment.
    segmentStrength = []
    for i in range(len(groupStr)):

        # Add agacent group strength then apply powerMod
        copyData = (groupStr[i-1] + groupStr[i]) * powerMod

        # Append data to list
        segmentStrength.append(copyData)

    # shift segmentStrength so the fist segment starts with the first input cord
    segmentStrength = segmentStrength[2:] + segmentStrength[:2]
    
    return segmentStrength


def calculateCurveHeight(base1:tuple, tip:tuple, base2:tuple):
    '''calculate the height of a triangle
    \nbase1: one of the bases of a triangle
    \nbase2: the other base of a triangle
    \ntip: the third point of a triangle
    \nReturn: the height of the input triangle'''
    import numpy
   
    #find the magnitude
    def mag(a:tuple):
        return numpy.sqrt(a[0]**2 + a[1]**2)
       
    ac = tuple(numpy.subtract(tip,base1))

    ab = tuple(numpy.subtract(base1,base2))

    acDOTab = numpy.dot(ab,ac)

    acMag = mag(ac)
    abMag = mag(ab)

    # theta = arccos( the dot product of ac and ab devided by 
    # (the magnatude of ac * the magnatude of ab))
    theta = numpy.arccos(acDOTab/(acMag*abMag))

    height = numpy.sin(theta) * acMag

    return height


def wardStrCircleTesting (r, centerX = 0, centerY = 0):
    import wardingGen
    ''' Tests wardingStrength on a circle or radius "r" at ("centerX", "centerY")
    \n prints the strength of each segment as calculated to the command line 
    then prints the max and min strengths 
    \n max and min ignore final segment'''

    testOutput = main(wardingGen.circleGen(r, centerX, centerY), 1)

    max = [0, testOutput[0]]
    min = [0, testOutput[0]]
    for i in range(len(testOutput)):
        print(f"{i}: {testOutput[i]}")

        # Check if a new max is found.
        tempMax = max[1]
        if testOutput[i] > tempMax and i != (len(testOutput)-1):
            max = [i, testOutput[i]]
        
        # Check if a new min is found.
        tempMin = min[1]
        if testOutput[i] < tempMin and i != (len(testOutput)-1):
            min = [i, testOutput[i]]
    
    print(f"Max Str:\n   {max[0]}: {max[1]} \nMin Str:\n   {min[0]}: {min[1]}")
    print(f"Difrance: {max[1] - min[1]}" + 
    f"\n   {round((max[1] - min[1])/min[1]*100, 3)}% max error")
