#https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10
#3147. Taking Maximum Energy From the Mystic Dungeon

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxVal = -float('inf')
        n = len(energy)
        for i in range(k):
            acc = 0
            j = i
            for j in range(n-1-i, -1, -k):
                acc += energy[j]
                maxVal = max(maxVal, acc)
        
        return maxVal