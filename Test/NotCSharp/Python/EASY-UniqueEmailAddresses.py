#https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        i = 0
        j = len(emails)-1
        em=[]
        for email in emails:
            loc = email.split('@')[0]
            loc=loc.replace('.','')
            if '+' in loc:
                loc = loc[:loc.index('+')]
            em.append(loc+'@'+email.split('@')[1])
        return(len(set(em)))
