class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        res = 1
        mp = {}
        l, r = 0, 1
        numFruits = 1
        mp[fruits[l]] = 1

        while r < len(fruits):
            # If valid window
            if mp.get(fruits[r], 0) != 0 or numFruits < 2:
                res = max(res, r - l + 1)
            else:
                while True:
                    mp[fruits[l]] -= 1
                    if mp[fruits[l]] == 0:
                        l += 1
                        break
                    l += 1
            if fruits[r] in mp:
                mp[fruits[r]] += 1
            else:
                mp[fruits[r]] = 1
                numFruits += 1
            r += 1
        return res

# Visiting a farm
# Single row of fruit trees

# fruits = []
# fruits[i] == type of fruit ith tree produces


# Goal: collect as much fruits as possibe, return max number of fruits you can pick
    # 2 baskets
    # each basket only holds one type of fruit
    # 