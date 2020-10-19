import numpy as np
import matplotlib.pyplot as plt

chances_x = {}
chances_xz = {}

pack_size = 4
iterations = 0

for j in range(6):
    for k in range(6):
        offset_abs = np.abs(j - k)
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
                    offset_abs = j + np.abs(m - n)
                    if offset_abs not in chances_x:
                        chances_x[offset_abs] = 1
                    else:
                        chances_x[offset_abs] += 1

                    iterations += 1


sorted_items = sorted(chances_x.items())
print(sorted_items)

sorted_x = []

for i, j in sorted_items:
    sorted_x.append((i, j / iterations))

print(sorted_x)
sorted_z = sorted_x
for i, j in sorted_x:
    for k, l in sorted_z:
        square_radius = max(i, k)
        if square_radius not in chances_xz:
            chances_xz[square_radius] = j * l
        else:
            chances_xz[square_radius] += j * l

sorted_items_xz = sorted(chances_xz.items())
cumulative_chances, x, z = [], [], []
cum = 0
for i, j in sorted_items_xz:
    cum += j
    x.append(i)
    z.append(round(cum, 10) * 100)
    cumulative_chances.append((i, round(cum, 10) * 100))

print(cumulative_chances)
plt.plot(x, z)
plt.show()
