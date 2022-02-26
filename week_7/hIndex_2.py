class Solution:

    def hIndex(self, citations: List[int]) -> int:
        last = len(citations)

        left = 0
        right = len(citations) - 1
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if last - mid > citations[mid]:
                left = mid + 1
            else:
                best = last - mid
                right = mid - 1
        return best

        # for idx in range(len(citations)):
        #     if last - idx <= citations[idx]:
        #         return last - idx
        #     else:
        #         print("h", last - idx, "value", citations[idx] )
        # return ans
