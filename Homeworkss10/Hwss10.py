import pygame

from object.game import Game
from object.map import Map
from object.pusher import Pusher
from object.box import Box
from object.dest import Dest

#object = Class()
sokoban = Game()
sokoban.map = Map(5, 5)
sokoban.pusher = Pusher(1, 1)
sokoban.box = Box(2, 2)
sokoban.dest = Dest(3, 3)

# sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
box_image = pygame.image.load("images/box.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
youwin_image = pygame.image.load("images/youwin2.png")
youwin_image = pygame.transform.scale(youwin_image, (100, 100))
restart_image = pygame.image.load("images/restart.jpg")
restart_image = pygame.transform.scale(restart_image, (128, 64))
sokoban.box.image = box_image
sokoban.dest.image = dest_image
sokoban.pusher.image = pusher_image

pixel = 64

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if sokoban.map.width * pixel <= x <= sokoban.map.width * pixel + restart_image.get_size()[0] and 0 <= y <= restart_image.get_size()[1]:
                sokoban.map = Map(5, 5)
                sokoban.pusher = Pusher(1, 1)
                sokoban.box = Box(2, 2)
                sokoban.dest = Dest(3, 3)
                sokoban.box.image = box_image
                sokoban.dest.image = dest_image
                sokoban.pusher.image = pusher_image

        sokoban.handle_input(event)

    sokoban.draw(screen, ground_image, restart_image)
    if sokoban.box.check_win(sokoban.dest):
        screen.blit(youwin_image,(120, 120))
        # pygame.display.flip()
        # pygame.time.wait(3000)
        # done = True


    pygame.display.flip()
