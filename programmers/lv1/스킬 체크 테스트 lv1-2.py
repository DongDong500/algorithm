def solution(s):
    answer = True

    for ch in s:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            answer = False
            break
        elif ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            answer = False
            break
        elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
            continue
        else:
            answer = False
            break

    return answer


if __name__ == "__main__":

    s = [
        "a234",
        "1234",
        "54854342132005487864534321",
        "SD34343434",
        "3423432342523452#@#@"
    ]

    for item in s:
        print(solution(item))

    