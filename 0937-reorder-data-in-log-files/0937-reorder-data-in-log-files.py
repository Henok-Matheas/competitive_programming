class Solution:
    def ordering(self, log):
        is_digit = 0
        id_, content = log.split(" ", maxsplit = 1)

        for word in content:
            is_digit |= int(word.isdigit())

        if is_digit:
            id_, content = "", []
            
        return (is_digit, content, id_)
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key = lambda log: self.ordering(log))
        return logs