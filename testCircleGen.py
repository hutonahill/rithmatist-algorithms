

# Returns a list of cords of a circle 
# with each point seperated by 1 unit of circomfrence
# returned list will contane a number of items eqle to the
# circumference (erhaps +1?)
def testCircleGen(radius, centerX =0, centerY=0):
    import math
    import numpy

    # Calculate circumference
    circumference = 2 * math.pi * radius

    #calculate the num of radians
    rad = 2 * math.pi

    #calculate the radians per unit in the circumference
    radPerUnit = rad/circumference

    cordList = []
    
    for theta in numpy.arange(0,rad,radPerUnit):

        # Calculate xy cords assuming center is 0,0.
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        # Shift cords to account for posible difrent center.
        cords = (x + centerX, y + centerY)

        cordList.append(cords)
    
    return cordList

testCircle = testCircleGen(5)
for i in range(len(testCircle)):
    print(f"{i}: {testCircle[i]}")
        