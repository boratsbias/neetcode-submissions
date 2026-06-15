class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(n)):
            output[i] *= postfix
            postfix *= nums[i]

        return output