import pygame
import random



def start_game():
    # Window dimensions
    WIDTH = 480
    HEIGHT = 660
    FPS = 60

    # Define colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Initialize Pygame
    pygame.font.init()
    font = pygame.font.SysFont(None, 36)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            # Load the image for the player spaceship
            self.image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\ship6.png").convert()
            self.image.set_colorkey(WHITE)  # Set the background color to be transparent
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.score = 0




        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_a]:
                self.speedx = -5
            if keystate[pygame.K_d]:
                self.speedx = 5
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            self.score += 1

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            # Load the image for the enemy
            self.image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\Alien7_1.png").convert()
            self.image.set_colorkey(WHITE)  # Set the background color to be transparent
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            # Load the image for the bullet
            self.image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\alien_bullet1.png").convert()
             # Set the background color to be transparent
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()


    # this function is for the gamer over message at last
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

   # this function is for the gamer over message at last
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

# Load the space background image
    space_background = pygame.image.load("spacegame\\pictureandsounds\\Assets\\space2.png").convert()

    # Game loop
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(space_background, (0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()



        # Update sprites
        all_sprites.update()

        # Check for collisions with bullets and create new enemies
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Check for collisions with enemies and end the game if needed
        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            draw_text(screen, "GAME OVER", 64, WIDTH / 2, HEIGHT / 3)
            draw_text(screen, f"Score: {player.score - 1}", 36, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False

        # Rendering
        all_sprites.draw(screen)

        # Display score
        score_text = font.render(str(player.score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

    pygame.quit()

# If this file is run directly, start the game
if __name__ == "__main__":
    start_game()
