import java_random
import matplotlib.pyplot as plt

packsize = 4
iterations = 1000000
random = java_random.Random()

n = 1
ranges = {}
datapoints = []

while n < iterations:
    x = random.nextInt(6) - random.nextInt(6)
    y = random.nextInt(6) - random.nextInt(6)
    offset = x if abs(x) > abs(y) else y
    datapoints.append(offset)
    if offset not in ranges:
        ranges[offset] = 1
    else:
        ranges[offset] += 1

    for i in range(packsize - 1):
        x += random.nextInt(6) - random.nextInt(6)
        y += random.nextInt(6) - random.nextInt(6)
        offset = x if abs(x) > abs(y) else y
        datapoints.append(offset)
        if offset not in ranges:
            ranges[offset] = 1
        else:
            ranges[offset] += 1
        n += 1

sorted_ranges = sorted(ranges.items())
total = 0
for i, j in sorted_ranges:
    total += j

sorted_normalised_ranges = [(i, j / total) for i, j in sorted_ranges]
print(sorted_normalised_ranges)

cum = 0
cum_ranges, x, y = [], [], []
for i, j in sorted_normalised_ranges:
    cum += j
    x.append(i)
    y.append(round(cum, 10) * 100)
    cum_ranges.append((i, round(cum, 10) * 100))

print(cum_ranges)
plt.plot(x, y, c='r')
plt.show()

plt.hist(datapoints, bins=20)
plt.show()