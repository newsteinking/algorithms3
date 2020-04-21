#implementation of max heap

def build_heap(x):
    n = len(x)
    for i in reversed(range(n//2)):
        max_heapify(x, n, i)

def max_heapify(x, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and x[i] < x[l]:
        largest = l

    if r < n and x[largest] < x[r]:
        largest = r

    if largest != i:
        x[largest], x[i] = x[i], x[largest]
        max_heapify(x, n, largest)


def heap_sort(x):
    n = len(x)
    build_heap(x)
    for i in range(n-1, 0, -1):
        x[0], x[i] = x[i], x[0]
        max_heapify(x, i, 0)

