def main():
    pass

def fourPoint(circle:list, points:list):

    #make sure no more than 4 points were input
    if len(points) >= 4:
        raise TypeError("You may not include more than 4 points")
    
    # make sure points have the proper type and are in circle.
    for i in points:
        if type(i) != tuple:
            raise TypeError("All point but be in the form of tuples")

        elif (i in circle) == False:
            raise TypeError("All points in points must be in circle.")
    #END LOOP



if __name__ == "__main__":
    main()