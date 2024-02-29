def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    isopen = False
    open = 0
    for ch in s:
        if ch == '(':
            if isopen:
                open += 1
            else:
                isopen = True
                open += 1
        else:
            if isopen:
                open -= 1
                if open == 0:
                    isopen = False
            else:
                return False
    if isopen:
        return False

    return True


if __name__ == "__main__":

    STR = [
        "()()",
        "(())()",
        ")()()",
        "(()("
    ]
    ANS = [
        True,
        True,
        False,
        False
    ]

    for idx, item in enumerate(zip(STR, ANS)):
        s, ans = item
        print(solution(s) == ans)