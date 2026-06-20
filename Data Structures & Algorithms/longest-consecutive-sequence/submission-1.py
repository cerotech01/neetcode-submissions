class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = sorted(set(nums))
        largest = 1
        current = 1

        for i in range(1, len(unique_nums)):
            if unique_nums[i] == unique_nums[i-1]+1:
                current +=1
            else:
                largest = max(largest, current)
                current = 1
        
        return max(largest, current)