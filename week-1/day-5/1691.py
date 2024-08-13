#Maximum Heights by Stacking Cuboids.

class Solution:
    def maxHeight(self, cuboids):

        for cuboid in cuboids:
            cuboid.sort()
        
        cuboids.sort()
        
        n = len(cuboids)
        dp = [0] * n
        
        for i in range(n):
            dp[i] = cuboids[i][2]
        
        for i in range(n):
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and 
                    cuboids[j][1] <= cuboids[i][1] and 
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        
        return max(dp)

cuboids = [[50,45,20],[95,37,53],[45,23,12]]
solution = Solution()
print(solution.maxHeight(cuboids))  
