class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numbers, longest = set(nums), 0
        for num in numbers:
            if num - 1 not in numbers:
                starting, count = num, 0
                while starting in numbers and num - 1 not in numbers:
                    count += 1
                    starting += 1
                longest = max(longest, count)
        return longest
