class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sortedl =[]
        i = j = 0
        lel = len(left)
        ler = len(right)

        while i < lel and j < ler:
            if left[i] < right[j]:
                sortedl.append(left[i])
                i+=1
            else:
                sortedl.append(right[j])
                j+=1
        sortedl.extend(left[i:])
        sortedl.extend(right[j:])
        return sortedl

