import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        lst = []
        for key in dict:
            lst.append([dict[key], key])

        heapq.heapify(lst)

        ordered = heapq.nlargest(k, lst)

        final = []

        for i in ordered:
            final.append(i[1])
        return final

        #         counted = [[0,0]]*100000
        #         for i in nums:
        #             counted[i] = [i, counted[i][1] + 1]

        #         counted.sort(key = lambda x : x[1], reverse = True)

        #         final = []
        #         for i in range(k):
        #             final.append(counted[i][0])
        #         return final
        import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        lst = []
        for key in dict:
            lst.append([dict[key], key])

        heapq.heapify(lst)

        ordered = heapq.nlargest(k, lst)

        final = []

        for i in ordered:
            final.append(i[1])
        return final


#         counted = [[0,0]]*100000
#         for i in nums:
#             counted[i] = [i, counted[i][1] + 1]

#         counted.sort(key = lambda x : x[1], reverse = True)

#         final = []
#         for i in range(k):
#             final.append(counted[i][0])
#         return final
