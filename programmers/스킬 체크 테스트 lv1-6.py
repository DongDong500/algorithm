"""
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


"""

def solution(new_id):
    answer = ''

    """
    3 <= len of id <= 15
    only numbers, little aphabets, _, -, .
    not consecutive . and cannot position first and last of word
    """
    def lowerch(id):
        id = list(id)
        for i, ch in enumerate(id):
            if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
                newch = chr(ord(ch) - ord('A') + ord('a'))
                id[i] = newch
        id = ''.join(id)
        return id

    def trim(id):
        from collections import deque
        Q = deque(list(id))
        out = []
        while Q:
            ch = Q.popleft()
            if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
                out.append(ch)
                continue
            elif ch == '.' or ch == '-' or ch == '_':
                out.append(ch)
                continue
            elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
                out.append(ch)
                continue
            else:
                continue
        id = ''.join(out)
        return id
    
    def eliminateDot(id):
        from collections import deque
        Q = deque(list(id))
        out = []
        cnt = 0
        while Q:
            ch = Q.popleft()
            if ch == '.':
                cnt += 1
                if cnt > 1:
                    continue
                else:
                    out.append(ch)
            else:
                cnt = 0
                out.append(ch)

        if out[0] == '.':
            out.pop(0)
        if out[-1] == '.':
            out.pop(-1)

        if len(out) == 0:
            out.append('a')

        if len(out) > 15:
            id = ''.join(out)
            if id[14] == '.':
                id = id[:14]
            else:
                id = id[:15]
        else:
            id = ''.join(out)

        if len(id) <= 2:
            while len(id) > 3:
                id += id[-2:-1]
        return id

    new_id = lowerch(new_id)
    new_id = trim(new_id)
    new_id = eliminateDot(new_id)

    new_id = answer
    return answer



if __name__ == "__main__":
    new_id = [
        "...!@BaT#*..y.abcdefghijklm.",
        "z-+.^.",
        "=.=",
        "123_.def",
        "abcdefghijklmn.p"
    ]
    result = [
        "bat.y.abcdefghi",
        "z--",
        "aaa",
        "123_.def",
        "abcdefghijklmn"
    ]

    for n, r in zip(new_id, result):
        print(solution(n) == r)