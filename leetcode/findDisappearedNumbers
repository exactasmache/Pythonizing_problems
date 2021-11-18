from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
            The very first solution a came up is just iterate over
            the list getting the maximum element, i.e., n, and then,
            creating a set of the elements from 1 to n, iterate over
            nums removing the elements seen from the set.

            Another approach is to transform the list in a set (removing
            repeated that way) and iterate from 1 to n = len(nums)
            noting those missing elements.
        '''
        snums = set(nums)
        sol = []
        for i in range(1, len(nums)+1):
            if i not in snums:
               sol.append(i)
        return sol


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    solver = Solution()
    sol = solver.findDisappearedNumbers(nums)

    print(sol)
