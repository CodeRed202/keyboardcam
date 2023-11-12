import pygame
from pygame.locals import *
pygame.init()

width = 200
height = 200

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("NoCamHandcam")

grey = (220,220,220)
red = (255,0,0)
black = (0,0,0)

color_w=grey
color_a=grey
color_s=grey
color_d=grey
color_shift=grey
color_space=grey

font = pygame.font.Font("termdos_extrabold.ttf",25)

run = True
while run:
    screen.fill((black))

    keys = pygame.key.get_pressed()
    if keys[K_w]: color_w = red
    else:color_w = grey
    if keys[K_a]: color_a = red
    else:color_a = grey
    if keys[K_s]: color_s = red
    else:color_s = grey
    if keys[K_d]: color_d = red
    else:color_d = grey
    if keys[K_LSHIFT]: color_shift = red
    else:color_shift = grey
    if keys[K_SPACE]: color_space = red
    else:color_space = grey

    w = pygame.draw.rect(screen,color_w, [50, 0, 50, 50])
    a = pygame.draw.rect(screen,color_a, [0, 50, 50, 50])
    s = pygame.draw.rect(screen,color_s, [50, 50, 50, 50])
    d = pygame.draw.rect(screen,color_d, [100, 50, 50, 50])
    shift = pygame.draw.rect(screen,color_shift, [0, 100, 100, 50])
    space = pygame.draw.rect(screen,color_space, [50, 150, 150, 50])

    w2 = font.render("W",True,black)
    w2rect = w2.get_rect()
    w2rect.centerx = w.centerx; w2rect.centery = w.centery
    screen.blit(w2,w2rect)

    a2 = font.render("A", True, black)
    a2rect = a2.get_rect()
    a2rect.centerx = a.centerx
    a2rect.centery = a.centery
    screen.blit(a2, a2rect)

    s2 = font.render("S", True, black)
    s2rect = s2.get_rect()
    s2rect.centerx = s.centerx
    s2rect.centery = s.centery
    screen.blit(s2, s2rect)

    d2 = font.render("D", True, black)
    d2rect = w2.get_rect()
    d2rect.centerx = d.centerx
    d2rect.centery = d.centery
    screen.blit(d2, d2rect)

    shift2 = font.render("SHIFT", True, black)
    shift2rect = shift2.get_rect()
    shift2rect.centerx = shift.centerx
    shift2rect.centery = shift.centery
    screen.blit(shift2, shift2rect)

    space2 = font.render("SPACE", True, black)
    space2rect = space2.get_rect()
    space2rect.centerx = space.centerx
    space2rect.centery = space.centery
    screen.blit(space2, space2rect)


    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
    pygame.display.flip()

pygame.quit()