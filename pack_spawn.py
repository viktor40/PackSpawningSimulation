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

chances_z = chances_x
for i, j in sorted(chances_x.items()):
    for k, l in sorted(chances_z.items()):
        square_radius = max(i, k)
        if square_radius not in chances_xz:
            chances_xz[square_radius] = (j + l) / 2
        else:
            chances_xz[square_radius] += (j + l) / 2

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

    chances_z = chances_x
    for o, p in sorted(chances_x.items()):
        for q, r in sorted(chances_z.items()):
            square_radius = max(o, q)
            if square_radius not in chances_xz:
                chances_xz[square_radius] = (p + r) / 2
            else:
                chances_xz[square_radius] += (p + r) / 2

sorted_items = sorted(chances_xz.items())
print(sorted_items)

chances = []

iterations *= 2
for i, j in sorted_items:
    chances.append((i, j / iterations))

cum = 0
cumulative_chances = []
blocks = []
overview = []
for i, j in chances:
    cum += j
    blocks.append(i)
    cumulative_chances.append(cum * 100)
    overview.append((i, cum * 100))

print(overview)

plt.plot(blocks, cumulative_chances)
plt.show()

print(iterations)
