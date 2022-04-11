# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        def timeToMins(t, roundUp):
            hoursToMins = int(t.split(":")[0]) * 60
            mins = int(t.split(":")[1])
            offset = mins % 15
            
            # return raw time without rounding if needed
            if roundUp is None:
                return hoursToMins + mins
            
            # will only work if offset is not 0
            # if time was 00:15, then offset = 0 (so we don't want to round)
            if offset is not 0:                
                if roundUp:
                    # find remaining mins to reach 15 interval whole
                    # add this to result
                    offset = 15 - offset
                else:
                    # reduce by this offset to reach a 15 interval whole
                    offset = -1 * offset
                
            return hoursToMins + mins + offset
        
        login = timeToMins(loginTime, None)
        logout = timeToMins(logoutTime, None)
        # get raw times, if we have something like 00:47 and 00:57
        # then we cannot play even a single game
        if logout > login and logout - login < 15:
            return 0
        
        # round up login time, example: 00:10 becomes 00:15
        # round down logout time, example: 00:25 becomes 00:15
        login = timeToMins(loginTime, True)
        logout = timeToMins(logoutTime, False)
        
        # say login was 10:15, logout was 08:30
        # then we want logout to be 10:15 + 12 hours + remaining time to midnight + 08:30
        if logout < login:
            logout = login + 12 * 60 + (24 * 60 - login - 12 * 60) + logout
        
        return int((logout-login)/15)