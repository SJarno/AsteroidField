import pygame
from random import randint

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_size: tuple):
        super(Spaceship, self).__init__()
        self.surf = pygame.image.load("assets/images/airship2.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.SCREEN_WIDTH = screen_size[0]
        self.SCREEN_HEIGTH = screen_size[1]
        self.move_up_sound = pygame.mixer.Sound("assets/sound/Rising_putter.ogg")
        self.move_down_sound = pygame.mixer.Sound("assets/sound/Falling_putter.ogg")
        self.collision_sound = pygame.mixer.Sound("assets/sound/Collision.ogg")

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # pidetään ruudussa:
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.SCREEN_HEIGTH:
            self.rect.bottom = self.SCREEN_HEIGTH

class CollisionAsteroid(pygame.sprite.Sprite):
    def __init__(self, screen_size: tuple):
        super(CollisionAsteroid, self).__init__()
        self.surf = pygame.image.load("assets/images/asteroid_fast.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.SCREEN_WIDTH = screen_size[0]
        self.SCREEN_HEIGTH = screen_size[1]
        # luo sattumanvaraiseen paikkaan:
        self.rect = self.surf.get_rect(
            center=(
                randint(self.SCREEN_WIDTH + 20, self.SCREEN_WIDTH + 100),
                randint(0, self.SCREEN_HEIGTH),
            )
        )
        self.speed = randint(5, 20)

    # liikuttaminen ja poistaminen:
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill() # metodi poistaa joukosta!



class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_size: tuple):
        super(Asteroid, self).__init__()
        self.surf = self._load_image()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.SCREEN_WIDTH = screen_size[0]
        self.SCREEN_HEIGTH = screen_size[1]
        self.rect = self.surf.get_rect(
            center=(
                randint(self.SCREEN_WIDTH + 20, self.SCREEN_WIDTH + 100),
                randint(0, self.SCREEN_HEIGTH),
            )
        )
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill() # removes from group

    def _load_image(self):
        images = {
            1: "assets/images/asteroid_small.png",
            2: "assets/images/asteroid_medium.png",
            3: "assets/images/asteroid_big.png"
        }
        return pygame.image.load(images.get(randint(1, 3))).convert()

if __name__ == "__main__":
    print(randint(1, 3))