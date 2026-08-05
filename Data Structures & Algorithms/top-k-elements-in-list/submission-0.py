class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucks = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucks[freq].append(num)
        
        res = []

        for i in reversed(bucks):
            for num in i:
                res.append(num)
                if len(res) == k:
                    return res
