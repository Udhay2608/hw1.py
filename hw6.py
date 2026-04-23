import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

font = pygame.font.SysFont(None, 40)
text = font.render("Hello Pygame", True, (0, 0, 0))

rect_width = 200
rect_height = 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()
