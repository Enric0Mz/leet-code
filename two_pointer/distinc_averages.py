class Solution(object):
    def distinctAverages(self, nums):
        unique_avg = set()
        while len(nums) > 1:
            left = min(nums)
            right = max(nums)
            nums.remove(left)
            nums.remove(right)
            avg = (left + right) / 2.0
            
            unique_avg.add(avg)
        
        return len(unique_avg)


print(Solution().distinctAverages(nums=[9,5,7,8,7,9,8,2,0,7]))

