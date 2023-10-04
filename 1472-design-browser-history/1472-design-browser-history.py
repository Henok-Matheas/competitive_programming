class BrowserHistory:
    
    """
    
    so what if for forward, we have a count for indexing
    
    and for backward we will just use the list
    
    for visit we will just make count of forward 0
    
    
    problem?
    
    pseudocode:
    
    we will have a history
    forward_count
    current_page
    
    visit:
    current_page += 1
    forward_count = 0
    
    if current_page == len(history):
    append
    
    history[current_page] = url
    
    
    forward:
    steps = min(steps, forward_count)
    current_page += steps
    forward_count -= steps
    return history[current_page]
    
    backward:
    steps = max(0, current_page - steps)
    forward_count += steps
    current_page -= steps
    return history[current_page]
    
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0
        self.forward_count = 0

    def visit(self, url: str) -> None:
        self.current_page += 1
        self.forward_count = 0
        
        if self.current_page == len(self.history):
            self.history.append("")
        
        self.history[self.current_page] = url

    def back(self, steps: int) -> str:
        steps = min(self.current_page, steps)            
        self.current_page -= steps
        self.forward_count += steps
        
        return self.history[self.current_page]
        

    def forward(self, steps: int) -> str:
        steps = min(steps, self.forward_count)
        self.current_page += steps
        self.forward_count -= steps
        
        return self.history[self.current_page]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)