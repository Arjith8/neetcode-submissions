class WordDictionary:

    def __init__(self):
        self.source = {}
        

    def addWord(self, word: str) -> None:
        current = self.source
        for i in word:
            current[i] = current.get(i, {})
            current = current[i]
        
        current[None] = True            
        

    def search(self, word: str) -> bool:
        stack = [self.source]
        for i in word:
            if not stack:
                return False

            if i == '.':
                temp = []
                while stack:
                    current = stack.pop()
                    for j in current:
                        if (j is not None):
                            if word == "a.d.":
                                print(j)
                            temp.append(current[j])
                stack = temp
            else:
                temp = []
                while stack:
                    current = stack.pop()
                    if i in current and i is not None:
                        temp.append(current[i])
                stack = temp

            if word == ".ay":
                print(stack)

        # print(stack, word)
        for i in stack:
            if None in i:
                return True
        return False