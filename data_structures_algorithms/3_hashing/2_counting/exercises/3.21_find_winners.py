class Solution:
    def find_winners(self, matches: [[int]]) -> [[int]]:
        # using a hashmap (set or dict)
        # forget about using a hashmap w/in the context of a sliding window. complete the problem.
        # use a hashmap within the context of sliding window
        return 0





class Solution: 
    def find_winners(self, matches: [[int]]) -> [[int]]:

        losses_count = {}
        
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]



matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution().find_winners(matches))

matches = [[2,3],[1,3],[5,4],[6,4]]
# print(Solution().find_winners(matches))