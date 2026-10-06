class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        
        freq_arr = [[] for _ in range(len(nums)+1)]

        for key,value in map.items():
            freq_arr[value].append(key)

        result_arr = []
        
        for i in range(len(freq_arr)-1,-1,-1):
            for j in freq_arr[i]:
                result_arr.append(j)

                if len(result_arr) == k:
                    return result_arr

        return result_arr
            


