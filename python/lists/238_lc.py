#redo

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create left, right and solution array
        left = [1] * len(nums)
        right = [1] * len(nums)
        solution = [0] * len(nums)
        #for each element, compute array at left
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] * nums[i + 1]
        
        for i in reversed(range(len(nums))):
            solution[i] = left[i] * right[i]
        
        return solution
