class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        buckets = one poisonous
        you have some time

        feeding
            1. choose some
            2. for each pig choose buckets feed at same time
            3. wait for minutesToDie, poisoned ones die
            4. do this until minutestToTest or you find the bucket

        minimize number of pigs

        the maximum number of pigs you need is <= len(buckets)

        we can then do binary search on the amount of pigs to find if it's possible or not

        
        simpler question
        n buckets
        minimum number of pigs

        """
        tries = minutesToTest / minutesToDie + 1
        pigs = 0
        while tries ** pigs < buckets:
            pigs += 1
            
        return pigs