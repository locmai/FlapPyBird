import sys
import pygame
from objects import Bird, Ground, PipeObj
from config import SIZE, BACKGROUND_COLOR

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('FlapPy Bird')

bird = Bird()
ground = Ground()
# First pipe
pipe_lists = [PipeObj()]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.fly_up()
        print(event)
    pipe_lists = [pipe for pipe in pipe_lists if not pipe.offscreen()]

    # Update positions
    bird.update_pos()
    for pipe in pipe_lists:
        pipe.update_pos()

    if pipe_lists[-1].need_more_pipe():
        pipe_lists.append(PipeObj())

    screen.fill(BACKGROUND_COLOR)
    for pipe in pipe_lists:
        screen.blit(pipe.top_pipe_image, pipe.pipe_top_pos())
        screen.blit(pipe.bottom_pipe_image, pipe.pipe_bottom_pos())
    screen.blit(bird.bird_image, bird.bird_pos())
    screen.blit(ground.ground_image, ground.ground_pos())
    pygame.display.update()
