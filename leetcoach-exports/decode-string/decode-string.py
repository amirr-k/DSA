class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        st = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                appendString = ""
                currString = st[-1]
                while (currString.isnumeric()) == False:
                    appendString = st.pop() + appendString
                    currString = st[-1]
                numToMultiply = st.pop()
                appendString = appendString * (int(numToMultiply))
                st.append(appendString)
                i += 1
            else:
                num = ""
                while s[i].isnumeric() == True:
                    num += s[i]
                    i += 1
                if num != "":
                    st.append(num)
                    i += 1
                num = ""
                while i < len(s) and (s[i].isalpha()) == True:
                    num += s[i]
                    i += 1
                st.append(num)
                if st == '[':
                    i += 1

        return "".join(st)

#3[a]2[bc]"
# 3a
# currString = 'a'
# 
# Given encoded string, return the decoded string
    # Given a number
    # ex. 3
    # always followed by bracket
    # so like 3[a]
    # This means push both
    # now, When bracket closes, that means just push that onto stack
    # i.e. 
        # 3[a]  = aaa == st = [aaa]
        # When embedded
        # 3[a2[c]]
        # Push 3
        # 3
        # push a
        # 3a
        # push 2
        # 3a2
        # push c
        # 3a2c
        # now pop off stack
        # first bracket
        # 3 a cc
        # now pop off stack
        # acc acc acc
        # so when bracket, pop until you hit a number
        # and append that to answer
