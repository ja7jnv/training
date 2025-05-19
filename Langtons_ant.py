# Langton's Ant シミュレーション（初期状態＆速度選択対応）
# This program simulates Langton's ant.
# The ant moves on a grid of black and white cells, changing the color of the cell it visits and turning based on the color.
# The ant starts facing up and turns right on a white cell and left on a black cell.


import pygame
import numpy as np

# 定数
GRID_SIZE = 101  # グリッドのサイズ (101x101)
CELL_SIZE = 5    # 各セルのピクセルサイズ
WHITE = (255, 255, 255)  # 白
BLACK = (0, 0, 0)        # 黒

# 方向：0=上, 1=右, 2=下, 3=左
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def get_initial_state(grid_size):
    while True:
        try:
            N = int(input("初期状態を選択してください（0:全白, 1:中央黒, N>1:ランダムN×N）[0]: ") or "0")
            if N < 0 or N > grid_size:
                raise ValueError
            return N
        except ValueError:
            print("無効な入力です。0以上、かつグリッドサイズ以下の整数を入力してください。")

def get_speed_setting():
    while True:
        try:
            speed = int(input("アリのスピード（1:最遅〜10:最速）省略時[5]: ") or "5")
            if 1 <= speed <= 10:
                return speed
            else:
                raise ValueError
        except ValueError:
            print("1〜10の整数を入力してください。")

class LangtonsAnt:
    def __init__(self, grid_size, init_state=0):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.color_grid = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)
        self.color_grid[:, :] = WHITE
        self.ant_position = (grid_size // 2, grid_size // 2)
        self.ant_direction = 0

        # 初期状態設定
        if init_state == 1:
            cx, cy = self.ant_position
            self.grid[cy, cx] = 1
            self.color_grid[cy, cx] = BLACK
        elif init_state > 1:
            start = grid_size // 2 - init_state // 2
            end = start + init_state
            random_block = np.random.randint(0, 2, size=(init_state, init_state))
            self.grid[start:end, start:end] = random_block
            self.color_grid[start:end, start:end] = np.where(
                random_block[..., None] == 1, BLACK, WHITE
            )

    def update(self):
        x, y = self.ant_position
        current_cell = self.grid[y, x]

        # 色を反転
        self.grid[y, x] = 1 - current_cell
        self.color_grid[y, x] = WHITE if current_cell == 1 else BLACK

        # 向きを変更
        if current_cell == 0:
            self.ant_direction = (self.ant_direction + 1) % 4  # 白：右へ
        else:
            self.ant_direction = (self.ant_direction - 1) % 4  # 黒：左へ

        # 前進
        dx, dy = DIRECTIONS[self.ant_direction]
        self.ant_position = ((x + dx) % self.grid_size, (y + dy) % self.grid_size)

def main():
    pygame.init()

    init_state = get_initial_state(GRID_SIZE)
    speed = get_speed_setting()
    delay = 2 ** (10 - speed)  # 高速（speed=1）→delay=512, 遅い（speed=10）→delay=1

    screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
    pygame.display.set_caption("Langton's Ant")
    clock = pygame.time.Clock()

    ant_simulation = LangtonsAnt(GRID_SIZE, init_state)

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused

        if not paused:
            ant_simulation.update()

        scaled_surface = pygame.transform.scale(
            pygame.surfarray.make_surface(ant_simulation.color_grid),
            (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
        )
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(1000 // delay)

    pygame.quit()

if __name__ == "__main__":
    main()

