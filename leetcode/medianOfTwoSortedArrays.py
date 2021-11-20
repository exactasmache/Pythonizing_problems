from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) \
     -> float:
        '''
            Start calculating i_med = n+m//2
            Iterate the arrays in paralell, when the 'med' element is reached
            odd  : [1 '2 3] -> 1;           return [med]
            even:  [1 2 '3 4] -> 'med' = 2  return ([med-1] + [med]) /2

            When iterating, we can have several combinations:
                'med' is reached and there are no more elements in num1
                'med' is reached and there are no more elements in num2
                'med' is reached and there are still elements in num1 and num2
                there are no more elements in num1 but 'med' is > 0
                there are no more elements in num2 but 'med' is > 0
            In the last two cases it could happen (taking num_i):
                'med' == 0, so we have to retrieve the previous element.
                'med' == 1, so we have to retrieve 'med' and 'med'-1 from num_j

            Every combination can be also combined with:
                n+m is odd
                n+m is even
        '''
        # print(f'nums1 = {nums1}\nnums2 = {nums2}')
        n = len(nums1)
        m = len(nums2)
        if n == 0:
            med, mod = divmod(m, 2)
            if mod == 0:
                # n+m is even
                return (nums2[med-1] + nums2[med])/2
            return nums2[med]

        # n > 0
        if m == 0:
            med, mod = divmod(n, 2)
            if mod == 0:
                # n+m is even
                return (nums1[med-1] + nums1[med])/2
            return nums1[med]

        med, mod = divmod(n+m, 2)
        # print(f'med = {med}, mod = {mod}')

        id1 = 0
        id2 = 0
        last = None
        while True:
            # print(f'nums1[{id1}] = {nums1[id1]}, nums2[{id2}] = {nums2[id2]}')
            if nums1[id1] < nums2[id2]:
                last = nums1[id1]
                id1 += 1
                med -= 1
                if id1 == n:                                # Revisar si med-1 puede estar en num1
                    if mod == 0:                            # n+m is even
                        if med > 0:                         # If med > 0, med-1 and med are retrieved from num2
                            last = nums2[id2+med-1]
                        return (last + nums2[id2+med])/2    # Else, we have to use 'last'
                    else:
                        return nums2[id2+med]               # next is in num2

            else:
                last = nums2[id2]
                id2 += 1
                med -= 1
                if id2 == m:
                    if mod == 0:                            # n+m is even
                        if med > 0:                         # If med > 0, med-1 and med are retrieved from num1
                            last = nums1[id1+med-1]
                        return (last + nums1[id1+med])/2    # Else, we have to use 'last'
                    else:
                        return nums1[id1+med]               # next is in num2

            if med == 0:
                # The next element is med
                if mod == 0:                                # n+m is even
                    if nums1[id1] < nums2[id2]:             
                        return (last + nums1[id1])/2        # next is in num1
                    return (last + nums2[id2])/2            # next is in num2
                else:
                    if nums1[id1] < nums2[id2]:
                        return nums1[id1]                   # next is in num1
                    return nums2[id2]                       # next is in num2
