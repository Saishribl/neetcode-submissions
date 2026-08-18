class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boat = 0
        low = 0
        high = n - 1

        while low <= high:
            s = people[low] + people[high]
            if s > limit:
                high-=1
                boat+=1
            elif s <= limit:
                low+=1
                high-=1
                boat+=1

        
        return boat