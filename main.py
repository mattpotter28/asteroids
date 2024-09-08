import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10)
    asteroid_filed = AsteroidField()

    updatable.add(player)
    drawable.add(player)

    while True:
        dt = clock.tick(60) / 1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                return
            
        for obj in shots:
            for asteroid in asteroids:
                if obj.check_collision(asteroid):
                    obj.kill()
                    asteroid.split()

        pygame.display.flip()


if __name__ == "__main__":
    main()