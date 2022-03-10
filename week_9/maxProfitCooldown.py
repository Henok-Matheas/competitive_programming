class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        visited = defaultdict(int)

        def recur(index):
            if index >= len(prices):
                return 0
            print(
                "############################################################")
            print("buy", index)
            if index in visited:
                return visited[index]
            buy = index
            maxim = 0
            for idx in range(index + 1, len(prices)):
                sell = idx
                curr = prices[sell] - prices[buy]

                tempmax = 0
                nxt = sell + 2
                while nxt < len(prices):
                    print("after", nxt)
                    if nxt in visited:
                        tempmax = max(tempmax, visited[nxt])
                    else:
                        visited[nxt] = recur(nxt)
                        tempmax = max(visited[nxt], tempmax)
                    nxt += 1
                maxim = max(maxim, curr + tempmax)
            visited[buy] = maxim
            return visited[buy]

        totalmaxim = 0
        for idx in range(len(prices)):
            if idx in visited:
                totalmaxim = max(totalmaxim, visited[idx])
            else:
                visited[idx] = recur(idx)
                totalmaxim = max(totalmaxim, visited[idx])
        print("this is the dictionary", visited)
        return totalmaxim


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        visited = defaultdict(int)

        def recur(index):
            if index >= len(prices):
                return 0
            if index in visited:
                return visited[index]
            buy = index
            maxim = 0
            for idx in range(index + 1, len(prices)):
                curr = prices[idx] - prices[buy]
                tempmax = 0
                nxt = idx + 2
                while nxt < len(prices):
                    if nxt not in visited:
                        visited[nxt] = recur(nxt)
                    tempmax = max(visited[nxt], tempmax)
                    nxt += 1
                maxim = max(maxim, curr + tempmax)
            visited[buy] = maxim
            return visited[buy]

        totalmaxim = 0
        for idx in range(len(prices)):
            if idx not in visited:
                visited[idx] = recur(idx)
            totalmaxim = max(totalmaxim, visited[idx])
        print("this is the dictionary", visited)
        return totalmaxim
