import sys

sys.stdin = open("_박스.txt")
"""
3
5 4
1 0 0 0
0 0 1 0
1 0 0 1
0 1 0 0
1 0 1 0
3 3
1 1 1
1 1 1
0 0 0
5 6
1 0 1 1 0 1
0 0 0 0 0 0
1 1 1 0 0 0
0 0 0 1 1 1
0 1 0 1 0 1
"""
박스 = 1
빈공간 = 0

행_개수, 열_개수 = 5, 4

박스_리스트 = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
]
이동거리 = 0 
# 이중 반복문
# 열부터 순회
for x in range(열_개수):
# 행순회 단, 아래에서 위로 탐색을 한다.
#   # 4 -> 0 -1
    for y in list(range(행_개수))[::-1]:
        
        # 만약에 현재 탐색하고(보고)있는 좌표에 박스가 있으면
        if 박스_리스트[y][x] == 박스:
            
            # y + 1 -> 5 : 조건 만족 X

            # while y+1 != 행_개수 and 박스_리스트[5][x] != 박스:
            while True:
                # 범위를 체크 1순위
                if y+1 == 행_개수:
                    break

                # 값을 체크
                if 박스_리스트[y+1][x] == 박스:
                    break

                박스_리스트[y][x] = 빈공간
                박스_리스트[y+1][x] = 박스
                y += 1
                이동거리 += 1

print(이동거리)
            


