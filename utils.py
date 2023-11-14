from random import randint as rand


# функция случайного места
def randbool(r, mxr):
    t = rand(0, mxr)
    return t <= r

# генератор истока
def rand_cell(w, h):
    tw = rand(0, w - 1)
    th = rand(0, h - 1)
    return th, tw

# 0-up, 1-righr, 2-down, 3-left  => индексы списка

# функция продолжения реки
def rand_cell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][-1]
    return x + dx, y + dy
