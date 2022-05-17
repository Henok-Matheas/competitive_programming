class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        odds = []

        for index, num in enumerate(nums):
            if num % 2 == 1:
                odds.append(index)

        i = 0
        j = k - 1
        # print("odds si",odds)
        prev = -1
        nice = 0
        while j < len(odds):
            # print(f"i is {i} and j is {j}")
            pre = odds[i] - prev - 1
            after = (odds[j +
                          1] if j + 1 < len(odds) else len(nums)) - odds[j] - 1
            # print(f"pre is {pre} and after is {after}")
            nice += pre + after + 1 + (pre * after)
            prev = odds[i]
            i += 1
            j += 1
        return nice
