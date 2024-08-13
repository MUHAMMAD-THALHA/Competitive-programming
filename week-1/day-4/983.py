#MINIMUM COST OF TICKETS.

class Solution:
    def mincostTickets(self, days, costs):
        max_day = days[-1]
        day_set = set(days)
        dp = [0] + [float('inf')] * max_day

        for i in range(1, max_day + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i], dp[i - 1] + costs[0])
                dp[i] = min(dp[i], dp[max(0, i - 7)] + costs[1])
                dp[i] = min(dp[i], dp[max(0, i - 30)] + costs[2])

        return dp[max_day]

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
solution = Solution()
print(solution.mincostTickets(days, costs)) 