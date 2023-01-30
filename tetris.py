import pygame
from copy import deepcopy
from random import choice, randrange

W, H = 10, 20
TILE = 45
S_SIZE = 720, 940
GS_SIZE = TILE * W, TILE * H
FPS = 60

pygame.init()
screen = pygame.display.set_mode(S_SIZE)
game_screen = pygame.Surface(GS_SIZE)
pygame.display.set_caption("Тетрис")
clock = pygame.time.Clock()

grid = [pygame.Rect(TILE * x, TILE * y, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(W)] for j in range(H)]

animation_count, animation_speed, animation_limit = 0, 60, 2000

background = pygame.image.load('data/bg.jpg').convert()
game_background = pygame.image.load('data/game_bg.jpg').convert()

main_font = pygame.font.Font('font/retro-land-mayhem.ttf', 45)
font = pygame.font.Font('font/retro-land-mayhem.ttf', 30)

tetris_title = main_font.render('TETRIS', True, pygame.Color('darkorange'))
next_title = font.render('Next figure:', True, pygame.Color('black'))
score_title = font.render('Score:', True, pygame.Color('red'))
highscore_title = font.render('Highscore:', True, pygame.Color('green'))

get_color = lambda: (randrange(50, 128), randrange(50, 128), randrange(50, 128))

figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))
color, next_color = get_color(), get_color()

score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}


def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


def get_highscore():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')


def set_highscore(highscore, score):
    highsc = max(int(highscore), score)
    with open('record', 'w') as f:
        f.write(str(highsc))


while True:
    highscore = get_highscore()
    dx, rotate = 0, False
    screen.blit(background, (0, 0))
    screen.blit(game_screen, (20, 20))
    game_screen.blit(game_background, (0, 0))

    # delay
    for i in range(lines):
        pygame.time.wait(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                animation_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True

    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

    # move y
    animation_count += animation_speed
    if animation_count > animation_limit:
        animation_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                animation_limit = 2000
                break

    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

    # check_lines
    line, lines = H - 1, 0
    for row in range(H - 1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            animation_speed += 5
            lines += 1

    # calculate score
    score += scores[lines]

    # draw grid
    [pygame.draw.rect(game_screen, (40, 40, 40), i_rect, 1) for i_rect in grid]

    # draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_screen, color, figure_rect)

    # draw next figure
    for i in range(4):
        figure_rect.x = next_figure[i].x * TILE + 380
        figure_rect.y = next_figure[i].y * TILE + 185
        pygame.draw.rect(screen, next_color, figure_rect)

    # draw field
    for y, row in enumerate(field):
        for x, col in enumerate(row):
            if col:
                figure_rect.x, figure_rect.y = x * TILE, y * TILE
                pygame.draw.rect(game_screen, col, figure_rect)

    # draw titles
    screen.blit(tetris_title, (495, 0))
    screen.blit(next_title, (495, 130))
    screen.blit(score_title, (545, 790))
    screen.blit(font.render(str(score), True, pygame.Color('white')), (580, 850))
    screen.blit(highscore_title, (505, 660))
    screen.blit(font.render(highscore, True, pygame.Color('gold')), (560, 720))

    # game over
    for i in range(W):
        if field[0][i]:
            set_highscore(highscore, score)
            field = [[0 for i in range(W)] for i in range(H)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0
            for i_rect in grid:
                pygame.draw.rect(game_screen, get_color(), i_rect)
                screen.blit(game_screen, (20, 20))
                pygame.display.flip()
                clock.tick(200)

    pygame.display.flip()
    clock.tick(FPS)
