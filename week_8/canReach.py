class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:

        bound = lambda row: row >= 0 and row < len(arr)

        visited = set()

        now = collections.deque([])
        neibrs = collections.deque([])

        now.append(start)
        visited.add(start)

        while now or neibrs:
            while now:
                curr = now.popleft()
                # print(curr,"this is the current")

                if arr[curr] == 0:
                    return True

                left = curr - arr[curr]
                right = curr + arr[curr]

                if bound(left) and left not in visited:
                    neibrs.append(left)
                if bound(right) and right not in visited:
                    neibrs.append(right)

            while neibrs:
                neibr = neibrs.popleft()

                now.append(neibr)
                visited.add(neibr)
        return False