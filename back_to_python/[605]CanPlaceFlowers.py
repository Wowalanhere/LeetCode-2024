class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:


        
        # empty_plots = 0

        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 0:
        #         empty_plots+=1
        # else:
        #     for i in range(0, len(flowerbed)):
        #         if flowerbed[i] != 1:
        #             if i == 0:
        #                 if flowerbed[1] == 0:
        #                     empty_plots+=1
        #                     flowerbed[i] = 1
        #             elif i == len(flowerbed)-1:
        #                 if flowerbed[-2] == 0:
        #                     empty_plots+=1
        #                     flowerbed[i] = 1
        #             else:
        #                 if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
        #                     empty_plots+=1
        #                     flowerbed[i] = 1
            
        # return empty_plots >= n

        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                
            return False

    





# f = [1, 0, 0, 0, 0, 1]
# n = 2

# s = Solution()
# print(s.canPlaceFlowers(f, n))

