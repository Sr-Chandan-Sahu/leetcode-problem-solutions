"""
Try it here :
https://leetcode.com/problems/two-sum/
"""
def twoSum(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    num_dict = {}  # Dictionary to store values and indices   
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]           
        num_dict[num] = i
        
    return []




"""
Try it here :
https://leetcode.com/problems/two-sum/
"""