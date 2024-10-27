class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg = {}
        pos = {}
        zeros = 0
        solutions = set()

        for i in nums:
            if i < 0:
                neg.setdefault(i, 0)
                neg[i] += 1
            elif i > 0:
                pos.setdefault(i, 0)
                pos[i] += 1
            else:
                zeros += 1

        for i in {num for num in nums}:
            if i < 0:
                for j in pos:
                    k = -i - j
                    if k in pos:
                        if k == j and pos[j]-1 < 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            elif i > 0:
                for j in neg:
                    k = -i - j
                    if k in neg:
                        if k == j and neg[j]-1 < 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            elif zeros >= 3:
                solutions.add((0, 0, 0))

        return [list(s) for s in solutions]
