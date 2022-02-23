n, m = map(int, input().split())
bw_board = []
w_chess = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"]
b_chess = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
error = []
def chess_check(lst):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (lst[0][0] == "W") | (lst[7][7] == "W") :
                if w_chess[i][j] != lst[i][j]:
                    cnt += 1
            elif (lst[0][0] == "B") | (lst[7][7] == "B"):
                if b_chess[i][j] != lst[i][j]:
                    cnt += 1
    error.append(cnt)

for _ in range(n):
    bw_board.append(input())

for i in range(n-7):
    pre_new_chess = bw_board[i:i+8]
    for k in range(m-7):
        new_chess = []
        for j in pre_new_chess:
            new_chess.append(j[k:k+8])
        chess_check(new_chess)

print(min(error))