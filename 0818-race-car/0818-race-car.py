class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([[0, 0, 1]])
        visited = set([(0, 1)])
        while queue:
            step, pos, speed = queue.popleft()
            if pos == target:
                return step
                
            new_speed = speed * 2
            if (pos + speed, new_speed) not in visited:
                queue.append([step + 1, pos + speed, speed * 2])
                visited.add((pos + speed, speed * 2))
                
            ne_speed = 1 if speed < 0 else -1
            if (pos, ne_speed) in visited:
                continue
            if (pos + speed < target and speed < 0) or (pos + speed > target and speed > 0):
                queue.append([step + 1, pos , ne_speed])
                visited.add((pos , ne_speed))