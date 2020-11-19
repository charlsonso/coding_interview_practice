#O(n^2) Brute force
def twoSum(self, nums: List[int], target: int) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
               return [i, j]

#two-pass hash table? necessary for python? create complement list

def twoSum(self, nums: List[int], target: int) -> List[int]:
    complement_dict = {}
    for idx, val in enumerate(nums):
        complement_dict[val] = idx

    for idx, val in enumerate(nums):
        complement_val = target - val
        if complement_val in complement_dict.keys() and complement_dict[complement_val] != idx:
            return [idx, complement_dict[complement_val]]

#one pass hash table
def twoSum(self, nums: List[int], target: int) -> List[int]:
    complement_dict = {}
    for idx, val in enumerate(nums):
         complement_val = target - val
         # key change
         if val in complement_dict.keys() and complement_dict[complement_val] != idx:
             return [idx, complement_dict[val]]
         else:
            complement_dict[complement_val] = idx
