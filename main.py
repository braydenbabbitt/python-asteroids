import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt1000 = clock.tick(60)
        dt = dt1000 / 1000

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.kill()


if __name__ == "__main__":
    main()
