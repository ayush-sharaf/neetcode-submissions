class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_parts = []
        for s in strs:
            encoded_parts.append(f"{len(s)}#{s}")

        return "".join(encoded_parts)


    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        right = 1
        while right < len(s):
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            result.append(s[left:right])
            left = right
            right = left + 1

        return result