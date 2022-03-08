class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()

        for num in nums:
            numbers.add(num)

        count = 0
        longest = 0

        for num in numbers:
            if num - 1 not in numbers:
                starting = num

                while starting in numbers:
                    count += 1
                    longest = max(longest, count)
                    starting += 1
                count = 0
        return longest
