'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''

# Solutions

class Solution(object):
    def countOdds(self, low, high):
        return ((high+1)//2)-(low//2)