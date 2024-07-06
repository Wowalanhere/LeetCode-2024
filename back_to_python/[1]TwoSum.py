from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], index]
            else:
                numMap[num] = index
        
        return []

# leetcode submit region end(Prohibit modification and deletion)

nums = [2, 4, 4] 
target = 8

question = Solution()
answer = question.twoSum(nums, target)
print(answer)