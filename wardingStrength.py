
from msvcrt import SEM_NOALIGNMENTFAULTEXCEPT


def main(circleCords:list, powerMod=1):
    
    # Create ouput list
    ouput = []

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
    
    return segmentStrength


def calculateCurveHeight(base1:tuple, tip:tuple, base2:tuple):
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

