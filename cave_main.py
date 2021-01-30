import pygame
import sys
import random

#pygame.font.init()
#pygame.mixer.init()
#pygame.mixer.music.load('RUDE - Eternal Youth.ogg')
#pygame.mixer.music.play(-1)

class Player():
    def __init__(self,x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

class Obstacle():
    def __init__(self, w_screen, h_screen, color):
        self.x = (9 * w_screen) // 10
        self.w = 20#random.randint(10, w_screen // 20)
        self.h = random.randint(10, 3 * h_screen // 4)
        self.gap = pl.r * 4#random.randint(min(w_screen, h_screen) // 15 * 4, min(w_screen, h_screen) // 15 * 10)
        self.color = color

def Move_right(frame):
    if frame % 60 <= 6 :
        plr1_rect = plr1_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr1_surf, plr1_rect)

    elif frame % 60 >= 6 and frame % 60 <= 12:
        plr2_rect = plr2_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr2_surf, plr2_rect)

    elif frame % 60 >= 12 and frame % 60 <= 18:
        plr3_rect = plr3_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr3_surf, plr3_rect)

    elif frame % 60 >= 18 and frame % 60 <= 24:
        plr4_rect = plr4_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr4_surf, plr4_rect)

    elif frame % 60 >= 24 and frame % 60 <= 30:
        plr5_rect = plr5_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr5_surf, plr5_rect)

    elif frame % 60 >= 30 and frame % 60 <= 36:
        plr6_rect = plr6_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr6_surf, plr6_rect)
        
    elif frame % 60 >= 36 and frame % 60 <= 42:
        plr7_rect = plr7_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr7_surf, plr7_rect)
        
    elif frame % 60 >= 42 and frame % 60 <= 48:
        plr8_rect = plr8_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr8_surf, plr8_rect)
        
    elif frame % 60 >= 48 and frame % 60 <= 54:
        plr9_rect = plr9_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr9_surf, plr9_rect)
        
    elif frame % 60 >= 54 and frame % 60 <= 60:
        plr10_rect = plr10_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr10_surf, plr10_rect)
    
def Move_left(frames):
    #i = frame % 60 // 6
    #sc.blit( plr_rects[i][1], plr_rects[i][0])
    if frame % 60 <= 6 :
        plL1_rect = plL1_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL1_surf, plL1_rect)

    elif frame % 60 >= 6 and frame % 60 <= 12:
        plL2_rect = plL2_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL2_surf, plL2_rect)

    elif frame % 60 >= 12 and frame % 60 <= 18:
        plL3_rect = plL3_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL3_surf, plL3_rect)

    elif frame % 60 >= 18 and frame % 60 <= 24:
        plL4_rect = plL4_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL4_surf, plL4_rect)

    elif frame % 60 >= 24 and frame % 60 <= 30:
        plL5_rect = plL5_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL5_surf, plL5_rect)

    elif frame % 60 >= 30 and frame % 60 <= 36:
        plL6_rect = plL6_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL6_surf, plL6_rect)
        
    elif frame % 60 >= 36 and frame % 60 <= 42:
        plL7_rect = plL7_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL7_surf, plL7_rect)
        
    elif frame % 60 >= 42 and frame % 60 <= 48:
        plL8_rect = plL8_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL8_surf, plL8_rect)
        
    elif frame % 60 >= 48 and frame % 60 <= 54:
        plL9_rect = plL9_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL9_surf, plL9_rect)
        
    elif frame % 60 >= 54 and frame % 60 <= 60:
        plL10_rect = plL10_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL10_surf, plL10_rect)



FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

vx = 0

frame = 0

width = 1024
height = 576

pygame.init()
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


fon_surf = pygame.image.load('podzemele-demo-1024x576.png')

bridge_surf = pygame.image.load('bridge.png')
bridge_surf.set_colorkey((255, 255, 255))



plr1_surf = pygame.image.load('move/move_r1.png')
plr1_surf.set_colorkey((255, 255, 255))

plr2_surf = pygame.image.load('move/move_r2.png')
plr2_surf.set_colorkey((255, 255, 255))

