
# System of equations for a 9 point circle.

# Variables, variables should be point on a carteshan plane
A = ()
Ap = ()
App = ()
B = ()
Bp = ()
Bpp = ()
C = ()
Cp = ()
Cpp = ()


Bpp[1]**2 - 2 * Bpp[1] * A[1] + Bpp[0]**2 - 2 * Bpp[0] * A[1],
Cpp[1]**2 - 2 * Cpp[1] * A[1] + Cpp[0]**2 - 2 * Cpp[0] * A[1]

Bpp[1]**2 - 2 * Bpp[1] * Ap[1] + Bpp[0]**2 - 2 * Bpp[0] * Ap[1],
Cpp[1]**2 - 2 * Cpp[1] * Ap[1] + Cpp[0]**2 - 2 * Cpp[0] * Ap[1]

# for 9 given points i can eliminate all posible arangements as what point 
# corisponds to what is determined by the order of the points around the circle.
# 
# symilerly we can condence 8 points down to 8 posibilities by going through 
# which gap between points the last point would go.
# 
# 7 is 7^2 = 49 options
# 
# 6 is 6^3 = 216
# 
# 5 is 5^4 = 625
# 
# 4 is 4^5 = 1024
# 
# 3 is 3^6 = 729
# 
# and 2 is always posible 
# 
# that brings us to  2,643
