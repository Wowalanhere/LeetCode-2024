class Solution:
    def reverseVowels(self, s: str) -> str:

        stack = []
        result = []

        for c in s:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                stack.append(c)
        
        for c in s:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                result.append(stack.pop())
            else:
                result.append(c)
        
        return "".join(result)

        # r = ''
        # backpointer = len(s)
        # for i in range(len(s)):
        #     if self.ifVowel(s[i]):
        #         backpointer -= 1
        #         while not self.ifVowel(s[backpointer]):
        #             backpointer -= 1
        #         r += s[backpointer]
        #     else:
        #         r += s[i]

        # return r 
    
        #python tricks:
        # two pointer or stack
        # backpointer of python logic above

    def ifVowel(self, s: str) -> bool:
        if s.lower() in ('a', 'e', 'i', 'o', 'u'):
            return True

        return False 
        