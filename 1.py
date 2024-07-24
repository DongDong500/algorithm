def solution(plants, watered):
    answer = []

    M = len(watered)
    N = len(plants)
    idx = [1 for _ in range(N)]

    for m in watered:
        plants[m-1] += 1
        for i in range(N):
            plants[i] -= 1
            if idx[i] == 1 and plants[i] == 0:
                N -= 1
                idx[i] = 0
        answer.append(N)

    return answer


if __name__ == "__main__":
    plants = [[2, 3, 1, 2]]
    watered = [[3, 1, 2, 1, 4, 1]]

    for p, w in zip(plants, watered):
        print(solution(p, w))