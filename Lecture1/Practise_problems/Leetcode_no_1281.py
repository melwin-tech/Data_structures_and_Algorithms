'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''

#  Solution

class Solution(object):
    def subtractProductAndSum(self, n):
        temp = n
        sum = 0
        product = 1
        while temp > 0:
            r = temp % 10       
            sum += r
            product *= r
            temp //= 10         
        return product - sum
