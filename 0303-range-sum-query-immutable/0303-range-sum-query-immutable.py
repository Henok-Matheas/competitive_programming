class NumArray:

    def __init__(self, nums: List[int]):
        self.p_sum = [0]
        for idx, num in enumerate(nums):
            self.p_sum.append(num + self.p_sum[idx])

    def sumRange(self, left: int, right: int) -> int:
        return self.p_sum[right + 1] - self.p_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)