plr3_surf = pygame.image.load('move/move_r3.png')
plr3_surf.set_colorkey((255, 255, 255))

plr4_surf = pygame.image.load('move/move_r4.png')
plr4_surf.set_colorkey((255, 255, 255))

plr5_surf = pygame.image.load('move/move_r5.png')
plr5_surf.set_colorkey((255, 255, 255))

plr6_surf = pygame.image.load('move/move_r6.png')
plr6_surf.set_colorkey((255, 255, 255))

plr7_surf = pygame.image.load('move/move_r7.png')
plr7_surf.set_colorkey((255, 255, 255))

plr8_surf = pygame.image.load('move/move_r8.png')
plr8_surf.set_colorkey((255, 255, 255))

plr9_surf = pygame.image.load('move/move_r9.png')
plr9_surf.set_colorkey((255, 255, 255))

plr10_surf = pygame.image.load('move/move_r10.png')
plr10_surf.set_colorkey((255, 255, 255))


plL1_surf = pygame.image.load('move/move_L1.png')
plL1_surf.set_colorkey((255, 255, 255))

plL2_surf = pygame.image.load('move/move_L2.png')
plL2_surf.set_colorkey((255, 255, 255))

plL3_surf = pygame.image.load('move/move_L3.png')
plL3_surf.set_colorkey((255, 255, 255))

plL4_surf = pygame.image.load('move/move_L4.png')
plL4_surf.set_colorkey((255, 255, 255))

plL5_surf = pygame.image.load('move/move_L5.png')
plL5_surf.set_colorkey((255, 255, 255))

plL6_surf = pygame.image.load('move/move_L6.png')
plL6_surf.set_colorkey((255, 255, 255))

plL7_surf = pygame.image.load('move/move_L7.png')
plL7_surf.set_colorkey((255, 255, 255))

plL8_surf = pygame.image.load('move/move_L8.png')
plL8_surf.set_colorkey((255, 255, 255))

plL9_surf = pygame.image.load('move/move_L9.png')
plL9_surf.set_colorkey((255, 255, 255))

plL10_surf = pygame.image.load('move/move_L10.png')
plL10_surf.set_colorkey((255, 255, 255))

#plr_rects = [(plr1_surf.get_rect(bottomleft=(pl.x, pl.y + 59)), plr1_surf), 
#             (plr2_surf.get_rect(bottomleft=(pl.x, pl.y + 59)), plr2_surf),]


pl = Player(width / 2, height - 122, 22, 59, WHITE)
#сделать разные препятствия и проработать хитбоксы(пересечения)
vd = 'right'
pygame.display.update()

# главный цикл
while True:
    
    # задержка
    clock.tick(FPS)
    frame += 1
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            print(i)
            if i.key == 1073741904:#влево
                vx = -5#5
                vd = 'left'
            elif i.key == 1073741903:#вправо
                vx = 5#-5
                vd = 'right'
        if i.type == pygame.KEYUP:
            if i.key == 1073741904 or i.key == 1073741903:
                vx = 0
    pl.x += vx
    # --------
    # изменение объектов
    # --------
    fon_rect = fon_surf.get_rect(
    bottomright=(width, height))
    sc.blit(fon_surf, fon_rect)

    bridge_rect = bridge_surf.get_rect(
    bottomright=(width, height))
    sc.blit(bridge_surf, bridge_rect)
    #pygame.draw.rect(sc, pl.color, (pl.x, pl.y, pl.w, pl.h))
    if vx < 0:
        Move_left(frame)
        
    elif vx > 0:
        Move_right(frame)
        
    elif vx == 0 and vd == 'right':
        plr1_rect = plr1_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plr1_surf, plr1_rect)
        sc.blit(plr1_surf, plr1_rect)
        
    elif vx == 0 and vd == 'left':
        plL1_rect = plL1_surf.get_rect(
        bottomleft=(pl.x, pl.y + 59))
        sc.blit(plL1_surf, plL1_rect)
        sc.blit(plL1_surf, plL1_rect)    


        
    # обновление экрана
    pygame.display.update()
