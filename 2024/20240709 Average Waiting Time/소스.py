class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        i = 0
        curr = 0
        count = 0
        sumWait = 0
        while i!=len(customers):
            arrival, time = customers[i]
            if arrival == curr:
                sumWait += (count + time)
                count += time
                i += 1
                continue
            curr += 1
            count = count-1 if count > 0 else count
        return sumWait / len(customers)