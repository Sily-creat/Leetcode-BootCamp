import heapq
from collections import Counter


def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element
    count = Counter(nums)

    # Step 2: Use a heap to keep track of the k most frequent elements
    # We use a min-heap, so we will store tuples of (-frequency, element) to sort by frequency in descending order
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)  # Pop the element with the smallest frequency

    # Step 3: Extract the elements from the heap
    return [num for freq, num in heap]
