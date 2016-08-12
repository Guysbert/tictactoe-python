import re
import json

level = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def check_draw():
    return not any(" " in row for row in level)

def check_diagonal(rows):
    return check_rows([[level[0][0], level[1][1], level[2][2]], [level[0][2], level[1][1], level[2][0]]])


def check_rows(rows):
    for i in range(0, len(rows)):
        if rows[i] == ["X", "X", "X"] or rows[i] == ["O", "O", "O"]:
            return True


def check_win():
    level_transposed = [list(i) for i in zip(*level)]
    return check_rows(level) or check_rows(level_transposed) or check_diagonal(level)


row_nums = {"A": 0, "B": 1, "C": 2}


def print_level():
    print "  A B C"
    for row in range(0, len(level)):
        print "%d %s %s %s" % (row + 1, level[row][0], level[row][1], level[row][2])


def do_move(move, player1):
    match = re.match(ur'^(A|B|C)(1|2|3)$', move)
    if match is not None:
        x = int(move[1]) - 1
        y = int(row_nums[move[0]])
        field = level[x][y]
        if field == " ":
            if player1:
                level[x][y] = "X"
            else:
                level[x][y] = "O"
            return True
        else:
            print "Field is not playable"
            return False


player1 = True
move = ""
print_level()
while move != "exit":
    if player1:
        move = raw_input("Make your move Player 1: ")
    else:
        move = raw_input("Make your move Player 2: ")
    if do_move(move, player1):
        print_level()
        if check_win():
            print "Player 1 wins" if player1 else "Player 2 wins"
            exit()
        if check_draw():
            print "Nobody wins"
            exit()
        player1 = not player1
