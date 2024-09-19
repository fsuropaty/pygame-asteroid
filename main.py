import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(delta)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots: 
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        delta = clock.tick(60) / 1000


    # print("Starting asteroids!")
    # print("Screen width:", SCREEN_WIDTH)
    # print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()


