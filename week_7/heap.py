class Solution:

    def heapify(self, arr, n, i):
        idx = i
        while self.parent(i) > -1 and arr[self.parent(i)] > arr[i]:
            arr[self.parent(i)], arr[i] = arr[i], arr[self.parent(i)]
            i = self.parent(i)

        while (self.leftChild(idx) < n and arr[self.leftChild(idx)] < arr[idx]
               ) or (self.rightChild(idx) < n
                     and arr[self.rightChild(idx)] < arr[idx]):
            minChildIndex = self.leftChild(idx)
            if self.rightChild(idx) < n and arr[self.rightChild(
                    idx)] < arr[minChildIndex]:
                minChildIndex = self.rightChild(idx)
            arr[idx], arr[minChildIndex] = arr[minChildIndex], arr[idx]
            idx = minChildIndex

        #Function to build a Heap from array.
    def buildHeap(self, arr, n):
        i = n - 1
        while i >= 0:
            self.heapify(arr, len(arr), i)
            i -= 1

        #Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, len(arr))
        i = 0
        j = len(arr) - 1
        while n > 0:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            n -= 1
            self.heapify(arr, n, 0)

        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def insert(self, arr, element):
        index = len(arr)
        arr.append(element)
        self.heapify(arr, len(arr), index)

    def remove(self, arr, index):
        self.update(arr, index, arr.pop())

    def update(self, arr, index, value):
        arr[index] = value
        self.heapify(arr, len(arr), index)

    def getMin(self, arr):
        return arr[0]

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def parent(self, index):
        if index - 1 > 0:
            return 0
        return index - 1 // 2


sol = Solution()
arr = [2, 6, 8, 10, 2, 34, 2, 3, 4, 3, 1, 8, 9, 5, 3, 7, 2, 6, 2, 5, 2]
sol.HeapSort(arr, len(arr))
print(arr)
