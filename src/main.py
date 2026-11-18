import pygame
import methods as m

# Hyperparameters
GRID_FILE_PATH = "grid.txt"
SCREEN_HEIGTH, SCREEN_WIDTH = m.screenSize(GRID_FILE_PATH)
FONT = "Comic Sans MS"
FONT_SIZE = 30

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()
running = True

cells_alive = m.readGridFile(GRID_FILE_PATH)
frequency = 10
generation = 1
pause = False

text_font = pygame.font.SysFont(FONT, FONT_SIZE)
play_rect = pygame.Rect(SCREEN_WIDTH-100, 90, 20, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                frequency+=1
            elif event.key == pygame.K_DOWN and frequency > 1:
                frequency-=1
            elif event.key == pygame.K_SPACE:
                pause = not pause

    if not pause:
        screen.fill("black")

        # Update the cells
        cells_update = {}
        for cell_alive in cells_alive:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    sum=0
                    cell = (cell_alive[0]+i, cell_alive[1]+j)

                    # Skip already updated cells
                    if (cell in cells_update):
                        continue

                    # Check the neighbors of each cell
                    for k in range(-1, 2, 1):
                        for p in range(-1, 2, 1):
                            # Skip itself
                            if (k==0 and p==0):
                                continue
                            elif (cell[0]+k, cell[1]+p) in cells_alive:
                                sum+=1

                    if sum == 2:
                        # No update
                        if cell in cells_alive:
                            screen.fill("white", m.greedToScreen(cell))
                    elif sum == 3:
                        screen.fill("white", m.greedToScreen(cell))

                        # A new cell is born
                        if cell not in cells_alive:
                            cells_update[cell] = "1"
                    else:
                        # The cell dies
                        if cell in cells_alive:
                            cells_update[cell] = "0"
        
        for cell in cells_update:
            if cells_update[cell] == "1":
                cells_alive.append(cell)
            else:
                cells_alive.remove(cell)
        generation += 1

        # Update text
        # Frequency
        m.drawText(text = "Frequency : "+str(frequency),
                    font = text_font,
                    color = "Red",
                    screen_width_margin = SCREEN_WIDTH-100,
                    screen_height_margin = 30,
                    screen = screen)

        # Generation
        m.drawText(text = "Generation : "+str(generation),
            font = text_font,
            color = "Red",
            screen_width_margin = SCREEN_WIDTH-100,
            screen_height_margin = 60,
            screen = screen)

    
    # Update pause button
    pygame.draw.rect(screen, "Black", play_rect)
    if pause:
        m.drawPauseButton(screen, "Red", play_rect)
    else:
        m.drawPlayButton(screen, "Red", play_rect)   
    
    pygame.display.flip()

    clock.tick(frequency)  # limits FPS to 60

pygame.quit()