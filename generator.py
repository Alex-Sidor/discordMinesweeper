import random

emojis = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣"]

def tryAddToPosition(x, y, size):
    if 0 <= x < size and 0 <= y < size and board[x][y] != -1:
        board[x][y] += 1

def addInRadius(x, y, size):
    for dx, dy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
        tryAddToPosition(x+dx, y+dy, size)

numberOfMines = int(input("how many mines\n"))
dimension = int(input("dimension of board\n"))
board = [[0 for _ in range(dimension)] for _ in range(dimension)]

if numberOfMines == -1:
    print("first line\n\n")
    for y in range(dimension - 1, -1, -1):
        line = input()
        board[y] = [-1 if c == '1' else int(c) for c in line]
else:
    count = 0
    while count < numberOfMines:
        a = random.randint(0, dimension - 1)
        b = random.randint(0, dimension - 1)
        if board[a][b] != -1:
            board[a][b] = -1
            addInRadius(a, b, dimension)
            count += 1

startx = -1
starty = -1

while startx == -1:
    a = random.randint(0, dimension - 1)
    b = random.randint(0, dimension - 1)
    if board[a][b] == 0:
            startx = a
            starty = b


print("\n")

for y in range(dimension - 1, -1, -1):
    currentLine = ""
    for x in range(dimension):
        cell = board[x][y]
        if cell == -1:
            currentLine += "||:bomb:||"
        elif cell == 0:
            if(startx == x and starty == y):
                currentLine += "⬜"
            else:
                currentLine += "||⬜||"
        else:
            currentLine += f"||{emojis[cell-1]}||"
    print(currentLine)

print("\n")
print("copy that part ^")
