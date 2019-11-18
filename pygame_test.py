import pygame

pygame.init()
pygame.display.set_caption('interation_projection')
screen = pygame.display.set_mode((1000, 800))
running = True
image = pygame.image.load('images/yezi.png')
image_rect = image.get_rect()
image_rect.x = 100
image_rect.y = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)
    pygame.display.flip()
    image_rect.y += 10

