import cmath

# # phase = argument of z = x + yj
# print(cmath.phase(complex(-1.0, 0.0)))
# # 3.141592653589793
#
# # absolute value
# print(abs(complex(-1.0, 0.0)))
# # 1.0
#

###

z = complex(input())

tuple_polar = cmath.polar(z)

for i in tuple_polar:
    print(i)

###

n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))