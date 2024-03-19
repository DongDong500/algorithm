"""


"""
def solution(seoul):
    answer = ''

    for i, s in enumerate(seoul):
        if 'Kim' in s:
            answer = f"김서방은 {i}에 있다"
            break

    return answer


if __name__ == "__main__":
    

    seoul = [['Jane', 'Kim']]
    result = [
        "김서방은 1에 있다"
    ]

    for s, rst in zip(seoul, result):
        print(solution(s) == rst)