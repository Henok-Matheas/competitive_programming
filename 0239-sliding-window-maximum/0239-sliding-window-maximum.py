class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque([])
        left = 0
        answer = []

        for right in range(len(nums)):
            ## remove top element if out of bounds of window
            if deq and deq[0] < left:
                deq.popleft()
            ## monotonic operations
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)
            
            ## append if window is satisfied.
            if right - left + 1 == k:
                answer.append(nums[deq[0]])
                left += 1

        return answer