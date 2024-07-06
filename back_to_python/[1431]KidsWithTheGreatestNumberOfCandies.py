class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = 0
        result = []

        for candy in candies:
            max_number = max(candy, max_number)
        print(max_number)

        for candy in candies:
            if candy + extraCandies >= max_number:
                result.append(True)
            else:
                result.append(False)
        
        return result