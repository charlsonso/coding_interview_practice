def containsDuplicate(self, nums: List[int]) -> bool:
    #by sorting, O(nlog(n)), space complexity O(1)
    sorted_nums = nums.sort()
    for idx, val in enumerate(nums):
        if idx == len(nums) - 1:
            continue
        if val == nums[idx+1]:
            return True
    return False

    #time complex O(n), space complexity O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        #by using a set
        for idx, val in enumerate(nums):
            if val in nums_set:
                return True
            else:
                nums_set.add(val)
        return False
