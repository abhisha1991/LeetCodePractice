# https://leetcode.com/problems/encode-and-decode-tinyurl/ 
import uuid
from collections import defaultdict

class Codec:
    def __init__(self):
        self.dic = dict()
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        x = uuid.uuid4().hex
        self.dic[x] = longUrl
        return x

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))