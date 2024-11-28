class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_arr = []
        for i in range(len(gas)):
            net_arr.append(gas[i]-cost[i])

        if sum(net_arr) < 0:
            return -1
        if len(net_arr) == 1:
            return 0

        total = 0
        i = 0
        validating = None
        length = len(gas)

        # If the validating station can reach itself then we've found it
        while validating != i % length:
            if net_arr[i % length] > 0: # Check for net gain
                if validating == None:
                    validating = i % length

            total += net_arr[i % length]
            if total < 0:
                validating = None
                total = 0

            i += 1

        return validating
