class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums) + 1)]

        freq_map = Counter(nums)

        for key,value in freq_map.items(): freq_list[value].append(key)

        result = []

        for i in range(len(freq_list) - 1, -1, -1):

            for j in freq_list[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result
            


