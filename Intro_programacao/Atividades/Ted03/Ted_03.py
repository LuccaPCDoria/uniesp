import math

A = 2
B = 7
C = 3.5
L = False
V = True

# B = A * C e (L ou V)
print((B == A * C) and (L or V))

# B > A ou B = pot(A, A)
print(B > A or B == A**A)

# L e B div A >= C ou não A <= C
print(L and B // A >= C or not A <= C)

# não L ou V e rad(A + B) >= C
print(not L or V and math.sqrt(A + B) >= C)

# B/A = C ou B/A <> C
print(B / A == C or B / A != C)

# L ou pot(B, A) <= C * 10 + A * B
print(L or B**A <= C * 10 + A * B)
