def checkwin(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != "*": 
            return True
        if game[0][i] == game[1][i] == game[2][i] != "*": 
            return True

    if game[0][0] == game[1][1] == game[2][2] != "*": 
        return True
    if game[0][2] == game[1][1] == game[2][0] != "*": 
        return True

    return False

def printboard(game):
    for row in game:
        print(row)
    print()

game = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
win = False
player1 = True

print("Game Instructions: Please input 0, 1, or 2 for row followed by 0, 1, or 2 for column. Enter the first player's name:")
x = input()
print("Enter the second player's name:")
y = input()

while not win:
    printboard(game)
    if player1:
        print(x + ", enter row number:")
    else:
        print("It's your turn, " + y + ". Enter row number:")
    
    row = int(input())
    print("Enter column number:")
    col = int(input())

    if 0 <= row < 3 and 0 <= col < 3:
        if game[row][col] == "*":
            game[row][col] = "X" if player1 else "O"
            if checkwin(game):
                printboard(game)
                print("Congratulations " + (x if player1 else y) + ", you win!")
                win = True 
            player1 = not player1
        else:
            print("Cell taken.")
    else:
        print("Invalid input, enter numbers between 0 and 2")
