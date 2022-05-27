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
for i in range(30000):
    a.append(random.randint(1, 30000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

# test 2
a = []
for i in range(60000):
    a.append(random.randint(1, 60000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

# test 3
a = []
for i in range(90000):
    a.append(random.randint(1, 90000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)


# test 4
a = []
for i in range(120000):
    a.append(random.randint(1, 120000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)


# test 5
a = []
for i in range(150000):
    a.append(random.randint(1, 150000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)



# test 6
a = []
for i in range(180000):
    a.append(random.randint(1, 180000))
time1 = time.time()
Quick_sort(a)
times.append(time.time() - time1)

print(times)

plt.xlabel('Количество чисел')
plt.ylabel('Время сортировки (в секундах )')
plt.plot([30000, 60000, 90000,120000,150000,180000], times,marker ='o')
plt.show()
