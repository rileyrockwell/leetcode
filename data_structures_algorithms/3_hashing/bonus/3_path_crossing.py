# collaborator: A. Hussey

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # start at the origin, for each "movement" in a direction, 
        # record coordinates, then determine if for any given movement,
        # coordinates are duplicates or not

        visited_locations_set = set()

        x = y = 0

        for direction in path:
            visited_locations_set.add((x, y))            

            if direction == "N":
                y += 1
            elif direction == "E":
                x += 1
            elif direction == "S":
                y -= 1
            elif direction == "W":
                x -= 1

            # if you have visited the coordinate beforehand
            if (x, y) in visited_locations_set:
                return True

        # every individual coordinate was unique
        return False


path = "NES"
print(Solution().isPathCrossing(path))

print("###")
path = "NESWW"
print(Solution().isPathCrossing(path))
