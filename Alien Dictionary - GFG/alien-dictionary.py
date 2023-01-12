# User function Template for python3
from collections import deque
from heapq import heappop, heappush
class Solution:
    def findOrder(self, dict, N, K):
        arr = dict
        ascii_lowercase = set()

        for word in dict:
            ascii_lowercase.update(word)

        graph = {x: [] for x in ascii_lowercase}
        in_degree = {x: 0 for x in ascii_lowercase}

        for i in range(n - 1):
            s1, s2 = arr[i], arr[i + 1]

            for j in range(len(s1)):
                if j >= len(s2):
                    return []

                if s1[j] != s2[j]:
                    graph[s1[j]].append(s2[j])
                    in_degree[s2[j]] += 1
                    break

        starting_nodes = list(filter(lambda x: in_degree[x] == 0, ascii_lowercase))

        que = starting_nodes
        order = []

        while que:
            letter = heappop(que)
            order.append(letter)

            for nei in graph[letter]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    heappush(que, nei)

        return order



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends