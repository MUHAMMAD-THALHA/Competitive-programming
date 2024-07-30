# RANGE SUM QUERY.
class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  
print(numArray.sumRange(2, 5))  
print(numArray.sumRange(0, 5))  
