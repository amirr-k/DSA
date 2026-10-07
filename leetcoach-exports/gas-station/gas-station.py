class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            # So we can guarantee that there is enough gas to make it across
            # The question is now; which gas station do we start at?
            viable = 0
            tank = 0
            for index, stop in enumerate(gas):
                tank += stop
                if tank < cost[index]:
                    viable = index + 1
                    tank = 0
                else:
                    tank -= cost[index]
            return viable
# Greedy
    # n gas stations
    # circular route
    # amount of gas at ith staiton is gas[i]

    # Cost to go from ith station to next is cost[i]

    # Must travel in clockwise direciton


    # Begin journey with an empty tank