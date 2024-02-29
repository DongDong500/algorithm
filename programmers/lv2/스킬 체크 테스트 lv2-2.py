def solution(relation):
    """ +, -, *
    """
    answer = 0

    def cutstr(r):
        nums, ops = [], []
        num = ''
        for idx in range(len(r)):
            if r[idx] == '+' or r[idx] == '-' or r[idx] == '*':
                ops.append(r[idx])
                nums.append(int(num))
                num = ''
            else:
                num += r[idx]
        nums.append(int(num))

        return nums, ops
    
    def calculate(a, b, op):
        if op == '+':
            return int(a) + int(b)
        elif op == '-':
            return int(a) - int(b)
        else:
            return int(a) * int(b)

    def cal(nums, ops, priority):
        val = 0

        for p in priority:
            for i, op in enumerate(ops):
                if p == op:
                    nums[i] = calculate(nums[i], nums[i+1], op)
                    nums.pop(i+1)
                    ops.pop(i)
        val = abs(nums[-1])

        return val
    
    nums, ops = cutstr(relation)

    for fop in ['+', '-', '*']:
        for sop in set(['+', '-', '*']) - set(fop):
            for lop in set(['+', '-', '*']) - set([fop, sop]):
                val = cal(nums, ops, [fop, sop, lop])
                if answer <= val:
                    answer = val
    
    return answer


if __name__ == "__main__":

    E = [
        "100-200*300-500+20",
        "50*6-3*2"
    ]
    ans = [
        60420,
        300
    ]

    for idx, e, a in zip(range(1, len(E) + 1), E, ans):
        print(solution(e) == a)