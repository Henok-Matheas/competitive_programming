class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [num for num in nums if num % 2][::-1]
        even = [num for num in nums if num % 2 == 0][::-1]
        
        print(odd, even)
        for idx in range(len(nums)):
            if idx % 2:
                ## odd
                nums[idx] = odd.pop()
            else:
                nums[idx] = even.pop()
                
        return nums