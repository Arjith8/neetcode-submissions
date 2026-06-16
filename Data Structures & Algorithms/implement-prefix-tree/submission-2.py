class PrefixTree:

    def __init__(self):
        self.source = {}
        

    def insert(self, word: str) -> None:
        current = self.source
        for i in word:
            current[i] = current.get(i, {})
            current = current[i]
        
        current[None] = True


    def search(self, word: str) -> bool:
        current = self.source
        for i in word:
            if i not in current:
                return False
            current = current[i]
        
        return current.get(None, False)
        

    def startsWith(self, prefix: str) -> bool:
        current = self.source
        for i in prefix:
            if i not in current:
                return False
            current = current[i]

        return True
        
        