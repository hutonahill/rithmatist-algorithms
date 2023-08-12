import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time

def segmentLine(line:list) -> list:
    """
    Args:
        - line (list): a list of points (x, y) as tuples that make up a line
    
    Returns:
        - segmentedLine (list): a list of line segments. 
            Each segment consists of a start point, a midpoint, and an end point
            every point appears in 3 segments, as a start point, as a midpoint, and as an end point
            (except for point at the begining and the end.)
        
    """
    
    # If the code is debugging, check and make sure the input is in the proper
    # format.
    if __debug__:
        if (type(line) != list):
            raise TypeError("line must be a list")

        for i in line:
            if (type(i) != tuple):
                raise TypeError("line must be a list of points as tuples")
            
            if (len(i) != 2):
                raise TypeError("A point may only have two componants, x and y.")
    #END __DEBUG__
    
    
                
    # create a list to output to.
    segmentedLine = []
    
    # loop though every set of three points
    for i in range(len(line) - 2):
        segment = [line[i], line[i+1], line[i+2]]
        
        # Add the current set of threee points to the output list
        segmentedLine.append(segment)
    
    return segmentedLine

def calculate_angle(p1: tuple, p2: tuple, p3: tuple) -> np.float64:
    """
    Calculate the angle formed by three points.
    
    Args:
        p1 (tuple): First point (x, y).
        p2 (tuple): Second point (x, y), forming the vertex of the angle.
        p3 (tuple): Third point (x, y).
        
    Returns:
        np.float64: Angle in degrees.
    """
    v1 = np.array(p1) - np.array(p2)
    v2 = np.array(p3) - np.array(p2)
    
    # Normalize vectors
    v1_normalized = v1 / np.linalg.norm(v1)
    v2_normalized = v2 / np.linalg.norm(v2)
    
    # Calculate dot product of normalized vectors
    dot_product = np.dot(v1_normalized, v2_normalized)
    
    # Ensure dot product is within valid range for arccosine
    dot_product = np.clip(dot_product, -1.0, 1.0)
    
    # Calculate the angle in radians using the arccosine
    angle_rad = np.arccos(dot_product)
    
    # Convert the angle from radians to degrees
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

def scoreSegments(segmentedLine:list) -> list:
    """
    Score the segments of a line based on the angle formed by three points in each segment.
    
    Args:
        segmentedLine (list): A list of line segments. Each segment contains 3 points.

    Returns:
        list: A list of scores. Each score correlates with the same index on the input line.
    """
    segmentScores = []
    
    for i in range(len(segmentedLine)):
        targetSegment = segmentedLine[i]
        angle = calculate_angle(targetSegment[0], targetSegment[1], targetSegment[2])
        complementaryAngle = np.float32(180.0) - abs(angle)
        score = complementaryAngle / np.float32(180.0)
        score = np.float32(1.0) - score
        segmentScores.append(score)
    
    return segmentScores
        
def combine_segment_scores(line:list, three_point_segments:list, three_point_scores:list) -> list:
    """
    Combine the scores of three-point segments to produce a list of two-point segment scores.
    
    Args:
        line (list): Original line points.
        three_point_segments (list): List of three-point segments, where each segment is a list of tuples.
        three_point_scores (list): List of scores corresponding to the three-point segments.
        
    Returns:
        list: List of tuples with start and end points along with combined scores for two-point segments.
    """
    
    # Initialize a list to store combined segment scores
    combined_scores = []
    
    # Calculate the score for the first two point segment
    combined_scores.append((line[0], line[1], three_point_scores[0]))
    
    # Loop through every two point segment except the first and the last.
    for i in range(1, len(line) - 2):
        startPoint = line[i]
        endPoint = line[i+1]
        
        assert type(startPoint) == tuple, (f"type(startPoint) == {type(startPoint)}")
        assert type(endPoint) == tuple, (f"type(endPoint) == {type(endPoint)}")
        
        score = (three_point_scores[i-1] + three_point_scores[i]) / 2
        
        compiledSegment = (startPoint, endPoint, score)
        
        combined_scores.append(compiledSegment)
    
    # Calculate the score for the last two point segment
    finalSegment = (line[-2], line[-1], three_point_scores[-1])
    
    combined_scores.append(finalSegment)
    
    return combined_scores
    
    
    
        

