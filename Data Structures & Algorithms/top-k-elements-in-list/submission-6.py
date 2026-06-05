class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1
        while k > 0:
            maxKey = 0
            maxVal = 0
            for key in numFreq:
                if numFreq[key] > maxVal and key not in output:
                    maxKey = key
                    maxVal = numFreq[key]
            output.append(maxKey)
            k -= 1
        return output