class Solution:

    def removeDuplicateLetters(self, s: str) -> str:

        if len(s) == 1:
            return s

        dup = {}
        stack = []
        for letter in s:
            if letter in dup:
                dup[letter] += 1
            else:
                dup[letter] = 1

        final = []
        visited = set()
        for idx in range(len(s)):
            now = s[idx]
            while stack and dup[
                    stack[-1]] > 0 and stack[-1] > now and now not in visited:
                visited.remove(stack.pop())

            if stack and stack[-1] == now:
                dup[now] -= 1
                continue

            elif not stack or (now not in visited and
                               (dup[stack[-1]] == 0 or stack[-1] < now)):
                stack.append(now)
                visited.add(now)
            dup[now] -= 1
        return "".join(stack)