def distance_between_points(point1: tuple, point2: tuple):
    """
    Calculate the Euclidean distance between two points in a 2D space.
    
    Args:
        point1 (tuple): First point (x1, y1).
        point2 (tuple): Second point (x2, y2).
        
    Returns:
        float: Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_average_distance(line: list):
    """
    Calculate the average distance between consecutive points in a line.
    
    Args:
        line (list): List of points [(x1, y1), (x2, y2), ...].
        
    Returns:
        float: Average distance between points in the line.
    """
    total_distance = 0
    for i in range(len(line) - 1):
        segment_length = distance_between_points(line[i], line[i+1])
        total_distance += segment_length
    
    average_length = total_distance / (len(line) - 1)
    return average_length

def generate_straight_line(line: list, point_separation_distance: float):
    """
    Generate a straight line based on the input line and point separation distance.
    
    Args:
        line (list): List of points [(x1, y1), (x2, y2), ...].
        point_separation_distance (float): Desired distance between consecutive points.
        
    Returns:
        list: Corrected straight line as a list of tuples [(x1, y1), (x2, y2), ...].
    """
    average_length = calculate_average_distance(line)
    
    # Convert the list of points to a NumPy array
    points_array = np.array(line)
    
    # Separate x and y coordinates
    x = points_array[:, 0]
    y = points_array[:, 1]
    
    # Reshape x to a 2D array
    x = x.reshape(-1, 1)
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(x, y)
    
    # Calculate the direction vector along the line
    direction_vector = np.array([1, model.coef_[0]])
    normalized_direction_vector = direction_vector / np.linalg.norm(direction_vector)
    
    # Calculate the number of points to generate based on the input line length
    num_points = int(np.ceil(distance_between_points(line[0], line[-1]) / point_separation_distance))
    
    # Generate new points along the line with the specified point separation distance
    new_points = []
    for i in range(num_points):
        new_point = line[0] + normalized_direction_vector * point_separation_distance * i
        new_points.append(tuple(new_point))  # Convert the new point to a tuple and append
    
    return new_points



def display_line(original_points:list, corrected_line:list, new_points:list, imperfection_score:float):
    """
    Display the original points, corrected line, and new points using matplotlib.
    
    Args:
        original_points (list): List of original input points.
        corrected_line (list): List of corrected points forming a straight line.
        new_points (list): List of new points generated along the straight line.
        imperfection_score (float): The imperfection score of the imperfect line.
    """
    # Convert the points to NumPy arrays
    original_points = np.array(original_points)
    corrected_line = np.array(corrected_line)
    new_points = np.array(new_points)
    
    # Plot the original points in red
    plt.scatter(original_points[:, 0], original_points[:, 1], color='red', label='Original Points')
    
    # Plot the corrected straight line in blue
    plt.plot(corrected_line[:, 0], corrected_line[:, 1], color='blue', label='Corrected Straight Line')
    
    # Plot the new points in green
    plt.scatter(new_points[:, 0], new_points[:, 1], color='green', label='New Points')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    # Add the imperfection score to the plot
    plt.text(0.5, 1.05, f'Imperfection Score: {imperfection_score:.4f}', transform=plt.gca().transAxes,
             horizontalalignment='center', fontsize=12)
    
    plt.show()


def calculatePerpendicularDistance(point, line_point1, line_point2):
    """
    Calculate the perpendicular distance from a point to a line segment defined by two points.

    Args:
        point (tuple): Point for which to calculate the distance (x, y).
        line_point1 (tuple): First point of the line segment (x1, y1).
        line_point2 (tuple): Second point of the line segment (x2, y2).

    Returns:
        float: Perpendicular distance from the point to the line segment.
    """
    x, y = point
    x1, y1 = line_point1
    x2, y2 = line_point2
    
    # Calculate the length of the line segment
    line_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Handle the case when the line segment has zero length (single point)
    if line_length == 0:
        return np.sqrt((x - x1)**2 + (y - y1)**2)
    
    # Calculate parameter t that represents the projection of the point onto the line
    t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / line_length**2
    t = np.clip(t, 0, 1)  # Clip t to [0, 1] to handle points outside the line segment
    
    # Calculate the closest point on the line segment
    closest_point = (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    
    # Calculate the perpendicular distance from the point to the line segment
    distance = np.sqrt((x - closest_point[0])**2 + (y - closest_point[1])**2)
    
    return distance

def calculateLineImperfection(imperfect_line, perfect_line):
    """
    Calculate the imperfection of an imperfect line compared to a perfect line.

    Args:
        imperfect_line (list): List of points representing the imperfect line.
        perfect_line (list): List of points representing the perfect line.

    Returns:
        float: A value representing the imperfection of the imperfect line.
    """
    total_distance = 0
    valid_points = 0
    
    for imperfect_point in imperfect_line:
        # Calculate the perpendicular distance from the imperfect point to the line defined by the perfect endpoints
        try:
            distance = calculatePerpendicularDistance(imperfect_point, perfect_line[0], perfect_line[-1])
            total_distance += distance
            valid_points += 1
        except ZeroDivisionError:
            # Handle the case where a perpendicular line cannot be calculated (division by zero)
            pass
    
    if valid_points == 0:
        return 0  # No valid points, return 0 imperfection
    
    # Calculate the average perpendicular distance as a measure of imperfection
    average_distance = total_distance / valid_points
    return average_distance


# Example usage
user_lines = [
    (1, 3),
    (2, 5),
    (3, 7),
    (4, 9),
    (5, 11),
    (6, 12),
    (7, 14),
    (8, 16),
    (9, 18),
    (10, 20),
    (11, 21),
    (12, 23),
    (13, 25),
    (14, 27),
    (15, 28),
    (16, 30),
    (17, 32),
    (18, 34),
    (19, 36),
    (20, 38),
    (21, 39),
    (22, 41),
    (23, 43),
    (24, 44),
    (25, 46),
    (26, 48),
    (27, 50),
    (28, 51),
    (29, 53),
    (30, 57),
    (31, 57),
    (32, 58),
    (33, 60),
    (34, 62),
    (35, 64),
    (36, 65),
    (37, 67),
    (38, 69),
    (39, 71),
    (40, 72)
]

# determin the average distance between points
distance = calculate_average_distance(user_lines)

# generate a corrected, perficly straight version of the line
corrected_line = generate_straight_line(user_lines, distance)

# split the line into three point segments
threePointSegments = segmentLine(corrected_line)

# gereate a score for every three point segment
segmentScores = scoreSegments(threePointSegments)

# compile the three point scores into scored two point segments
finalLine = combine_segment_scores(corrected_line, threePointSegments, segmentScores)


# display the results
# lowestExcepableAngle = 179.9999
# highestExceptableAngle = 180.0001
# lowAngleCounter = 0
# highAngleCounter = 0
# for i in threePointSegments:
#     angle = calculate_angle(i[0], i[1], i[2])
#     print(angle)
    
#     if (angle < lowestExcepableAngle):
#         lowAngleCounter += 1
#     elif (angle > highestExceptableAngle):
#         highAngleCounter +=1

# print(f"Angles that are lower than {lowestExcepableAngle}: {lowAngleCounter}")
# print(f"Angles that are higher than {highestExceptableAngle}: {highAngleCounter}")



minScore = 1
maxScore = 0
for i in finalLine:
    
    score = i[2]
    
    if (score < minScore):
        minScore = score
    
    if (score> maxScore):
        maxScore = score
    
    print(f"{score:.6f}")
print(f"Min Score: {minScore:.6f}")
print(f"Max Score: {maxScore:.6f}")

#display_line(user_lines, corrected_line, corrected_line, score)