from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            target = 12
            nums   = [0, 1, 3, 4, 5, 7, 9, 10, 15]
            I sort the list in n.log(n).
            Then I can iterate from the end until the first element
            lower or equal to target, and also from the begining
            looking for a marriage.
        '''
        nums = [(idx, nums[idx]) for idx in range(len(nums))]
        nums.sort(key=lambda x: x[1])
        l = 0
        r = len(nums)-1

        while nums[r][1] + nums[l][1] > target:
            r -= 1
        while nums[r][1] + nums[l][1] < target:
            l += 1
        print(nums[l:r])

        while r > l:
            suma = nums[l][1] + nums[r][1]
            print(f'{suma} = {nums[l][1]} + {nums[r][1]}')

            if suma == target:
                return [nums[l][0], nums[r][0]]

            if suma > target:
                r -= 1
                l -= 1
            else:
                l += 1

        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    solver = Solution()
    sol = solver.twoSum(nums, target)

    print(sol)
