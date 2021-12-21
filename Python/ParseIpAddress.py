import re
class Solution(object):
    def __init__(self, text):
        self.text = text

    def parseIp(self):
        if '-' in self.text:
            # non cidr notation
            text = self.text.split(',')
            # now you have a range like 10.0.0.0 - 11.0.0.0
            for i in text:
                # split the range into 2 parts
                text2 = i.split('-')
                for j in text2:
                    # get rid off white spaces
                    ip = j.strip()
                    ipv4 = re.findall(r'([0-9]{1,3}\.){3}[0-9]{1,3}', ip)
                    print(ipv4)
        else:
            # cidr notation
            # something like 10.0.0.0/24
            text = self.text.split(',')
            for i in text:
                text2 = text.split('/')
                ipv4 = re.findall(r'([0-9]{1,3}\.){3}[0-9]{1,3}', text2[0].strip())
                cidr = re.findall(r'\d{1,2}', text2[1].strip())


s = Solution('10.0.0.0-  10.1.0.0')
s.parseIp()
# match a website url: ^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*((com)|(org))$
# general website url: https://www.regextester.com/23
# match http or www url: (?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])
# match ipv6: https://www.regextester.com/25

