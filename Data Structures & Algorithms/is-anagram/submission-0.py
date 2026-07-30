class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for i in s:
            if i in char_count:
                char_count[i] +=1
            else:
                char_count[i] = 1
        for i in t:
            if i not in char_count:
                return False
            else:
                char_count[i] -= 1
        
        all_values = char_count.values()
        for i in all_values:
            if i !=0:
                return False

        return True
                