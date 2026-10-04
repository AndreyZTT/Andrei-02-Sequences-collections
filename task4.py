"""Task 4: Stable Temperature Intervals.

This script identifies intervals of stable temperatures.
"""

temps = [18, 19, 21, 20, 22, 28, 30, 27,
         15, 16, 18, 17, 25, 24, 26, 10, 12, 11, 13, 12]

stable_temps = []

stable_start = None
stable_end = None

ind = 0
next_ind = 1

for t in temps:
    if next_ind < len(temps) and abs(temps[next_ind] - t) <= 4:
        if stable_start is None:
            stable_start = ind
        stable_end = next_ind
        ind += 1
        next_ind += 1
    else:
        if stable_start is not None:
            stable_temps.append(temps[stable_start:stable_end+1])
        stable_start = None
        stable_end = None
        ind += 1
        next_ind += 1

print(stable_temps)
