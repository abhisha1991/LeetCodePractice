# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = dict()
        
        for cpd in cpdomains:
            arr = cpd.split(' ') # 9001 discuss.leetcode.com
            num = int(arr[0]) # 9001
            domains = arr[1].split('.') # discuss.leetcode.com ==> [discuss, leetcode, com]
            sub = ''
            for i in range(len(domains)-1, -1, -1):
                sub = '.' + domains[i] + sub
                # key sub[1:] because we want to avoid having the prefix '.' in the key
                # for example, we dont want .leetcode.com, we just want leetcode.com
                key = sub[1:]
                
                if key not in dic:
                    dic[key] = num
                else:
                    dic[key] += num
        
        # we want to return the data in the format ["num url_domain", "num url_domain"]
        return [str(v) + " " + str(k) for k,v in dic.items()]