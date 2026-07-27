# Last updated: 7/27/2026, 3:48:07 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        result=[]
        for num in nums:
            res[num]+=1
        min_heap=[]
        heapq.heapify(min_heap)
        for num,freq in res.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        for [freq,num] in min_heap:
            result.append(num)
        return result