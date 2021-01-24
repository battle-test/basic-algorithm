a = [1,2,3,4,5,6,7,8,9]
b = [0 if x % 2 != 0 else x**2 for x in a]

# [0, 4, 0, 16, 0, 36, 0, 64, 0]
# b = []
# for x in a:
#     if a[x] % 2 != 0:
#         b.append(0)
#     else:
#         b.append(a[x]**2)
