# https://leetcode.com/problems/reconstruct-itinerary
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for i,j in tickets:
            graph[i].append(j)
        
        # here nodes can be revisited
        # but edges cannot, ie, you can't use the same ticket twice from the same from --> to
        # generally in dfs its the node that we check for for visited condition
        
        # we need to sort the value list stored against a given node
        # say graph[JFK] = [SFO, ATL] --> we need graph[JFK] = [ATL, SFO]  
        # why? because we need to return the answer in lexographical sorted format
        # so if we sort, we will dfs into say ATL, instead of SFO first
        for g in graph:
            graph[g] = sorted(graph[g])
        
        # this is the condition for a valid answer
        # when we have exhausted all possible edges
        # the +1 at the end indicates that we have visited JFK already
        def allTicketsExhausted(result):
            return len(result) == len(tickets) + 1
        
        # JFK is starting point so its always first in res
        res = ["JFK"]
        def dfs(source):
            if allTicketsExhausted(res):
                return True
            
            # we have a dead end node
            # like JFK --> ATL, but no flight from ATL to JFK
            '''
            this case is important
             ______
            |      |
            A ---- C
             \
              \
               B
            
            say you start at 'A'
            you may have 'B' coming before 'C' (lexographically) 
            but the problem is once you travel to 'B' its a dead end
            you cannot travel back to 'A' to go to C
            
            thus, the correct order will be A -> C -> A -> B 
            
            this condition checks that 'B' doesn't exist in graph since it doesn't have an adjacency list
            '''
            if source not in graph:
                return False
            
            # we are using the fact that we pop from graph[source] as a criteria for "visited"
            # so we enumerate over a copy of graph[source] since we cannot enumerate over 
            # graph[source] and pop from it at the same time
            tmp = list(graph[source])
            
            for i, dest in enumerate(tmp):
                # visit the ith destination, thereby popping it from graph[source] 
                graph[source].pop(i)
                # add dest to result
                res.append(dest)
                
                if dfs(dest):
                    return True
                
                # at this point dfs(dest) was false, ie, it hit the above condition for dead end node
                # so backtrack!
                res.pop()
                # insert back the dest node at pos 'i' indicating it has not been visited yet
                graph[source].insert(i, dest)
        
        dfs("JFK")
        return res