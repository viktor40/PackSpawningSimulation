import numpy as np
import matplotlib.pyplot as plt

chances_x = {}
chances_xz = {}

pack_size = 4
iterations = 0

for j in range(6):
    for k in range(6):
        offset_abs = j - k
        if offset_abs not in chances_x:
            chances_x[offset_abs] = 1
        else:
            chances_x[offset_abs] += 1

        iterations += 1


for i in range(pack_size - 1):
    sorted_items = sorted(chances_x.items())
    for j, k in sorted(chances_x.items()):
        for l in range(k):
            for m in range(6):
                for n in range(6):
                    offset_abs = j + (m - n)
                    if offset_abs not in chances_x:
                        chances_x[offset_abs] = 1
                    else:
                        chances_x[offset_abs] += 1

                    iterations += 1


sorted_items = sorted(chances_x.items())

sorted_x = []

for i, j in sorted_items:
    sorted_x.append((i, j / iterations))

print(sorted_x)
sorted_z = sorted_x
for i, j in sorted_x:
    for k, l in sorted_z:
        square_radius = i if abs(i) > abs(k) else k
        if square_radius not in chances_xz:
            chances_xz[square_radius] = j * l
        else:
            chances_xz[square_radius] += j * l

sorted_items_xz = sorted(chances_xz.items())
print(sorted_items_xz)
cumulative_chances, x, z = [], [], []
cum = 0

in_between = 0
for i, j in sorted_items_xz:
    cum += j
    cumulative_chances.append((i, round(cum, 10) * 100))
    x.append(i)
    z.append(round(cum, 10) * 100)
    if i == -5:
        in_between -= cum

    elif i == 5:
        in_between += cum

print(cumulative_chances)
plt.plot(x, z)
plt.show()

print(in_between)