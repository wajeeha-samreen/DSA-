class Solution:

    def Anagrams(self, words):
        d={}
        for i in words:
            x=''.join(sorted(i))
            if x in d:
                d[x].append(i)
            else:
                d[x]=[i]
        return list(d.values())
