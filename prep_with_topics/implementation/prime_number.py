"""
Count prime numbers with <= n
"""

def solution(n):
    answer = 0

    cnt = n - 1

    for i in range(2, n+1):
        for x in range(2, int(i**0.5 + 1)):
            if i % x == 0:
                cnt -= 1
                break
    answer = cnt

    return answer



if __name__ == "__main__":
    n = [
        10, 5
    ]
    ans = [
        4, 3
    ]

    for idx, item, a in zip(range(1, len(n)+1), n, ans):
        print(f"case {idx}:", solution(item) == a)
