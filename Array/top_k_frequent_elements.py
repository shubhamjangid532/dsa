import heapq
from collections import Counter
from ..measure_times import measure_time

# Add this to your daily_dsa.py
@measure_time
def topKFrequent(nums, k):
    # Step 1: Count Frequencies O(N)
    # Example: nums=[1,1,1, 2,2, 3] -> count={1:3, 2:2, 3:1}
    count = Counter(nums) 
    
    # Step 2: Use a Min-Heap to keep the top k elements
    # The heap stores tuples: (frequency, number)
    # Python compares the first item in the tuple (frequency) for sorting
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        
        # If the heap grows bigger than k, remove the smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)
            
    # Step 3: The heap now contains the top k. Extract just the numbers.
    return [num for freq, num in heap]

# Test it
if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))