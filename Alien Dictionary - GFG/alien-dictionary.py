#User function Template for python3
from collections import defaultdict, deque
import heapq
class Solution:
    def findOrder(self,dict, N, K):
    # code here
    
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for word in dict:
            for letter in word:
                graph[letter] = []
        
        for idx in range(0, len(dict) - 1):
            curr = dict[idx]
            next_ = dict[idx + 1]
            
            for idx in range(len(curr)):
                if len(next_) == idx:
                    return []
                if next_[idx] != curr[idx]:
                    graph[curr[idx]].append(next_[idx])
                    indegree[next_[idx]] += 1
                    break
                
        queue = deque([])
        answer= []
        
        for node in graph:
            if not indegree[node]:
                
                # heapq.heappush(heap, node)
                queue.append(node)
        
        while queue:
            # node = heapq.heappop(heap)
            node = queue.popleft()
            answer.append(node)
            
            for neigh in graph[node]:
                indegree[neigh] -= 1
                
                if not indegree[neigh]:
                    # heapq.heappush(heap, neigh)
                    queue.append(neigh)
                
        return "".join(answer)



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