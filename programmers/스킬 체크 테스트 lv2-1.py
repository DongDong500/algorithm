def solution(relation):
    import itertools
    answer = 0

    def minkey(uniquekey, tar):
        for u in uniquekey:
            diff = set(u) - set(tar)
            if len(diff) == 0:
                return False
        return True       

    row, col = len(relation), len(relation[-1])

    cnt, cidx = 0, [i for i in range(col)]
    ANS = []
    for i in range(col):
        nCr = itertools.combinations(cidx, i+1)
        for g in nCr:
            unique = True
            for r in range(row):
                pivot = [relation[r][i] for i in g]
                for idx in range(r+1, row):
                    tar = [relation[idx][i] for i in g]
                    if pivot == tar:
                        unique = False
                        break
                if not unique:
                    break
            if unique and minkey(ANS, g):
                cnt += 1
                ANS.append(g)
    
    answer = cnt
    return answer


if __name__ == "__main__":

    R = [
        [
            ["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]
        ]
    ]
    ans = [
        2
    ]

    for idx, r, a in zip(range(1, len(R) + 1), R, ans):
        print(solution(r) == a)