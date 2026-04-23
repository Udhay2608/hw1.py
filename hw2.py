import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")

image = pygame.image.load("your_image.png")
image = pygame.transform.scale(image, (300, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((58, 58, 58))
    x = (500 - 300) // 2
    y = (500 - 300) // 2
    screen.blit(image, (x, y))

    pygame.display.update()

pygame.quit()
