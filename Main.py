from models.Vase import Vase
import time

def merge(A, B):
    global merge_swap
    global merge_compare
    a = b = 0
    out = []
    while a < len(A) and b < len(B):
        merge_compare += 1
        if A[a].weight <= B[b].weight:
            out.append(A[a])
            a += 1
            merge_swap += 1
        else:
            out.append(B[b])
            b += 1
            merge_swap += 1
    out += A[a:] + B[b:]
    merge_swap += len(A)-a + len(B)-b
    return out

def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = int(len(A) / 2)
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

def selectionSort(A):
    global selection_swap
    global selection_compare
    for i in range(len(A)):
        min_i = i
        for j in range(i+1, len(A)):
            selection_compare += 1
            if A[j].volume > A[min_i].volume:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
        selection_swap += 1

arr = []

with open('input.txt', 'r') as input:
    fields = input.read().split(',')
    i = 0
    volume = 0
    weight = 0
    for field in fields:
        i += 1
        if(i % 3 == 1):
            volume = int(field)
        if(i % 3 == 2):
            weight = int(field)
        if(i % 3 == 0):
            arr.append(Vase(volume, weight, field))

selection_begin = time.time()
selection_compare = 0
selection_swap = 0
selectionSort(arr)
selection_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('SELECTION SORT\n')
    output.write('Time: ' + str(selection_finish-selection_begin) + '\n')
    output.write('Compares: ' + str(selection_compare) + '\n')
    output.write('Swaps: ' + str(selection_swap) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.material.find('\n') == -1:
            output.write('\n')

merge_begin = time.time()
merge_compare = 0
merge_swap = 0
arr = mergeSort(arr)
merge_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('MERGE SORT\n')
    output.write('Time: ' + str(merge_finish - merge_begin) + '\n')
    output.write('Compares: ' + str(merge_compare) + '\n')
    output.write('Swaps: ' + str(merge_swap) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.material.find('\n') == -1:
            output.write('\n')
