import pygame
import os
import random


class Settings(object):
    file_path = os.path.dirname(os.path.abspath(__file__))
    width = 700
    height = 400
    fps = 60       
    title = "Spieleprogrammierung - Marvin G." 
    images_path = os.path.join(file_path, "bitmaps")

    @staticmethod
    def get_dim():
        return (Settings.width, Settings.height)

class Game_Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "treeGreen_small.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.width // 2
        self.rect.bottom = Settings.height
        self.speed = 5
        self.lock_up = 0
        self.lock_down = 0
        self.lock_left = 0
        self.lock_right = 0

    def ranomize(self):
        self.rect.centerx = random.randrange(80, Settings.width-80)
        self.rect.centery = random.randrange(80, Settings.height-80)

    def update(self):
        keys = pygame.key.get_pressed()

        if self.rect.top <= Settings.height * 0:
            self.lock_up = 1
        else:
            self.lock_up = 0

        if self.rect.bottom >= Settings.height:
            self.lock_down = 1
        else:
            self.lock_down = 0

        if self.rect.left <= Settings.width * 0:
            self.lock_left = 1
        else:
            self.lock_left = 0

        if self.rect.right >= Settings.width:
            self.lock_right = 1
        else:
            self.lock_right = 0


        if keys[pygame.K_UP]:
            if self.lock_up == 0:
                self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.lock_down == 0:
                self.rect.y += self.speed


        if keys[pygame.K_LEFT]:
            if self.lock_left == 0:
                self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            if self.lock_right == 0:
                self.rect.x += self.speed


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(os.path.join(Settings.images_path, "jngl_bg.jpg")).convert_alpha()
        self.background = pygame.transform.scale(self.background, (Settings.width, Settings.height))
        self.background_rect = self.background.get_rect()
        self.movable_object = Game_Object()
        self.mov_group = pygame.sprite.Group()
        self.mov_group.add(self.movable_object)
        self.done = False
        
    
    def run(self):
        while not self.done:             # Hauptprogrammschleife mit Abbruchkriterium   
            self.clock.tick(Settings.fps)          # Setzt die Taktrate auf max 60fps   
            for event in pygame.event.get():    # Durchwandere alle aufgetretenen  Ereignisse
                if event.type == pygame.QUIT:   # Wenn das rechts obere X im Fenster geklicktr
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.movable_object.ranomize()

            self.screen.blit(self.background, self.background_rect)
            self.mov_group.draw(self.screen)
            self.mov_group.update()

        

            pygame.display.flip()

game = Game()
if __name__ == '__main__':
                                    
    pygame.init()               # Bereitet die Module zur Verwendung vor
    pygame.mixer.init()
    game.run()
  
    pygame.quit()               # beendet pygame
