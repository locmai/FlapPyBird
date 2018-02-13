import pygame
import static
import random
from config import HEIGHT, WIDTH
from config import GROUND_SIZE, GROUND_POS, GROUND_HEIGHT
from config import GRAVITY, BIRD_SIZE, BIRD_PADDING_LEFT, LIFT
from config import PIPE_WIDTH, PIPE_HEIGHT, PIPE_SIZE, PIPE_VELOCITY, PIPE_BASE_RANGE, PIPE_DISTANCE_RANGE, BETWEEN


class Bird:
    def __init__(self):
        __raw_image = pygame.image.load(static.BIRD_IMG_PATH)
        self.bird_image = pygame.transform.scale(__raw_image, BIRD_SIZE)
        self.y = HEIGHT /2 - 60
        self.x = BIRD_PADDING_LEFT
        self.gravity = GRAVITY
        self.velocity = 0

    def update_pos(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def bird_pos(self):
        return self.x, self.y

    def fly_up(self):
        self.y -= LIFT
        self.velocity = 0


class PipeObj:
    def __init__(self):
        self.y1 = random.randint(PIPE_BASE_RANGE, HEIGHT-PIPE_BASE_RANGE) - PIPE_HEIGHT - GROUND_HEIGHT
        self.y2 = self.y1 + PIPE_HEIGHT + PIPE_DISTANCE_RANGE
        self.x = WIDTH

        __raw_image_top_pipe = pygame.image.load(static.PIPE_TOP_IMG_PATH)
        self.top_pipe_image = pygame.transform.scale(__raw_image_top_pipe, PIPE_SIZE)

        __raw_image_bottom_pipe = pygame.image.load(static.PIPE_BOTTOM_IMG_PATH)
        self.bottom_pipe_image = pygame.transform.scale(__raw_image_bottom_pipe, PIPE_SIZE)

    def update_pos(self):
        self.x -= PIPE_VELOCITY

    def offscreen(self):
        return self.x < (0 - PIPE_WIDTH)

    def pipe_top_pos(self):
        return self.x, self.y1

    def pipe_bottom_pos(self):
        return self.x, self.y2

    def need_more_pipe(self):
        return WIDTH - (self.x + PIPE_WIDTH) > BETWEEN


class Ground:
    def __init__(self):
        __raw_image = pygame.image.load(static.GROUND_IMG_PATH)
        self.ground_image = pygame.transform.scale(__raw_image, GROUND_SIZE)

    @staticmethod
    def ground_pos():
        return GROUND_POS