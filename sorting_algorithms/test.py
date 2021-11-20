from random import randint, seed
import insertionSort

ls = None


def main(_seed):
    print('Executing python default sorting algorithm')
    ls = list_gen(10, _seed=_seed)
    print(sorted(ls))

    print('Executing sorting algorithm')
    ls = insertionSort.insertion_sort([e for e in list_gen(10, _seed=_seed)])
    print(ls)
    return


def list_gen(n, _seed=None):
    '''
    Function that returns a generator of a list.
    The returned list will be the same for each call.
    '''
    if _seed:
        seed(_seed)
    return (randint(-x, x) for x in range(n))


if __name__ == '__main__':
    main(_seed=randint(1, 10000))
