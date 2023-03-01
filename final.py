import pygame
from copy import deepcopy
from random import choice, randrange, randint

snake, tetris, life, tic_tac_toe = 0, 0, 0, 0
if __name__ == "__main__":
    pygame.font.init()
    sc = pygame.display.set_mode((800, 500))
    sc.fill((0, 0, 0))
    fo = pygame.font.SysFont('arial', 60)
    f = pygame.font.SysFont('arial', 30)
    text = f.render('Выберите в какую игру вы хотите поиграть', True, (255, 255, 255))
    sc.blit(text, (150, 10))
    text_1 = f.render('(нажмите на название игры):', True, (255, 255, 255))
    sc.blit(text_1, (220, 60))

    f1 = pygame.font.SysFont('arial', 50)
    text1 = f1.render('Змейка', True, 'red')
    sc.blit(text1, (330, 110))
    pygame.draw.rect(sc, 'white', (320, 110, 160, 60), 3)

    text1 = f1.render('Тетрис', True, 'green')
    sc.blit(text1, (330, 197))
    pygame.draw.rect(sc, 'white', (320, 197, 160, 60), 3)

    text1 = f1.render('Игра "Жизнь"', True, 'blue')
    sc.blit(text1, (270, 285))
    pygame.draw.rect(sc, 'white', (260, 285, 270, 60), 3)

    text1 = f1.render('Крестики-нолики', True, 'yellow')
    sc.blit(text1, (235, 372))
    pygame.draw.rect(sc, 'white', (225, 372, 340, 60), 3)

    f_start = pygame.font.SysFont('arial', 30)

    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = list(event.pos)
                    if 320 <= x <= 480 and 110 <= y <= 170:
                        snake = 1
                        text_start = f_start.render("Хорошо, чтобы начать игру, закройте это окно", True, 'white')
                        sc.blit(text_start, (125, 440))
                    if 320 <= x <= 480 and 197 <= y <= 257:
                        tetris = 1
                        text_start = f_start.render("Хорошо, чтобы начать игру, закройте это окно", True, 'white')
                        sc.blit(text_start, (125, 440))
                    if 260 <= x <= 530 and 285 <= y <= 345:
                        life = 1
                        text_start = f_start.render("Хорошо, чтобы начать игру, закройте это окно", True, 'white')
                        sc.blit(text_start, (125, 440))
                    if 225 <= x <= 565 and 372 <= y <= 432:
                        tic_tac_toe = 1
                        text_start = f_start.render("Хорошо, чтобы начать игру, закройте это окно", True, 'white')
                        sc.blit(text_start, (125, 440))
            pygame.display.update()
    pygame.quit()

