class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        bracket_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        bracket_stack = []

        for i in s:
            if i in bracket_map:
                if not bracket_stack or bracket_stack[-1] != bracket_map[i]:
                    return False
                
                bracket_stack.pop()

            else: 
                bracket_stack.append(i)

        return not bracket_stack

            