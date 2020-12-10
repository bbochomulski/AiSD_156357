tablica = [6,3,9,0,4]
# print(f'Source: {tablica}')

def bubblesort(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i]<l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def selectionsort(l):
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n-1):
            if l[j] < l[min_index]:
                min_index = j
                l[j], l[min_index] = l[min_index], l[j]
    return l

def insertsort(l):
    n = len(l)
    for i in range(1,n-1):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j-1
            l[j+1] = key
    return l

def bubblesort_desc(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i]>l[j]:
                l[i], l[j] = l[j], l[i]
    return l

def selectionsort_desc(l):
    n = len(l)
    for i in range(n):
        max_index = i
        for j in range(i+1,n-1):
            if l[j] > l[max_index]:
                max_index = j
                l[j], l[max_index] = l[max_index], l[j]
    return l

def insertsort_desc(l):
    n = len(l)
    for i in range(1,n-1):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] < key:
            l[j+1] = l[j]
            j = j-1
            l[j+1] = key
    return l

assert bubblesort(tablica) == [0, 3, 4, 6, 9]
assert selectionsort(tablica) == [0, 3, 4, 6, 9]
assert insertsort(tablica) == [0, 3, 4, 6, 9]
assert bubblesort_desc(tablica) == [9, 6, 4, 3, 0]
assert selectionsort_desc(tablica) == [9, 6, 4, 3, 0]
assert insertsort_desc(tablica) == [9, 6, 4, 3, 0]


        