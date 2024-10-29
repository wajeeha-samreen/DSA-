# O(n) Mono Stack Solution
class RandomizedCollection:
    def __init__(self):
        self.val = []
        self.mpp = {}

    def insert(self, val: int) -> bool:
        self.mpp.setdefault(val, set()).add(len(self.val))
        self.val.append(val)
        return len(self.mpp[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.mpp or not self.mpp[val]:
            return False
        i = self.mpp[val].pop()
        self.mpp[self.val[-1]].add(i)
        self.mpp[self.val[-1]].remove(len(self.val)-1)
        self.val[i] = self.val[-1]
        self.val.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.val)
