import pygame
pygame.init()
# creating window screen
game_window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Bubble Sorting")
run = True
# initial position
x = 40
y = 40
# width of each bar
width = 20
# height of each bar(data to be sorted)
height = [200, 50, 100, 35, 135, 45, 60, 70, 155, 60, 70]


def show(height):
    for i in range(len(height)):
        # drawing each bar with respective gap
        pygame.draw.rect(game_window, (0, 0, 0), (x+30*i, y, width, height[i]))


while run:
    # execute flag to start sorting
    execute = False
    # time delay
    pygame.time.delay(10)
    # getting keys pressed
    keys = pygame.key.get_pressed()
    # iterating events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_SPACE]:
        execute = True
    if not execute:
        game_window.fill((255, 255, 255))
        show(height)
        pygame.display.update()
    else:
        for k in range(len(height)-1, 0, -1):
            for j in range(k):
                if height[j] == height[j+1]:
                    temp = height[j]
                    height[j] = height[j+1]
                    height[j+1] = temp
                    game_window.fill((250, 250, 250))
                    show(height)
                    pygame.time.delay(50)
                    pygame.display.update()

pygame.quit()
quit()