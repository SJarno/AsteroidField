import pygame
from models import Spaceship, Asteroid, CollisionAsteroid

# background nebula image: http://www.godsandidols.com/
# music: under creative commons 0


class AsteroidField:
    # Global screen size
    SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    def __init__(self):
        self._init_game()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background = pygame.image.load("assets/images/nebula1.jpg").convert()
        # Custom events:
        self.ADDCOLL = pygame.USEREVENT + 1
        self.ADDAST = pygame.USEREVENT + 2
        # Creating player:
        self._player = Spaceship(self.SIZE)
        # sprite groups:
        self._colliding_asteroids = pygame.sprite.Group() 
        self._asteroids = pygame.sprite.Group()
        self._all_sprites = pygame.sprite.Group() # for rendering
        self._all_sprites.add(self._player)
        # frames:
        self.clock = pygame.time.Clock()
        # music and sounds:
        self.collision_sound = pygame.mixer.Sound("assets/sound/Collision.ogg")
        self.soundtrack = pygame.mixer.music.load("assets/sound/370801__romariogrande__space-chase.wav")

        

    def main_loop(self):
        pygame.time.set_timer(self.ADDCOLL, 250)
        pygame.time.set_timer(self.ADDAST, 2000)
        pygame.mixer.music.play(loops=-1)
        self.collision_sound.set_volume(1.0)

        while True:
            self._handle_input()
            self._handle_game_logic()
            self._draw()
        pygame.mixer.quit()

    def _init_game(self):
        pygame.mixer.init()
        pygame.init()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                exit()
            elif event.type == self.ADDCOLL:
                col_asteroid = CollisionAsteroid(self.SIZE)
                self._colliding_asteroids.add(col_asteroid)
                self._all_sprites.add(col_asteroid)
            elif event.type == self.ADDAST:
                asteroid = Asteroid(self.SIZE)
                self._asteroids.add(asteroid)
                self._all_sprites.add(asteroid)

        # check for pressed keys and handle them
        pressed_keys = pygame.key.get_pressed()
        self._player.update(pressed_keys)
        self._colliding_asteroids.update()
        self._asteroids.update()


    def _handle_game_logic(self):
        # logic for collision and game over
        if pygame.sprite.spritecollideany(self._player, self._colliding_asteroids):
            self._player.kill()
            pygame.mixer.music.stop()
            pygame.time.delay(50)
            self.collision_sound.play()
            pygame.time.delay(500)
            exit()

    def _draw(self):

        self.screen.blit(self.background, (0, 0))

        # render sprites
        for entity in self._all_sprites:
            self.screen.blit(entity.surf, entity.rect)

        pygame.display.flip() # update everything
        self.clock.tick(30)

if __name__ == "__main__":
    peli = AsteroidField()
    peli.main_loop()