"""Task 4: Stable Temperature Intervals.

This script identifies intervals of stable temperatures.
"""

temps = [18, 19, 21, 20, 22, 28, 30, 27,
         15, 16, 18, 17, 25, 24, 26, 10, 12, 11, 13, 12]

stable_temps = []
stable_start = 0

# В начале отрезок состоит только из первого измерения
min_temp = temps[0]
max_temp = temps[0]

for ind in range(1, len(temps)):
    # Обновляем минимум / максимум отрезка с учетом текущей температуры
    new_min = min(min_temp, temps[ind])
    new_max = max(max_temp, temps[ind])

    # Если разница > 4, то текущая температура начинает новый отрезок
    if new_max - new_min > 4:
        if ind - stable_start >= 3:
            stable_temps.append(temps[stable_start:ind])
        stable_start = ind
        min_temp = max_temp = temps[ind]
    # Если разница <= 4, то текущая температура продолжает текущий отрезок
    else:
        min_temp = new_min
        max_temp = new_max

# После цикла проверяем, нужно ли добавить последний отрезок
if len(temps) - stable_start >= 3:
    stable_temps.append(temps[stable_start:])

print(stable_temps)
