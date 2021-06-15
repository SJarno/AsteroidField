# importit
import pygame

class SimpleGame:
    def __init__(self):
        self._init_game()
        self.screen = pygame.display.set_mode((500, 500))

    def main_loop(self):
        while True:
            self._handle_input()
            # pelilogiikka
            self._draw()
        #pygame.quit()

    def _init_game(self):
        pygame.init()
        
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
    def _draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
        pygame.display.flip()


if __name__ == "__main__":
    peli = SimpleGame()
    peli.main_loop()
