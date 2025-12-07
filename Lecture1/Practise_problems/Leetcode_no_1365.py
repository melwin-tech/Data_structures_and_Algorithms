'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

# Solutions

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            answer.append(count)
        return answer