from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            Very naive solution with some prunes
            Tempral complexity: O(n^4)
            Spatial complexity: combinatorial(n,4)
        '''
        nums.sort()
        n = len(nums)

        # Prune 1
        if n < 4:
            return []

        # Prune 2
        nums2 = nums[:1]
        last = nums[0]
        count = 0
        for i in range(1, n):
            elem = nums[i]
            if elem != last:
                nums2.append(elem)
                count = 0
                continue
            count += 1
            if count < 4:
                nums2.append(elem)
        nums = nums2
        n = len(nums)

        # Prune 3
        if nums[n-4] + nums[n-3] + nums[n-2] + nums[n-1] < target:
            return []

        # Prune 4
        for i in range(3, len(nums)):
            if nums[0] + nums[1] + nums[2] + nums[i] > target:
                break

        n = len(nums[:i+1])
        ret = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for h in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[h] == target:
                            sol = [nums[i], nums[j], nums[k], nums[h]]
                            sol.sort()
                            ret.add(tuple(sol))
        return list(ret)
