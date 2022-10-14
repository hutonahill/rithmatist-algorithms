
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

Eq1 = [(App[1] - Bp[1])**2 + (App[0] - Bp[0])**2], [(App[1] - B[1])**2 + (App[0] - B[0])**2]
Eq2 = [(Cpp[1] - Bp[1])**2 + (Cpp[0] - Bp[0])**2], [(Cpp[1] - B[1])**2 + (Cpp[0] - B[0])**2]

Eq3 = [(App[1] - Cp[1])**2 + (App[0] - Cp[0])**2], [(App[1] - C[1])**2 + (App[0] - C[0])**2]
Eq4 = [(Bpp[1] - Cp[1])**2 + (Bpp[0] - Cp[0])**2], [(Bpp[1] - C[1])**2 + (Bpp[0] - C[0])**2]

Eq5 = [(Bpp[1] - Ap[1])**2 + (Bpp[0] - Ap[0])**2], [(Bpp[1] - A[1])**2 + (Bpp[0] - A[0])**2]
Eq6 = [(Cpp[1] - Ap[1])**2 + (Cpp[0] - Ap[0])**2], [(Cpp[1] - A[1])**2 + (Cpp[0] - A[0])**2]

Eq7 = A, Ap * (-1)
Eq8 = B, Bp * (-1)
Eq9 = C, Cp * (-1)