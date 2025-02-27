a = min([12, -2, 32, -4 * 5])
b = max([12, -2, 32, -4 * 5])
print(a)  # -20
print(b)  # 32

##############################
a = min([12, 'apple', 223, 'B'], key=str)
print(a)  # 12
b = min([12, 'apple', 223, 'B'], key=lambda c: len(str(c)))
print(b)  # B
