class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            sorted_string = str(sorted(strs[i]))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(i)
            else:
                hashmap[sorted_string] = [i]
        result = []
        for value in hashmap.values():
            inter = []
            for j in value:
                inter.append(strs[j])
            result.append(inter)
        return result



