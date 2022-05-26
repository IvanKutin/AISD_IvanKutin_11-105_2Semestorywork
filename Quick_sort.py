import matplotlib.pyplot as plt
import time
import random


def Quick_sort(a, i=0, j=0):
    if j == 0:
        j = len(a) - 1
    m = i
    n = j
    while i != j:
        if a[i] > a[j]:
            a[i], a[j - 1] = a[j - 1], a[i]
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1
        else:
            i = i + 1
    if i - m > 1:
        Quick_sort(a, m, i - 1)
    if n - i > 1:
        Quick_sort(a, i + 1, n)
    return a


times = []

# test 1
a = []
for i in range(1000):
    a.append(random.randint(1, 1000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

# test 2
a = []
for i in range(10000):
    a.append(random.randint(1, 10000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

# test 3
a = []
for i in range(100000):
    a.append(random.randint(1, 100000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

print(times)

plt.xlabel('Количество чисел')
plt.ylabel('Время сортировки')
plt.plot([1000, 10000, 100000], times)
plt.show()
