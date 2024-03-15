import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie2")
run = True


def rysuj():
    surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    pygame.draw.rect(surface, (255, 0, 0), (14, 300, 565, 10))
    return surface


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (100, 100, 400, 10))
    figura = pygame.transform.rotate(rysuj(), 45)
    win.blit(figura, (300 - figura.get_width() // 2, 300 - figura.get_height() // 2))
    pygame.draw.rect(win, (255, 0, 0), (100, 500, 400, 10))
    pygame.display.update()
