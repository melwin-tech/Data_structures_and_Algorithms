'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

#  Solution

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp=x
        reverse = 0
        while temp>0:
            r = temp % 10
            reverse = (reverse*10) + r
            temp = temp // 10
        if x == reverse:
            return True
        else:
            return False

        