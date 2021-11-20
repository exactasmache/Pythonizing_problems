def insertion_sort(ls):
    '''
    Function that receives a list and returns the same list sorted
    in increasing order using the insertion sort algorithm
    '''
    n = len(ls)
    for i in range(1, n):
        binaryInsert(i, ls)
        linearInsert(i, ls)
    return ls


def linearInsert(i, ls):
    binaryInsert(i, ls)


def binaryInsert(i, ls):
    for j in range(i, 0, -1):
        if ls[j] < ls[j-1]:
            ls[j], ls[j-1] = ls[j-1], ls[j]
        else:
            return
