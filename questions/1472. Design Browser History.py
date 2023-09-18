class BrowserHistory:

    def __init__(self, homepage: str):
        self.list1 = [homepage]
        self.list2 = []
        
    def visit(self, url: str) -> None:
        self.list1.append(url)
        self.list2 = []
        
    def back(self, steps: int) -> str:

        while steps and len(self.list1) > 1:
            self.list2.append(self.list1.pop())
            steps -= 1

        return self.list1[-1]
        
    def forward(self, steps: int) -> str:

        while steps and self.list2:
            self.list1.append(self.list2.pop())
            steps -= 1

        return self.list1[-1]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