if snake == 1:
    if __name__ == "__main__":
        RES = 800
        SIZE = 50

        x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length = 1
        snake = [(x, y)]
        dx, dy = 0, 0
        fps = 60
        dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
        score = 0
        speed_count, snake_speed = 0, 10

        pygame.init()
        surface = pygame.display.set_mode([RES, RES])
        clock = pygame.time.Clock()
        font_score = pygame.font.SysFont('Arial', 26, bold=True)
        font_end = pygame.font.SysFont('Arial', 66, bold=True)
        img = pygame.image.load('1.jpg').convert()


        def close_game():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


        while True:
            surface.blit(img, (0, 0))
            # drawing snake, apple
            [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
            pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
            # show score
            render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
            surface.blit(render_score, (5, 5))
            # snake movement
            speed_count += 1
            if not speed_count % snake_speed:
                x += dx * SIZE
                y += dy * SIZE
                snake.append((x, y))
                snake = snake[-length:]
            # eating food
            if snake[-1] == apple:
                apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
                length += 1
                score += 1
                snake_speed -= 1
                snake_speed = max(snake_speed, 4)
            # game over
            if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
                while True:
                    render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
                    surface.blit(render_end, (RES // 2 - 200, RES // 3))
                    pygame.display.flip()
                    close_game()

            pygame.display.flip()
            clock.tick(fps)
            close_game()
            # controls
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                if dirs['W']:
                    dx, dy = 0, -1
                    dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
            elif key[pygame.K_s]:
                if dirs['S']:
                    dx, dy = 0, 1
                    dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
            elif key[pygame.K_a]:
                if dirs['A']:
                    dx, dy = -1, 0
                    dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
            elif key[pygame.K_d]:
                if dirs['D']:
                    dx, dy = 1, 0
                    dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

if tetris == 1:
    if __name__ == "__main__":
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

if life == 1:
    class Board:

        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            self.left = 10
            self.top = 10
            self.cell_size = 30

        def render(self, screen):
            for row, row_v in enumerate(self.board):
                for col, col_v in enumerate(row_v):
                    color = 'white'
                    rect_width = 1
                    pygame.draw.rect(screen, pygame.Color(color), (
                        self.left + col * self.cell_size, self.top + row * self.cell_size, self.cell_size,
                        self.cell_size),
                                     rect_width)
                    color = 'black'
                    rect_width = 0
                    pygame.draw.rect(screen, pygame.Color(color), (
                        self.left + col * self.cell_size + 1, self.top + row * self.cell_size + 1, self.cell_size - 2,
                        self.cell_size - 2), rect_width)

        def set_view(self, left, top, cell_size):
            self.left, self.top, self.cell_size = left, top, cell_size

        def get_cell(self, mouse_pos):
            x, y = mouse_pos
            if self.left < x < self.left + (self.width * self.cell_size):
                cell_x = (x - self.left) // self.cell_size
            else:
                return
            if self.top < y < self.top + (self.height * self.cell_size):
                cell_y = (y - self.top) // self.cell_size
            else:
                return
            return cell_x, cell_y

        def on_click(self, cell_pos):
            if cell_pos is None:
                return
            row, col = cell_pos[::-1]
            self.board[row][col] = int(not self.board[row][col])

        def get_click(self, mouse_pos):
            cell = self.get_cell(mouse_pos)
            self.on_click(cell)


    class Life(Board):

        def render(self, screen):
            for row, row_v in enumerate(self.board):
                for col, col_v in enumerate(row_v):
                    color = 'white'
                    rect_width = 1
                    pygame.draw.rect(screen, pygame.Color(color),
                                     (self.left + col * self.cell_size,
                                      self.top + row * self.cell_size,
                                      self.cell_size,
                                      self.cell_size),
                                     rect_width)
                    if col_v == 1:
                        color = 'green'
                    elif col_v == 0:
                        continue
                    rect_width = 0
                    pygame.draw.rect(screen, pygame.Color(color),
                                     (self.left + col * self.cell_size + 1,
                                      self.top + row * self.cell_size + 1,
                                      self.cell_size - 2,
                                      self.cell_size - 2),
                                     rect_width)

        def get_cell_by_coord(self, row, col):
            if 0 <= row < self.height and 0 <= col < self.width:
                return self.board[row][col]
            else:
                return 0

        def get_neighbour_cells(self, row, col):
            neighbour_cells = []
            for row_ind in range(row - 1, row + 2):
                for col_ind in range(col - 1, col + 2):
                    if not row_ind - row and not col_ind - col:
                        continue
                    cell = self.get_cell_by_coord(row_ind, col_ind)
                    neighbour_cells.append(cell)
            return neighbour_cells

        def solve_cell(self, row, col):
            cell = self.board[row][col]
            neighbour_cells = self.get_neighbour_cells(row, col)
            living_cells = [i for i in neighbour_cells if i]
            living_cells_count = len(living_cells)
            if not cell:
                if living_cells_count == 3:
                    cell_state = 1
                else:
                    cell_state = 0
            else:
                if not (living_cells_count == 2 or living_cells_count == 3):
                    cell_state = 0
                else:
                    cell_state = 1

            return cell_state

        def next_move(self):
            next_cells = []
            for row_ind, row in enumerate(self.board):
                for col_ind, col in enumerate(row):
                    cell_state = self.solve_cell(row_ind, col_ind)
                    next_cells.append(((row_ind, col_ind), cell_state))
            for (row, col), cell_state in next_cells:
                self.board[row][col] = cell_state


    def main():
        pygame.init()
        size = width, height = 600, 600
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Игра «Жизнь»')
        left, top, cell_size = 0, 0, 15
        board = Life((width - left * 2) // cell_size, (height - top * 2) // cell_size)
        board.set_view(left, top, cell_size)
        running = True
        clock = pygame.time.Clock()
        game_state = False
        timer = 0
        fps = 60
        update_time = 20
        d_update = 100
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        game_state = not game_state
                    elif event.button == 1:
                        board.get_click(event.pos)
                    elif event.button == 4:
                        update_time -= d_update
                    elif event.button == 5:
                        update_time += d_update
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = not game_state
            screen.fill((0, 0, 0))
            if game_state and pygame.time.get_ticks() - timer > update_time:
                timer = pygame.time.get_ticks()
                board.next_move()
            board.render(screen)
            clock.tick(fps)
            pygame.display.flip()
        pygame.quit()


    if __name__ == '__main__':
        main()

if tic_tac_toe == 1:
    class Board_K_N:
        # создаем доску для крестиков-ноликов))
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.colors = ["blue", "red"]
            self.board = [[0] * width for _ in range(height)]
            self.left = 10
            self.top = 10
            self.cell_size = 160
            self.prov = 0
            self.progress = 0
            self.to_win = 0

        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size

        # часть, связанная с показом самик элементов
        def render(self, screen):
            for i in range(self.width):
                for j in range(self.height):
                    # рисуем клетки поля
                    pygame.draw.rect(screen, "black", (self.top + i * self.cell_size, self.left + j * self.cell_size,
                                                       self.cell_size, self.cell_size), 1)
                    if self.board[j][i] == 1:
                        # рисуем крестик, если он нужен
                        pygame.draw.line(screen, "blue",
                                         (self.top + i * self.cell_size + 4, self.left + j * self.cell_size + 4),
                                         (self.top + i * self.cell_size + self.cell_size - 4,
                                          self.left + j * self.cell_size + self.cell_size - 4), width=2)
                        pygame.draw.line(screen, "blue", (
                            self.top + i * self.cell_size + self.cell_size - 4, self.left + j * self.cell_size + 4),
                                         (self.top + i * self.cell_size + 4,
                                          self.left + j * self.cell_size + self.cell_size - 4), width=2)
                    if self.board[j][i] == 2:
                        # рисуем нолик, если он нужен
                        pygame.draw.circle(screen, "red", ((self.top + i * self.cell_size + self.cell_size // 2),
                                                           (self.left + j * self.cell_size + self.cell_size // 2)),
                                           self.cell_size / 2 - 2, width=2)

        def get_cell(self, mouse_pos):
            x, y = mouse_pos[0], mouse_pos[1]
            x_real, y_real = (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
            if 0 <= x_real and x_real <= self.width - 1 and 0 <= y_real and y_real <= self.height - 1:
                return (x_real, y_real)
            else:
                return None

        def on_click(self, cell_coords):
            y, x = cell_coords[0], cell_coords[1]
            self.progress += 1
            # ход пользователя
            if self.board[x][y] == 0:
                self.prov = 1
                self.board[x][y] = 1
            # определяем, куда походит пк
            if self.progress != 5:
                while self.board[x][y] != 0:
                    x, y = randint(0, 2), randint(0, 2)
                self.board[x][y] = 2

            if self.prov_on_win() == 1:
                self.to_win = self.prov_on_win()

        def get_click(self, mouse_pos):
            cell = self.get_cell(mouse_pos)
            if cell:
                self.on_click(cell)

        def prov_on_win(self):
            global running
            global is_win
            # проверка на победу за счет совпадения по цвету
            # провека по горизонтали
            if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
                running = False
                return self.board[0][0]
            elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
                running = False
                return self.board[1][0]
            elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
                running = False
                return self.board[2][0]
            # проверка по наклонным(?)
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
                running = False
                return self.board[0][0]
            elif self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
                running = False
                return self.board[2][0]
            # проверка по вертикали
            elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
                running = False
                return self.board[0][0]
            elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
                running = False
                return self.board[0][1]
            elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
                running = False
                return self.board[0][2]
            else:
                return None


    if __name__ == '__main__':
        # создаем игровое поле
        is_win = 0
        pygame.init()
        pygame.font.init()
        size = width, height = 500, 500
        screen = pygame.display.set_mode(size)
        screen.fill('white')
        board = Board_K_N(3, 3)
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
            screen.fill("white")
            board.render(screen)

            pygame.display.flip()
        pygame.quit()
