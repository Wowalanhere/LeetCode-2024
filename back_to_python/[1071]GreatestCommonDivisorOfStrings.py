str1 = "AAABBB"
str2 = "AAABBBAAABBB"

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # trick here 
        # if a+b == b+a, strings have gcd
        # or no gcd
        # and the gcd of len of a and b -> the substring len

        if str1 + str2 == str2 + str1:
            return str1[:self.gcd(len(str1), len(str2))]
        
        return ""
    
    # the gcd funtion implementation 
    def gcd(self, len_str1: int, len_str2: int) -> int:
        return len_str1 if len_str2 == 0 else self.gcd(len_str2, len_str1%len_str2)
    

s = Solution()
print(s.gcdOfStrings(str1, str2))