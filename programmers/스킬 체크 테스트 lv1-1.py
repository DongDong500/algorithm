def solution(n):
    """ Count prime numbers with <= n 
    """
    answer = 0

    def prime(n):
        # count prime numbers <= n
        count = n-1
        for i in range(2,n+1):
            for x in range(2,int(i**0.5 + 1)):
                if i % x == 0:
                    count -= 1
                    break
        return count

    def sol_alpha(n):
        answer = 0
        for i in range(2, n + 1):
            isPrime = True
            # search from 2 to the square root of n+1
            upper = int(i**0.5 + 1)

            for p in range(2, upper):
                if i % p == 0:
                    isPrime = False
                    break
            if isPrime:
                answer += 1
        return answer


    answer = prime(n)
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