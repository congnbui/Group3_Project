import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# classes

class Balloon(pygame.sprite.Sprite):
    """ this class represents the baloons """

    def __init__(self):
        # Call the parent class (Sprite) constructor  (not get it??)
        super().__init__()

        self.image = pygame.Surface([20, 15])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
    def update(self):
        """ Release the balloons"""
        self.rect.y += self.speed

class Shooter(pygame.sprite.Sprite):
    """this class represents the player """

    def __init__(self):
        """set up the player on creation"""
        # Call the parent class (Sprite) constructor   ???? for what????
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 10

class Bullet(pygame.sprite.Sprite):
    """This class represents the bullets """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([10, 4])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x -= 6

# --- Create the window

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode([screen_width, screen_height])
myfont = pygame.font.SysFont("monospace", 16)
# --- Sprite lists

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()

# List of each balloons in the game
balloon_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# --- Create the sprites



# Create a red shooter
shooter = Shooter()
all_sprites_list.add(shooter)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0
ammo = 10
time_to_reload = 1000
reloading = False
lastReloadTime = time.clock()
times = 0
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing

    times += 1

    if times % 150 == 0:
        # This represents baloons:
        for i in range(2):
            balloon = Balloon()
            balloon.speed = 1

            # Set a random location for the balloon
            balloon.rect.x = random.randrange(400)
            balloon.rect.y = 10

            # Add the balloon to the list of objects
            balloon_list.add(balloon)
            all_sprites_list.add(balloon)




    # make shooter move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        shooter.rect.y -= 5
    elif keys[pygame.K_DOWN]:
        shooter.rect.y += 5

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # shoot the bullets
            if event.key == pygame.K_SPACE and not reloading and ammo > 0:
                ammo -= 1
                bullet = Bullet()
                bullet.rect.x = shooter.rect.x
                bullet.rect.y = shooter.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

            elif event.key == pygame.K_SPACE:
                lastReloadTime = time.clock()
                reloading = True
        # pygame.event.pump()
    if reloading and time.clock() - lastReloadTime > 1:  # 1000
        reloading = False
        ammo = 10
        print(time.clock() - lastReloadTime)
    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_list.update()

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a balloon
        balloon_hit_list = pygame.sprite.spritecollide(bullet, balloon_list, True)

        # For each balloon hit, remove the bullet and add to the score
        for balloon in balloon_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1



        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # --- Draw a frame

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites_list.draw(screen)
    scoretext = myfont.render("Score = " + str(score) +" /Ammo =" + str(ammo), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 20 frames per second
    clock.tick(60)

pygame.quit()