class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        else:
            countHash = {}
            count = 0
            res = []
            for char in p:
                if char in countHash:
                    countHash[char] += 1
                else:
                    countHash[char] = 1
                    count += 1


            check = 0
            checkHash = {}
            l, r = 0, len(p) - 1
            for i in range(len(p)):
                curr = s[i]
                if curr in checkHash:
                    checkHash[curr] += 1
                else:
                    checkHash[curr] = 1
                if curr in countHash:
                    if checkHash[curr] == countHash[curr]:
                        check += 1
                # Otherwise do nothing
            if check == count:
                    res.append(l)

            while r + 1< len(s):
                charToRemove = s[l]
                checkHash[charToRemove] -= 1
                if charToRemove in countHash:
                    if checkHash[charToRemove] + 1 == countHash[charToRemove] and checkHash[charToRemove] != countHash[charToRemove]:
                        check -= 1
                l += 1
                r += 1
                curr = s[r]
                
                if curr in checkHash:
                    checkHash[curr] += 1
                else:
                    checkHash[curr] = 1
                if curr in countHash:
                    if checkHash[curr] == countHash[curr]:
                        check += 1
                if check == count:
                    res.append(l)

            return res



# Given 2 strings s and p
# reutnr an array of all the start indices of p's anagrams in s


