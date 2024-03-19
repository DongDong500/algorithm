"""
각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.

보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.

"""
def solution(board, h, w):
    answer = 0

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    H = len(board)
    W = len(board[-1])

    for x, y in zip(dx, dy):
        if h + y < H and h + y >= 0:
            if w + x < W and w + x >= 0:
                pivot = board[h][w]
                tar = board[h + y][w + x]
                if board[h][w] == board[h + y][w + x]:
                    answer += 1

    return answer


if __name__ == "__main__":
    

    board = [
        [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],
        [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
    ]
    H = [1, 0]
    W = [1, 1]
    result = [
        2, 1
    ]

    for b, h, w, r in zip(board, H, W, result):
        print(solution(b, h, w) == r)