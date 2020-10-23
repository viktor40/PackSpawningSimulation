import java_random
import matplotlib.pyplot as plt
import numpy as np

pack_size = 4
iterations = 1000000
random = java_random.Random()

# list used to store the different distances from the pack centre for each pack spawn
data_points_list = []

n = 0
while n <= iterations:
    print("Iteration: {}/{}".format(n, iterations))
    x = random.nextInt(6) - random.nextInt(6)
    y = random.nextInt(6) - random.nextInt(6)
    offset = x if abs(x) > abs(y) else y
    data_points_list.append(offset)

    for i in range(pack_size - 1):
        x += random.nextInt(6) - random.nextInt(6)
        y += random.nextInt(6) - random.nextInt(6)
        offset = x if abs(x) > abs(y) else y
        data_points_list.append(offset)
    n += 1

bins = [i for i in range(-20, 22)]

plt.hist(data_points_list, bins=bins, density=True)
plt.show()

data_points_hist = np.histogram(data_points_list, bins=bins, density=True)

chances = data_points_hist[0]
positions = data_points_hist[1]

cum_chances = []
cum = 0
for i in range(41):
    pos = positions[i]
    chance = chances[i]
    cum += chance
    cum_chances.append((pos, round(cum * 100, 10)))

print(cum_chances)
