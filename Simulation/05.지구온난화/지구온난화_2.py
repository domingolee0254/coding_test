import sys
input = sys.stdin.read
data = input().split()

R = int(data[0])
C = int(data[1])

# 지도 입력을 처리하고, 상하좌우에 경계를 추가합니다.
tmp_map = [['.'] * (C + 2)]
for i in range(R):
    tmp_map.append(['.'] + list(data[2 + i]) + ['.'])
tmp_map.append(['.'] * (C + 2))

# cur_map을 tmp_map과 동일하게 설정합니다.
cur_map = tmp_map

def search(y, x):
    cnt = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if cur_map[ny][nx] == '.':
            cnt += 1
    return cnt

def main():
    contact_map = [[0] * (C + 2) for _ in range(R + 2)]

    x_min = y_min = float('inf')
    x_max = y_max = -float('inf')

    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if cur_map[r][c] == 'X':
                contact = search(r, c)
                contact_map[r][c] = contact

    for rr in range(1, R + 1):
        for cc in range(1, C + 1):
            if contact_map[rr][cc] >= 3:
                cur_map[rr][cc] = '.'

    for rrr in range(1, R + 1):
        for ccc in range(1, C + 1):
            if cur_map[rrr][ccc] == 'X':
                x_min = min(x_min, ccc)
                x_max = max(x_max, ccc)
                y_min = min(y_min, rrr)
                y_max = max(y_max, rrr)

    if x_min > x_max or y_min > y_max:
        print("")
    else:
        for row in range(y_min, y_max + 1):
            print("".join(cur_map[row][x_min:x_max + 1]))

main()