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
    print("Iteration: {}/{} = {}%".format(n, iterations, round((n / iterations) * 100, 4)))
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

bins = [i for i in range(-pack_size * 5, pack_size*5 + 2)]

plt.hist(data_points_list, bins=bins, density=True)
plt.show()

data_points_hist = np.histogram(data_points_list, bins=bins, density=True)

prob = data_points_hist[0]
positions = data_points_hist[1]

probabilities = []
prob_dict = {}
for i in range(41):
    pos = positions[i]
    p = prob[i]
    probabilities.append((pos, round(p * 100, 10)))
    if abs(pos) not in prob_dict:
        prob_dict[abs(pos)] = p
    else:
        prob_dict[abs(pos)] += p

sorted_prob_dict = sorted(prob_dict.items())

cum = 0
cum_probability = []
for i, j in sorted_prob_dict:
    cum += j
    cum_probability.append((i, round(cum * 100)))
    print(i, round(cum * 100, 6))


