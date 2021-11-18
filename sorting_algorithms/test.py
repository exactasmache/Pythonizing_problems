from random import randint, seed
import insertionSort

ls = None

def main(_seed):
    print('Executing python default sorting algorithm')
    print(sorted(list_gen(_seed)))

    print('Executing sorting algorithm')
    insertionSort.insertion_sort(list_gen(_seed))
    return


def list_gen(n=10, _seed=None):
    '''
    Function that returns a generator of a list.
    The returned list will be the same for each call.
    '''
    print(n, _seed)
    return []
    if _seed:
        seed(_seed)
    return (randint(-x, x) for x in range(n))


if __name__ == '__main__':
    main(_seed=randint(1, 10000))
