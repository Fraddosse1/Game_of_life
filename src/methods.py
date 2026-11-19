CELL_GRID_RATIO = 10

import pygame

def screenSize(path):
    with open(path, "r", encoding="utf-8") as f:
        height = 0
        width = 0

        for line in f:
            if not width:
                for c in line:
                    width+=1
            height+=1
    return (height*CELL_GRID_RATIO + 30), (width*CELL_GRID_RATIO + 100)

def readGridFile(path):
    with open(path, "r", encoding="utf-8") as f:
        l = []
        i = 0
        j = 0

        while True:
            c = f.read(1)

            if not c:
                return l
            elif c == "\n":
                j+=1
                i=0

            if c == "1":
                l.append((i,j))
            i+=1
        

def greedToScreen(position):
    x = position[0]*CELL_GRID_RATIO
    y = position[1]*CELL_GRID_RATIO
    return (x, y, CELL_GRID_RATIO, CELL_GRID_RATIO)

def drawText(text, font, color, screen_width_margin, screen_height_margin, screen):
    surface = font.render(text, False, color)
    f_rect = surface.get_rect(center=(screen_width_margin, screen_height_margin))
    screen.blit(surface, f_rect)

def drawPlayButton(screen, color, rect):
    points = [
        (rect.left, rect.top),
        (rect.left, rect.bottom),
        (rect.right, rect.centery)
    ]
    pygame.draw.polygon(screen, color, points)

def drawPauseButton(screen, color, rect):
    bar_width = rect.width // 3
    left_bar = pygame.Rect(rect.left, rect.top, bar_width, rect.height)
    right_bar = pygame.Rect(rect.right - bar_width, rect.top, bar_width, rect.height)
    pygame.draw.rect(screen, color, left_bar)
    pygame.draw.rect(screen, color, right_bar)