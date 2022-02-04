import pygame
import time
from pygame.locals import *
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self,*kwargs):
        super(Player,self).__init__(*kwargs)
        # self.surf = pygame.Surface((10,10))
        # self.surf.fill((0,0,255))
        self.surf = pygame.image.load('bird.png')
        # self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(topleft = (2*15+2,6*15+2))
    def update(self,pressedKey):
        if pressedKey[K_a] or pressedKey[K_LEFT]:
            self.rect.move_ip(-15,0)
        elif pressedKey[K_d] or pressedKey[K_RIGHT]:
            self.rect.move_ip(15,0)
        elif pressedKey[K_w] or pressedKey[K_UP]:
            self.rect.move_ip(0,-15)
        elif pressedKey[K_s] or pressedKey[K_DOWN]:
            self.rect.move_ip(0,15)
        
        # collision detection
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if pressedKey[K_a] or pressedKey[K_LEFT]:
                    self.rect.x += 15
                    self.rect.y += 0
                    # self.rect = self.surf.get_rect().move(20,100)
                    # self.rect.move_ip(-15,0)
                elif pressedKey[K_d] or pressedKey[K_RIGHT]:
                    self.rect.move_ip(-15,0)
                elif pressedKey[K_w] or pressedKey[K_UP]:
                    self.rect.move_ip(0,15)
                elif pressedKey[K_s] or pressedKey[K_DOWN]:
                    self.rect.move_ip(0,-15)
        
class Board():
    def __init__(self):
        self.layout = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                        [1,1,1,0,1,1,1,0,0,0,1,0,0,0,1],
                        [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
                        [1,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
                        [1,0,1,1,1,0,0,0,1,0,1,1,1,0,1],
                        [1,0,0,0,1,0,1,0,1,1,1,0,0,0,1],
                        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Wall(object):
    def __init__(self,pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0],pos[1],15,15)

class Target():
    def __init__(self):
        # self.rect = pygame.Rect(9*15+2,5*15,10,10)
        self.surf = pygame.image.load('birdnest1.png')
        # self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(topleft = (9*15,5*15))
       
def message(msg,color,screen):
    fontStyle = pygame.font.SysFont(None,30,bold=1,italic=1)
    msg =fontStyle.render(msg,True,color)
    screen.blit(msg,(40,40))

player = Player()
board = Board()
target = Target()
walls =[]

# sending walls position to Wall class
posX = posY = 0
for row in board.layout:
        for column in row:
            if column == 1:
                Wall((posX,posY))
                # pygame.draw.rect(screen,brown,(posX,posY,15,15))
            posX += 15
        posX = 0
        posY += 15

def gameLoop():
    width = 225
    height = 135
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Resolve Me")
    brown =(100,20,20)
    clock = pygame.time.Clock()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
          
        screen.fill((0,255,255))

        for wall in walls:
            pygame.draw.rect(screen,brown,wall.rect)
       
        screen.blit(player.surf,player.rect)
        # pygame.draw.rect(screen,(0,0,255),player.rect)
        screen.blit(target.surf,target.rect)
        # pygame.draw.rect(screen,(255,0,0),target.rect)
        
        pressedKey = pygame.key.get_pressed()
        player.update(pressedKey)
        
        # end of game when the target reached
        if player.rect.colliderect(target.rect):
            message("Game Over",(255,155,50),screen)  
            running = False
        
        pygame.display.update()
        clock.tick(10)

gameLoop()
time.sleep(1)
pygame.quit()
quit()