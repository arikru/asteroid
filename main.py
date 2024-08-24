import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    asteroidfield = AsteroidField()
    player = Player(x, y, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for member in updateable:
            member.update(dt)
        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("GAME OVER!")
                return
            for shot in shots:
                if shot.checkCollision(asteroid):
                    shot.kill()
                    asteroid.split()

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
