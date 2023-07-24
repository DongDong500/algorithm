# Q1. Find largest area and the number of white zone.

if __name__ == "__main__":

    v = [
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1]
    ]  
    
    def span(j, i):
        s = 1
        if i - 1 > 0:
            if v[j][i-1] == 1 and not occupied[j][i-1]:
                occupied[j][i-1] = True
                s += span(j, i-1)
        if i + 1 < len(v[0]):
            if v[j][i+1] == 1 and not occupied[j][i+1]:
                occupied[j][i+1] = True
                s += span(j, i+1)
        if j - 1 > 0:
            if v[j-1][i] == 1 and not occupied[j-1][i]:
                occupied[j-1][i] = True
                s += span(j-1, i)
        if j + 1 < len(v):
            if v[j+1][i] == 1 and not occupied[j+1][i]:
                occupied[j+1][i] = True
                s += span(j+1, i)

        return s

    occupied = []
    cnt = 0
    size = 0

    # initialize
    for j in range(0, len(v)):
        tmp = []
        for i in range(0, len(v[0])):
            tmp.append(False)
        occupied.append(tmp)
    
    for i in range(0, len(v[0])):
        for j in range(0, len(v)):
            if not occupied[j][i] and v[j][i] == 1:
                occupied[j][i] = True
                cnt += 1
                tmp = span(j, i)
                if size < tmp:
                    size = tmp

    print(f"cnt: {cnt}, size: {size}")

