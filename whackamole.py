import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_x = 0
        mole_y = 0

        running = True
        while running:
            screen.fill("pink")

            for x in range(0, 641, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 513, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_x = random.randrange(0, 640, 32)
                    mole_y = random.randrange(0, 512, 32)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()

