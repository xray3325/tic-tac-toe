import pygame as py
import numpy as np

py.init()

WIDTH = 1200
HEIGHT = 800

win = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player1 = "x"
def draw_x(middle):
    size = 75
    global player1
    if player1 == "x":
        A = (middle[0]-size, middle[1]+size)
        B = (middle[0]+size, middle[1]-size)
        A_1 = (middle[0]-size, middle[1]-size)
        B_1 = (middle[0]+size, middle[1]+size)
        py.draw.line(win, "white", A, B)
        py.draw.line(win, "white", A_1, B_1)
    elif player1 == "o":
        py.draw.circle(win, "white", middle, size, 1)

def grid(lines):
    py.draw.rect(win, "white", (0, 0, 800, 800), 1)
    for i in lines:
        py.draw.line(win, "white", i[0:2], i[2:4])

def mouse():
    mouse_pos = py.mouse.get_pos()
    if (mouse_pos[0] < 260 and mouse_pos[1] < 260):
        draw_xo(0)
    if (mouse_pos[0] > 260 and mouse_pos[0] < 520 and mouse_pos[1] < 250):
        draw_xo(1)
    if (mouse_pos[0] > 520 and mouse_pos[0] < 780 and mouse_pos[1] < 250):
        draw_xo(2)
    if (mouse_pos[0] < 260 and mouse_pos[1] < 520 and mouse_pos[1] > 260):
        draw_xo(3)
    if (mouse_pos[0] > 260 and mouse_pos[0] < 520 and mouse_pos[1] > 260 and mouse_pos[1] < 520):
        draw_xo(4)
    if (mouse_pos[0] > 520 and mouse_pos[1] > 260 and mouse_pos[1] < 520):
        draw_xo(5)
    if (mouse_pos[0] < 250 and mouse_pos[1] > 520):
        draw_xo(6)
    if (mouse_pos[0] > 260 and mouse_pos[0] < 520 and mouse_pos[1] > 520):
        draw_xo(7)
    if (mouse_pos[0] > 520 and mouse_pos[0] < 780 and mouse_pos[1] > 520):
        draw_xo(8)
    

def draw_xo(tile):
    global player1
    if tile == 0 and game[0][0] == 0:
        draw_x((130, 130))
    if tile == 1 and game[0][1] == 0:
        draw_x((390, 130))
    if tile == 2 and game[0][2] == 0:
        draw_x((660, 130))
    if tile == 3 and game[1][0] == 0:
        draw_x((130, 380))
    if tile == 4 and game[1][1] == 0:
        draw_x((390, 380))
    if tile == 5 and game[1][2] == 0:
        draw_x((660, 380))
    if tile == 6 and game[2][0] == 0:
        draw_x((130, 660))
    if tile == 7 and game[2][1] == 0:
        draw_x((390, 660))
    if tile == 8 and game[2][2] == 0:
        draw_x((660, 660))
    if tile <= 2:
        game[0][tile] = player1
    elif tile >= 3 and tile <= 5:
        game[1][tile-3] = player1
    elif tile >= 6 and tile <= 8:
        game[2][tile-6] = player1
        
    if player1 == "x":
        player1 = "o"
    else:
        player1 = "x"

    print(checkWin(game))

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

def identical(array, index):
    if array[index[0]] != 0 and array[index[1]] != 0 and array[index[2]] != 0:
        if array[index[0]] == array[index[1]] and array[index[1]] == array[index[2]]:
            return True
        else:
            return False
def main():
    running = True
    lines = [(260, 0, 260, 800),
             (520, 0, 520, 800),
             (0, 260, 800, 260),
             (0, 520, 800, 520)]
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse()


        grid(lines)

        py.display.flip()
        clock.tick(60)

    quit()

main()

