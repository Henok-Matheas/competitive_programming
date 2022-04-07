class Solution:

    def findTheWinner(self, n: int, k: int) -> int:

        friends = [i + 1 for i in range(n)]
        i = 0
        while len(friends) > 1:
            i = (i + k - 1) % len(friends)
            friends.remove(friends[i])
            i %= len(friends)
        return friends[0]