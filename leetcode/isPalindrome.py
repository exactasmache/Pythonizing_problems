import time
import random
'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x % 10 == 0 and x != 0 or x < 0:
            return False

        rev_x = 0
        while x > rev_x:
            rev_x = rev_x * 10 + x % 10
            x = x//10

        return x == rev_x or x == rev_x//10

    def isPalindrome2(self, x: int) -> bool:
        equis = str(x)
        return equis == equis[::-1]


if __name__ == '__main__':
    solver = Solution()

    result = 0
    total = 1000000
    fst_total = 0
    snd_total = 0
    for i in range(total):
        num = random.randint(0, 1000*200)
        if random.random() > .7:
            num *= -1

        start = time.time()
        sol = solver.isPalindrome(num)
        end = time.time()
        fst_time = end - start

        start = time.time()
        sol2 = solver.isPalindrome2(num)
        end = time.time()
        snd_time = end - start

        if sol != sol2:
            print(f'ERROR: different results:\n num = {num}, {sol}, {sol2}')
            exit(1)

        fst_total += fst_time
        snd_total += snd_time

    print(f'Speedup: {snd_total/fst_total}')
