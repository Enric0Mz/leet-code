class Solution:
    def __init__(self):
        ...

    def invert_string(string: str):
        right = len(string) - 1
        result = ""
        while right != -1:
            result += string[right]
            right -= 1
        return result
    
    def invert_string_refactored(string: str):
        result = ""
        result += string[::-1]
        return result



result = Solution.invert_string("PARALELEPIPEDO")
print(result)

result2 = Solution.invert_string_refactored("PARALELEPIPEDO")
print(result2)
