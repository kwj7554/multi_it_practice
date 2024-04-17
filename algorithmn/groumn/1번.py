import sys

N= int(sys.stdin.readline())
board=[]

for i in range(N):
    board.append(sys.stdin.readline().split())


print(board)