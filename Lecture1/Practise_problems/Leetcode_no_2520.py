'''
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
'''

#  Solution

class Solution(object):
    def countDigits(self, num):
        temp = num
        count = 0
        while temp > 0:
            r = temp % 10
            if r != 0 and num % r == 0:
                count += 1
            temp //= 10
        return count
