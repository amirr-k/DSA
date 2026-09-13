class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        st = []
        i = 0
        while i < len(temperatures):
            if len(st) == 0:
                st.append((temperatures[i], i))
                i += 1
                continue
            while (len(st) > 0) and (temperatures[i] > st[-1][0]):
                top = st[-1]
                index = top[1]
                res[index] = i - index
                st.pop()
            st.append((temperatures[i], i))
            i += 1
        return res


# 


# Given array of integers temps
    # return array answer such that answer[i] == nums of days you have to wait for the ith day
    # to get a warmer temp

# if there is no future day for which this is possible, keep answer[i] == 0 instead.   
    

    # E.g.
        # temperatures = [73,74,75,71,69,72,76,73]
        #Output: [1,1,4,2,1,1,0,0]
            # out[0] = 