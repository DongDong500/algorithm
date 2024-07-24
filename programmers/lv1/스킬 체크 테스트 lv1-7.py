"""
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

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