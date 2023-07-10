class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_d={} """its will store the number and index"""
        for i,num in enumerate(nums): """for taking index and number both"""
            compl=target-num 
            if compl in num_d: 
                return(num_d[compl],i)
            num_d[num]=i
        return []
