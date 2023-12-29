import pygame as py

py.init()

WIDTH = 1200
HEIGHT = 800

win = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
my_font = py.font.SysFont('Comic Sans MS', 80)

class field():
    def __init__(self, x, y, width, height, row, column):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.clicked = False

    def draw(self):
        py.draw.rect(win, "white", (self.x, self.y, self.width, self.height), 1)

    def return_rect(self):
        rect = py.Rect(self.x, self.y, self.width, self.height)
        return rect
    
    def return_pos(self):
        pos = (self.x, self.y)
        return pos

def game(m, n, middle):
    global score
    global player

    if score[m][n] == 0:
        score[m][n] = player 
    draw_xo(player, middle)
    check_win()
    player = 'x' if player == 'o' else 'o'

def draw_xo(player, middle):
    size = 75
    if player == "x":
        A = (middle[0]-size, middle[1]+size)
        B = (middle[0]+size, middle[1]-size)
        A_1 = (middle[0]-size, middle[1]-size)
        B_1 = (middle[0]+size, middle[1]+size)
        py.draw.line(win, "white", A, B, 3)
        py.draw.line(win, "white", A_1, B_1, 3)
    elif player == "o":
        py.draw.circle(win, "white", middle, size, 3)

def check_win():
    for i in range(3):
        if len(set(score[i])) == 1 and 0 not in score[i]:
            print(f"wygrana poziomo {i}")
            end(f'h{i}')

    new_score = [[score[i][j] for i in range(len(score))] for j in range(len(score[0])-1, -1, -1)]

    for j in range(3):
        if len(set(new_score[j])) == 1 and 0 not in new_score[j]:
            print(f"wygrana pionowo {abs(j-2)}")
            end(f"v{abs(j-2)}")

    diagonal = []
    zigonal = []

    for z in range(3):
        diagonal.append(score[z][z])

    for x in range(2, -1, -1):
        zigonal.append(score[abs(x-2)][x])

    if len(set(diagonal)) == 1 and 0 not in diagonal:
        print("lewo gora")
        end('l')

    elif len(set(zigonal)) == 1 and 0 not in zigonal:
        print("prawo gora")
        end('r')
    elif 0 not in score[0] and 0 not in score[1] and 0 not in score[2]:
         restart()

def end(position):
    global player
    global buttons
    global x, o
    if player == 'x':
        x += 1
    else:
        o += 1
    for obj in buttons:
        obj.clicked = True

    print(f"{player} won")
    thick = 15

    if position == 'l':
        py.draw.line(win, 'red', (50, 50), (750, 750), thick)
    elif position == 'r':
        py.draw.line(win, 'red', (50, 750), (750, 50), thick)
    elif position == 'h0':
        py.draw.line(win, 'red', (50, 133), (750, 133), thick)
    elif position == 'h1':
        py.draw.line(win, 'red', (50, 399), (750, 399), thick)
    elif position == 'h2':
        py.draw.line(win, 'red', (50, 665), (750, 665), thick)
    elif position == 'v0':
        py.draw.line(win, 'red', (133, 50), (133, 750), thick)
    elif position == 'v1':
        py.draw.line(win, 'red', (399, 50), (399, 750), thick)
    elif position == 'v2':
        py.draw.line(win, 'red', (665, 50), (665, 750), thick)

    restart()

def restart():   
    py.display.flip()
    py.time.delay(2000)

    global score
    py.draw.rect(win, 'black', (0, 0, 1200, 800))
    score = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    py.time.delay(500)
    for obj in buttons:
        obj.clicked = False
        obj.draw()
    py.mouse.set_pos(900, 750)

buttons = []
buttons.append(field(0, 0, 266, 266, 0, 0))
buttons.append(field(266, 0, 266, 266, 0, 1))
buttons.append(field(532, 0, 266, 266, 0, 2))

buttons.append(field(0, 266, 266, 266, 1, 0))
buttons.append(field(266, 266, 266, 266, 1, 1))
buttons.append(field(532, 266, 266, 266, 1, 2))

buttons.append(field(0, 532, 266, 266, 2, 0))
buttons.append(field(266, 532, 266, 266, 2, 1))
buttons.append(field(532, 532, 266, 266, 2, 2))

score = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player = 'x'
x = 0
o = 0
def main():
    running = True
    for obj in buttons:
        obj.draw()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONUP and event.button == 1:
                print(py.time.get_ticks())
                for obj in buttons:
                    if py.Rect.collidepoint(obj.return_rect(), py.mouse.get_pos()) and obj.clicked == False:
                        obj.clicked = True
                        middle = (obj.x + 133, obj.y + 133)
                        game(obj.row, obj.column, middle)

        text_surface = my_font.render('X - O', False, ('white'))
        score = my_font.render(f"{x} - {o}", False, ('white'))
        win.blit(score, (960, 120))
        win.blit(text_surface, (950, 50))

        py.display.flip()
        clock.tick(60)
    quit()

main()
