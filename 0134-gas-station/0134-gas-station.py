class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starting = 0
        total_gas = 0


        for current in range(len(gas)):
            total_gas += gas[current] - cost[current]
            if total_gas < 0:
                total_gas = 0
                starting = current + 1

        return starting if sum(gas) >= sum(cost) else -1
