
def main():
    pass

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

