def solution(numbers):
    answer = []

    numbers = sorted(numbers)

    for i, a in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            tar = a + numbers[j]
            if tar not in answer:
                answer.append(tar)

    return answer



if __name__ == "__main__":
    numbers = [
        [2,1,3,4,1],
        [5,0,2,7],
        [1, 1]
    ]
    ANS = [
        [2,3,4,5,6,7],
        [2,5,7,9,12],
        [2]
    ]
    for n, ans in zip(numbers, ANS):
        print(solution(n) == ans)