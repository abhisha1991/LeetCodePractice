# https://leetcode.com/problems/web-crawler-multithreaded/
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # list of urls we have parsed
        seen = set()
        # returns yahoo.com from https://yahoo.com/news
        def getHostName(url):
            url = url.replace("http://", "")
            url = url.replace("https://", "")
            return url.split('/')[0]
        
        # q is a list of future objects
        # each future object result() returns a list of links
        q = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            seen.add(startUrl)
            q.append(executor.submit(htmlParser.getUrls, startUrl))
            while q:
                # notice when we pick out a futures object from the queue
                # and call result(), we get back a list of urls
                urls = q.pop(0).result()
                for url in urls:
                    if url not in seen and getHostName(startUrl) == getHostName(url):
                        seen.add(url)
                        linksFutures = executor.submit(htmlParser.getUrls, url)
                        q.append(linksFutures)
        
        return list(seen)