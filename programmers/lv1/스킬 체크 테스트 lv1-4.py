def solution(left, right):
    answer = 0

    def cal_square(n):
        import math
        root_n = n**0.5
        up = int(math.ceil(n**0.5))
        low = int(n**0.5)
        for i in range(low-1, up+1):
            if n == i**2:
                return True
        return False

    for n in range(left, right+1):
        if cal_square(n):
            answer -= n
        else:
            answer += n

    return answer


if __name__ == "__main__":
    left = [
        13, 24
    ]
    right = [
        17, 27
    ]
    ANS = [
        43, 52
    ]
    for l, r, ans in zip(left, right, ANS):
        print(solution(l, r) == ans)