def solution_a(people, limit):
    answer = 0
    
    from collections import deque
    people = deque(sorted(people, reverse=True))
    while people:
        answer += 1
        l = people.popleft()
        s = l
        while people:
            if s + people[-1] <= limit:
                r = people.pop()
                s += r
            else:
                break

    return answer

def solution(people, limit):
    answer = 0
    
    from collections import deque
    people = deque(sorted(people))
    while people:
        answer += 1
        l = people.popleft()
        s = l
        while people:
            if s + people[0] <= limit:
                r = people.popleft()
                s += r
            else:
                break

    return answer

if __name__ == "__main__":

    P = [
        [70, 50, 80, 50],
        [70, 80, 50],
        [100]
    ]
    L = [
        100,
        100,
        100
    ]
    R = [
        3,
        3,
        1
    ]
    for p, l, r in zip(P, L, R):
        print(solution(p, l) == r)