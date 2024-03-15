import math
import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie1")
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BACKGROUND = BIALY
run = True
START = True
figura_surface = None
figura_3 = None
figura_5 = None
figura_6 = None
figura_7 = None
figura_8 = None
figura_9 = None


def rysuj(x, y, radius):
    angle = math.radians(360 / 15)
    vertices = []
    for i in range(15):
        xi = x + radius * math.cos(i * angle)
        yi = y - radius * math.sin(i * angle)
        vertices.append((int(xi), int(yi)))
    surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    pygame.draw.polygon(surface, CZARNY, vertices, 5)
    return surface


def rysuj_rownoleglobok(x, y, radius):
    angle = math.radians(360 / 15)
    vertices = []
    for i in range(15):
        xi = x + radius * math.cos(i * angle)
        yi = y - radius * math.sin(i * angle)
        vertices.append((int(xi), int(yi)))
    max_shift = 100
    max_distance = max(abs(vertex[0] - 600) for vertex in vertices)
    for i in range(len(vertices)):
        diff = 300 - vertices[i][1]
        shift = diff * (max_shift / 300) * (vertices[i][0] / max_distance)
        vertices[i] = (vertices[i][0] - shift, vertices[i][1])
    surface = pygame.Surface((600, 600), pygame.SRCALPHA)
    pygame.draw.polygon(surface, CZARNY, vertices, 5)
    return surface


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if START:
        win.fill(ZOLTY)
        figura_surface = rysuj(300, 300, 150)
        win.blit(figura_surface, (0, 0))
        START = False
    if keys[pygame.K_1]:
        win.fill(ZOLTY)
        figura_surface = rysuj(300, 300, 75)
        win.blit(figura_surface, (0, 0))
    elif keys[pygame.K_2]:
        win.fill(ZOLTY)
        figura_surface = pygame.transform.rotate(rysuj(300, 300, 150), -45)
        win.blit(figura_surface, (300 - figura_surface.get_width() // 2, 300 - figura_surface.get_height() // 2))
    elif keys[pygame.K_3]:
        win.fill(ZOLTY)
        figura_surface = pygame.transform.rotate(rysuj(300, 300, 150), 180)
        figura_3 = pygame.transform.flip(pygame.transform.scale(figura_surface, (figura_surface.get_width() // 2, figura_surface.get_height())), False, True)
        win.blit(figura_3, (300 - figura_3.get_width() // 2, 300 - figura_3.get_height() // 2))
    elif keys[pygame.K_4]:
        win.fill(ZOLTY)
        win.blit(rysuj_rownoleglobok(300, 300, 150), (0, 0))
    elif keys[pygame.K_5]:
        win.fill(ZOLTY)
        figura_surface = rysuj(300, 150, 150)
        figura_5 = pygame.transform.scale(figura_surface, (figura_surface.get_width(), figura_surface.get_height() // 2))
        win.blit(figura_5, (0, 0))
    elif keys[pygame.K_6]:
        win.fill(ZOLTY)
        figura_surface = rysuj_rownoleglobok(300, 300, 150)
        figura_6 = pygame.transform.rotate(figura_surface, -90)
        win.blit(figura_6, (0, 0))
    elif keys[pygame.K_7]:
        win.fill(ZOLTY)
        figura_surface = pygame.transform.rotate(rysuj(300, 300, 150), 180)
        figura_7 = pygame.transform.scale(figura_surface, (figura_surface.get_width() // 2, figura_surface.get_height()))
        win.blit(figura_7, (300 - figura_7.get_width() // 2, 300 - figura_7.get_height() // 2))
    elif keys[pygame.K_8]:
        win.fill(ZOLTY)
        figura_surface = pygame.transform.scale(rysuj(300, 300, 150), (rysuj(300, 300, 150).get_width() // 2, rysuj(300, 300, 150).get_height()))
        figura_8 = pygame.transform.rotate(figura_surface, 60)
        win.blit(figura_8, (300 - figura_8.get_width() // 2 - 80, 300 - figura_8.get_height() // 2 + 180))
    elif keys[pygame.K_9]:
        win.fill(ZOLTY)
        figura_surface = rysuj_rownoleglobok(300, 300, 150)
        figura_9 = pygame.transform.rotate(figura_surface, -180)
        win.blit(figura_9, (140, 0))
    elif keys[pygame.K_0]:
        win.fill(ZOLTY)
        figura_surface = rysuj(300, 300, 150)
        win.blit(figura_surface, (0, 0))
    pygame.display.update()
