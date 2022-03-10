import heapq

tests = int(input())

answers = []
for test in range(tests):
    vals = input().split()
    n = int(vals[0])
    k = int(vals[1])

    needed = input().split()
    permanent = input().split()
    heap = []
    discarded = []

    for i in range(n):
        heapq.heappush(heap, [-1 * int(permanent[i]), -1 * int(needed[i])])

    while heap or (discarded and discarded[-1][0] <= k):
        while discarded and discarded[0][0] <= k:
            k += heapq.heappop(discarded)[1]
        # maxheap of [permannent addable, temp needed]

        if heap:
            curr = heapq.heappop(heap)
            if -1 * curr[1] <= k:
                k += (-1 * curr[0])
            else:
                heapq.heappush(discarded, [-1 * curr[1], -1 * curr[0]])
    while discarded and discarded[0][0] <= k:
        k += heapq.heappop(discarded)[1]

    answers.append(k)

for answer in answers:
    print(answer)