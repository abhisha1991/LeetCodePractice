from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r2i = defaultdict(list)
        # graph has keys of ingredient and value is a list of recipes for which this ingredient is needed
        # example yeast --> [bread] or flour --> [bread, pizza]
        # note that since a recipe like bread can be an ingredient in another recipe, we can have graph contain a 'recipe' as well
        # example, bread --> [sandwich]
        graph = defaultdict(list)
        
        # indgree is going to count the indegree of all recipies
        indegree = defaultdict(int)
        
        for x in range(len(recipes)):
            recipie = recipes[x]
            ingredientList = ingredients[x] 
            r2i[recipie] = ingredientList
            for i in ingredientList:
                if i not in graph:
                    graph[i] = []

            if recipie not in indegree:
                indegree[recipie] = 0
                
            for i in ingredientList:
                graph[i].append(recipie)
                indegree[recipie] +=1
        
        q = list(supplies)
        res = set()
        visited = set()
        
        while q:
            x = q.pop(0)
            
            if x in visited:
                continue
                
            visited.add(x)
            
            # get all recipies that can be made partially/fully with this ingredient
            # and reduce their indegree by 1 
            # bread can be made with yeast and flour - so if 'x' is yeast, and originally indegree[bread] = 2, then now indegree[bread] = 1
            # ie, only flour needs to be explored to make indegree[bread] = 0, when this happens, bread can be prepared
            for r in graph[x]:
                if indegree[r] > 0:
                    indegree[r] -= 1
                    # if recipie indegree is 0, it can be prepared
                    if indegree[r] == 0:
                        res.add(r)
                        # if this recipie, which can now be prepared, is also an ingredient 
                        # for some other recipie, then add this to the q
                        if r in graph and r not in visited:
                            q.append(r)
        
        return list(res)