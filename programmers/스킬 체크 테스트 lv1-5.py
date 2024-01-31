def solution(t, p):
    answer = 0

    p_len = len(p)

    for i in range(len(t) - p_len + 1):
        subint = int(t[i:i+p_len])
        if subint <= int(p):
            answer += 1

    return answer



if __name__ == "__main__":
    T = [
        "3141592",
        "500220839878",
        "10203"
    ]
    P = [
        "271", "7", "15"
    ]
    ANS = [
        2, 8, 3
    ]

    for t, p, ans in zip(T, P, ANS):
        print(solution(t, p) == ans)