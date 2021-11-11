import sys
import pygame
import random
import time

SIZE = WIDTH, HEIGHT = 1024, 700
clock = pygame.time.Clock()
pygame.display.init()

SCREEN = pygame.display.set_mode(SIZE)
# pygame.draw.rect(SCREEN, (162, 205, 205), pygame.Rect((0, 0), (WIDTH, HEIGHT)))

Orange1 = (235, 130, 66)
SoftGreen = (198, 213, 126)
SkyBlue = (162, 205, 205)
colors = [Orange1, SoftGreen, SkyBlue]

seed = time.time()
random.seed(int(seed))
print(int(seed))


def brushStrike(x, y, len2, color, starting_size=30, direction=True):
    if direction:
        hev = vev = 5
    else:
        hev = -5
        vev = 5
    color_c = color[:]
    print(color_c)
    for ii in range(len2):
        pygame.draw.circle(SCREEN, color_c, (x, y), starting_size - (starting_size // len2) * ii)
        x += hev
        y += vev
        color_c = [min(255, c + 1) for c in color_c]
        print(color_c)


# Dibuix
# Fill the background
for i in range(200):
    clock.tick(100)
    brushLen = random.randint(20, 40)
    startSize = random.randint(0, 40)
    color_ind = random.randint(0, 2)
    x = random.randint(0, 1024)
    y = random.randint(0, 700)
    brushStrike(x, y, brushLen, colors[color_ind], startSize, True)
    brushStrike(x + startSize * brushLen, y, brushLen, colors[color_ind], startSize, False)
    pygame.display.flip()
h = 0
dir = 5
for i in range(WIDTH):
    rect = pygame.Rect((i, h), (10, dir))
    #pygame.draw.rect(SCREEN, Orange1, rect)
    h += dir
    if h > 700 or h < 0:
        dir *= -1
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type != pygame.QUIT and event.type != pygame.KEYDOWN:
            continue
        if event.type == pygame.QUIT:
            sys.exit()
