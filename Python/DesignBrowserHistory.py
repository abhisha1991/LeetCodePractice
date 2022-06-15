# https://leetcode.com/problems/design-browser-history
class BrowserHistory:

    def __init__(self, homepage: str):
        # 2 stacks, one for storing browser history, one for storing forward history
        self.browser = [homepage]
        self.forwardHistory = []

    def visit(self, url: str) -> None:
        self.browser.append(url)
        # clear forward history everytime we visit as per instructions
        self.forwardHistory = []

    def back(self, steps: int) -> str:
        if not self.browser:
            return None
        
        if steps >= len(self.browser):
            # make this as len - 1 because we want to still have something always in the browser
            steps = len(self.browser)-1
        
        while steps:
            # remove from browser and add to fwd history
            url = self.browser.pop()
            self.forwardHistory.append(url)
            steps -=1
            
        return self.browser[-1]

    def forward(self, steps: int) -> str:
        if not self.forwardHistory:
            return None if not self.browser else self.browser[-1]
        
        if steps >= len(self.forwardHistory):
            steps = len(self.forwardHistory)
        
        while steps:
            url = self.forwardHistory.pop()
            self.browser.append(url)
            steps -=1
        
        return self.browser[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)