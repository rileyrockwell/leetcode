class Solution:
    def find_winners(self, matches: [[int]]) -> [[int]]:
        # using a hashmap (set or dict)
        # forget about using a hashmap w/in the context of a sliding window. complete the problem.
        # use a hashmap within the context of sliding window
        pass

class Solution: 
    def find_winners(self, matches: [[int]]) -> [[int]]:

        losses_count = {}
        
        for winner, loser in matches:
            print(losses_count)
            losses_count[winner] = losses_count.get(winner, 0)
            print(losses_count)
            
            losses_count[loser] = losses_count.get(loser, 0) + 1

        return losses_count

        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)
        
        return [sorted(zero_lose), sorted(one_lose)]



# matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# print(Solution().find_winners(matches))

matches = [[2,3],[1,3],[5,4],[6,4], [2,1], [1,4]]
print(Solution().find_winners(matches))

# same concept in different situations. do not try to rewrite or memorie 1 problem.
# understand the underlying concept and paply the principles to  3-5 problems.