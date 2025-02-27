def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

############################################

import math
a = 15
b = 5
print(math.gcd(b, a))
