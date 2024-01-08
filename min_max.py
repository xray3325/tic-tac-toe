from copy import deepcopy

score = [['x', 'o', 'x'],
         ['x', 'x', 0],
         ['x', 0, 0]]

def value(score):
    for i in range(3):
        if len(set(score[i])) == 1 and 0 not in score[i]:
            if 'o' in set(score[i]):
                return -1
            else:
                return 1

    new_score = [[score[i][j] for i in range(len(score))]
                for j in range(len(score[0])-1, -1, -1)]

    for j in range(3):
        if len(set(new_score[j])) == 1 and 0 not in new_score[j]:
            if 'o' in set(score[j]):
                return -1
            else:
                return 1

    diagonal = []
    zigonal = []

    for z in range(3):
        diagonal.append(score[z][z])

    for x in range(2, -1, -1):
        zigonal.append(score[abs(x-2)][x])

    if len(set(diagonal)) == 1 and 0 not in diagonal:
        if 'o' in set(score[j]):
            return -1
        else:
            return 1

    elif len(set(zigonal)) == 1 and 0 not in zigonal:
        if 'o' in set(score[j]):
            return -1
        else:
            return 1
        
    elif 0 not in score[0] and 0 not in score[1] and 0 not in score[2]:
        return 0

def player(score):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if score[i][j] == 'x':
                x += 1
            elif score[i][j] == 'o':
                o += 1
    if x == o:
        return "max"
    else:
        return "min"

def actions(score):
    actions = []
    for i in range(3):
        for j in range(3):
            if score[i][j] == 0:
                actions.append(i*3 + j)
    return actions

def result(score, actions):
    lista = []
    for i in actions:
        score[i // 3][i % 3] = 'x'
        lista.append(deepcopy(score))
        score[i // 3][i % 3] = 0
    return lista

print(result(score, actions(score)))
