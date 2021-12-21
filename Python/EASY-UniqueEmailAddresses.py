#https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution:
    def numUniqueEmails(self, emails):
        setx = set()
        for e in emails:
            splits = e.split("@")
            first = splits[0]
            last = splits[1]
            first = first.split("+")[0]
            first = first.replace('.','')
            setx.add(first + "@" + last)
        return len(setx)
