# COUNT NUMBER OF TEAMS.

class Solution:
    def numTeams(self, rating):
        n = len(rating)
        count = 0

        for j in range(n):
            left_less = left_greater = right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            count += left_less * right_greater + left_greater * right_less

        return count


rating = [2, 5, 3, 4, 1]
solution = Solution()
print(solution.numTeams(rating))  

