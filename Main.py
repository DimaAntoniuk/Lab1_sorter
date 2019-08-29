from models.Vase import Vase

def merge(A, B):
    a = b = 0
    out = []
    while a < len(A) and b < len(B):
        if A[a].weight < B[b].weight:
            out.append(A[a])
            a += 1
        else:
            out.append(B[b])
            b += 1
    out += A[a:] + B[b:]
    return out

def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = int(len(A) / 2)
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

def selectionSort(A):
    for i in range(len(A)):
        min_i = i
        for j in range(i+1, len(A)):
            if A[j].volume > A[min_i].volume:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

arr = []

with File('input.txt', 'r') as input:
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

selectionSort(arr)

with File('output.txt', 'a+') as output:
    output.write('SELECTION SORT\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.material.find('\n') == -1:
            output.write('\n')

arr = mergeSort(arr)

with File('output.txt', 'a+') as output:
    output.write('MERGE SORT\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.material.find('\n') == -1:
            output.write('\n')
