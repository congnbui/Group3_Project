import pygame
# from object.map import Map
# from object.pusher import Pusher
# from object.box import Box
# from object.dest import Dest
class Game:
    def __init__(self):
        pass
    # def console_draw(self):
    #     #draw in console
    #     for y in range(self.map.height):
    #         for x in range(self.map.width):
    #             if y == self.dest.y and x == self.dest.x:
    #                 print(" D ", end = "")
    #             elif y == self.box.y and x == self.box.x:
    #                 print(" B ", end = "")
    #             elif y == self.pusher.y and x == self.pusher.x:
    #                 print(" P ", end = "")
    #             else:
    #                 print(" - ", end = "")
    #         print()

    def draw_image_center(self, object, screen):
        pixel = 64
        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height()) / 2 + object.y * pixel
        screen.blit(object.image, (w, h))

    def draw(self, screen, ground_image, restart_image):
        #draw in pygame
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))


        # screen.blit(pusher_image, (self.pusher.x * pixel, self.pusher.y * pixel))
        # screen.blit(box_image, (self.box.x * pixel, self.box.y * pixel))
        # screen.blit(dest_image, (self.dest.x * pixel, self.dest.y * pixel))
        self.draw_image_center(self.pusher, screen)
        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.dest, screen)
        screen.blit(restart_image, (self.map.width * pixel, 1))

    def in_map(self, object, dx, dy):
        if 0 <= object.x + dx < self.map.width and 0 <= object.y + dy < self.map.height:
            return True
        return False

    def handle_input(self, event): # including move
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
        if self.pusher.collide(self.box, dx, dy):
            if self.in_map(self.box, dx, dy):
                self.pusher.move(dx, dy)
                self.box.move(dx, dy)
        else:
            if self.in_map(self.pusher, dx, dy):
                self.pusher.move(dx, dy)
    # def restart(self):
    #     self.map = Map(5, 5)
    #     self.pusher = Pusher(1, 1)
    #     self.box = Box(2, 2)
    #     self.dest = Dest(3, 3)
    #     pygame.init()
    #     screen = pygame.display.set_mode((640, 640))
    #     done = False
    #     box_image = pygame.image.load("images/box.png")
    #     pusher_image = pygame.image.load("images/pusher.png")
    #     ground_image = pygame.image.load("images/ground.png")
    #     dest_image = pygame.image.load("images/dest.png")
    #     youwin_image = pygame.image.load("images/youwin2.png")
    #     youwin_image = pygame.transform.scale(youwin_image, (100, 100))
    #     restart_image = pygame.image.load("images/restart.jpg")
    #     restart_image = pygame.transform.scale(restart_image, (128, 64))
    #     sokoban.box.image = box_image
    #     sokoban.dest.image = dest_image
    #     sokoban.pusher.image = pusher_image