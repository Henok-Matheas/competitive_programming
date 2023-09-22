class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """
        n songs
        goal number of songs
        
        
        playlist
            - song played atleast once
            - replay if k songs have been played
            
        all the songs will be played once
        
        thought:
        
        actually generate them
        doesn't pass but you get the idea
        
        
        thought: a sort of dp()
        
        
        for a character and idx
        
        
        
        """
        
        @lru_cache(None)
        def count(curr_goal, old_songs):
            if curr_goal == 0 and old_songs == n:
                return 1
            
            if curr_goal == 0 or old_songs > n:
                return 0
            
            ## choose new song
            total = (n - old_songs) * count(curr_goal - 1, old_songs + 1)
            
            ## choose old song if the we have used k or above old songs
            if old_songs > k:
                total += (old_songs - k) * count(curr_goal - 1, old_songs)
                
                
            return total
        
        return count(goal, 0) % (10 ** 9 + 7)
            