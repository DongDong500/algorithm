

def sol(cells, x, y):

    answer = 0

    def chk(cur, isx, ispos):
        cx, cy = cur

        if isx:
            if ispos:
                for i in range(cx, H):
                    if cells[i][cy] == "#":
                        return [i, cy]
                return [H-1, cy]
            else:
                for i in range(cx, -1, -1):
                    if cells[i][cy] == "#":
                        return [i, cy]
                return [0, cy]
        else:
            if ispos:
                for i in range(cy, W):
                    if cells[cx][i] == "#":
                        return [cx, i]
                return [cx, W-1]
            else:
                for i in range(cy, -1, -1):
                    if cells[cx][i] == "#":
                        return [cx, i]
                return [cx, 0]

    # BFS
    queue = deque()
    queue.append([(0, 0), 0])

    H, W = len(cells), len(cells[-1])
    print("HxW:", H, W)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    CTRL = [True, False]

    while queue:
        pnt, t = queue.pop()
        
        ox, oy = pnt
        print("ox, oy:", type(ox), ox)

        if pnt == (x-1, y-1):
            return t
        
        for ctrl in CTRL:
            for k in range(4):
                if not ctrl:
                    nx, ny = ox + dx[k], oy + dy[k]
                else:
                    if k == 0:
                        nx, ny = chk(pnt, True, True)                    
                    elif k == 1:
                        nx, ny = chk(pnt, True, False)
                    elif k == 2:
                        nx, ny = chk(pnt, False, True)
                    else:
                        nx, ny = chk(pnt, False, False)

                if 0 <= nx < H and 0 <= ny < W:
                    queue.appendleft([(nx, ny), t+1])

    return answer

if __name__ == "__main__":

    from collections import deque

    cells = ["....", "....", "#..."]
    x = 3
    y = 3

    print(sol(cells, x, y))