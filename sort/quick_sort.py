def partition(A, start, end):
    pivot = A[end]
    partition_index = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[partition_index] = A[partition_index], A[i]
            partition_index += 1
    A[end], A[partition_index] = A[partition_index], A[end]
    
    return partition_index

def quick_sort(A, start, end):
    if start >= end: return 
    partition_index = partition(A, start, end)
    quick_sort(A, start, partition_index - 1)
    quick_sort(A, partition_index + 1, end)

