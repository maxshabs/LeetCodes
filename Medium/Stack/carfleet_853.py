class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_stack = []
        comb_arr = []
        for i in range(len(position)):
            comb_arr.append((position[i], speed[i]))
        comb_arr.sort(reverse=True)
        for pos, s in comb_arr:
            if not fleet_stack or fleet_stack[-1] < (target - pos) / s:
                fleet_stack.append((target - pos) / s)
        return len(fleet_stack)
