# https://leetcode.com/problems/reformat-date/
class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, 
                 "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        
        date = date.split(" ")
        d = date[0]
        m = date[1]
        y = date[2]
        
        m = month[m]
        if m < 10:
            m = "0" + str(m)
        else:
            m = str(m)
        
        def handleDay(suffix, d):
            if suffix not in ["st", "nd", "rd", "th"]:
                raise ValueError()
            
            if len(d) == 3:
                d = "0" + d[0]
            elif len(d) == 4:
                d = d[:2]
            else:
                raise ValueError()
            
            return d
        
        d = handleDay(d[-2:], d)
        
        return y + "-" + m + "-" + d