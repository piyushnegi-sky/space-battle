# Import necessary libraries
import pygame
import sys
import multiplayer
import singleplayer

# Initialize Pygame
pygame.init()

# Set up screen dimensions, font, and frames per second
WIDTH, HEIGHT = 900, 500
FONT = pygame.font.Font(None, 36)
FPS = 60

# Define color constants
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (170, 170, 170)
BLACK = (0, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\_82cd00f3-7970-41c6-96e7-49426dd3ead3.jpeg")
gamename_image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\Screenshot 2023-12-17 190544.png")
gamemode_image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\game_modes.png")
difficulty_image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\difficulty.png")
settings_image = pygame.image.load("spacegame\\pictureandsounds\\Assets\\Screenshot 2023-12-18 004357.png")

# change the size of the image
background_image = pygame.transform.scale(background_image, (900, 500))
gamename_image = pygame.transform.scale(gamename_image, (350, 70))
settings_image = pygame.transform.scale(settings_image, (250,70))


# Load background music
pygame.mixer.music.load("spacegame\\pictureandsounds\\Assets\\battle_three.mp3")
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed
pygame.mixer.music.play(-1)  # -1 means play the music in an infinite loop


# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Function to show a popup message on the screen
def show_popup(message):
    popup_font = pygame.font.Font(None, 60)
    popup_text = popup_font.render(message, True, WHITE)
    popup_rect = popup_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(popup_text, popup_rect.topleft)
    pygame.display.update()
    pygame.time.delay(1000)

# Function representing the main game loop
def game():
    running = True
    while running:
        # Set the background image
        screen.blit(background_image, (0, 0))
        screen.blit(gamemode_image, (385, 60))


        # Get mouse position
        mx, my = pygame.mouse.get_pos()

        # Define buttons and their positions
        button_single_player = pygame.Rect(360, 150, 200, 50)
        button_multiplayer = pygame.Rect(360, 250, 200, 50)
        button_back = pygame.Rect(360, 350, 200, 50)

        # Render button texts
        button_single_player_text = FONT.render('Single Player', True, WHITE)
        button_multiplayer_text = FONT.render('Dual Player', True, WHITE)
        button_back_text = FONT.render('Back', True, WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_single_player.collidepoint((mx, my)):
                        singleplayer.start_game()
                    elif button_multiplayer.collidepoint((mx, my)):
                        multiplayer.main()
                    elif button_back.collidepoint((mx, my)):
                        main_menu()

        # Draw buttons on the screen
        pygame.draw.rect(screen, GRAY if button_single_player.collidepoint((mx, my)) else BLACK, button_single_player)
        pygame.draw.rect(screen, GRAY if button_multiplayer.collidepoint((mx, my)) else BLACK, button_multiplayer)
        pygame.draw.rect(screen, GRAY if button_back.collidepoint((mx, my)) else BLACK, button_back)

        # Draw button texts on the screen
        screen.blit(button_single_player_text, (button_single_player.x + 10, button_single_player.y + 10))
        screen.blit(button_multiplayer_text, (button_multiplayer.x + 10, button_multiplayer.y + 10))
        screen.blit(button_back_text, (button_multiplayer.x + 10, button_back.y + 10))

        # Update the display and set the frame rate
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


def difficulty_level():
    running = True
    while running:
        # Set the background image
        screen.blit(background_image, (0, 0))
        screen.blit(difficulty_image, (345, 20))


         # Get mouse position
        mx, my = pygame.mouse.get_pos()

        # Define buttons and their positions
        easy = pygame.Rect(320, 100, 200, 50)
        medium = pygame.Rect(320, 200, 200, 50)
        hard = pygame.Rect(320, 300, 200, 50)
        back = pygame.Rect(320, 400, 200, 50)

        #render buttons text
        button_easy_text = FONT.render('Easy', True, WHITE)
        button_medium_text = FONT.render('Medium', True, WHITE)
        button_hard_text = FONT.render('Hard', True, WHITE)
        button_back_text = FONT.render('Back', True, WHITE)

        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy.collidepoint((mx, my)):
                        show_popup("The game is set to Easy mode")
                        # Add your logic for Easy mode here
                    elif medium.collidepoint((mx, my)):
                        show_popup("The game is set to Medium mode")
                        # Add your logic for Medium mode here
                    elif hard.collidepoint((mx, my)):
                        show_popup("The game is set to Hard mode")
                        # Add your logic for Hard mode here
                    elif back.collidepoint((mx, my)):
                        main_menu()

        # draw buttons on screen
        pygame.draw.rect(screen, GRAY if easy.collidepoint((mx, my)) else BLACK, easy)
        pygame.draw.rect(screen, GRAY if medium.collidepoint((mx, my)) else BLACK, medium)
        pygame.draw.rect(screen, GRAY if hard.collidepoint((mx, my)) else BLACK, hard)
        pygame.draw.rect(screen, GRAY if back.collidepoint((mx, my)) else BLACK, back)

        # draw text on buttons
        screen.blit(button_easy_text, (easy.x + 10, easy.y + 10))
        screen.blit(button_medium_text, (medium.x + 10, medium.y + 10))
        screen.blit(button_hard_text, (hard.x + 10, hard.y + 10))
        screen.blit(button_back_text, (back.x + 10, back.y + 10))

        # Update the display and set the frame rate
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


def settings():
    running = True
    while running:

        # Set the background image
        screen.blit(background_image, (0, 0))
        screen.blit(settings_image, (325, 20))

        # Get mouse position
        mx, my = pygame.mouse.get_pos()

        # Define buttons and their positions
        button_sound = pygame.Rect(350, 100, 200, 50)
        button_music = pygame.Rect(350, 200, 200, 50)
        button_back = pygame.Rect(350, 300, 200, 50)

        # Render buttons text
        button_sound_text = FONT.render('Sound', True, WHITE)
        button_music_text = FONT.render('Music', True, WHITE)
        button_back_text = FONT.render('Back', True, WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_sound.collidepoint((mx, my)):
                        print("sound is off")
                    elif button_music.collidepoint((mx, my)):
                        # Stop the music when the music button is clicked
                        pygame.mixer.music.stop()
                    elif button_back.collidepoint((mx, my)):
                        main_menu()
                        # Exit the settings function

        # Draw buttons on screen
        pygame.draw.rect(screen, GRAY if button_sound.collidepoint((mx, my)) else BLACK, button_sound)
        pygame.draw.rect(screen, GRAY if button_music.collidepoint((mx, my)) else BLACK, button_music)
        pygame.draw.rect(screen, GRAY if button_back.collidepoint((mx, my)) else BLACK, button_back)

        # Draw text on buttons
        screen.blit(button_sound_text, (button_sound.x + 10, button_sound.y + 10))
        screen.blit(button_music_text, (button_music.x + 10, button_music.y + 10))
        screen.blit(button_back_text, (button_back.x + 10, button_back.y + 10))

        # Update the display and set the frame rate
        pygame.display.update()
        pygame.time.Clock().tick(FPS)



def main_menu():
    pygame.mixer.music.load("spacegame\\pictureandsounds\\Assets\\battle_three.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    current_screen = "main_menu"
    click = False  # Initialize click variable outside the loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if current_screen == "main_menu":
            # Set the background image
            screen.blit(background_image, (0, 0))
            screen.blit(gamename_image, (281, 10))


             # Get mouse position
            mx, my = pygame.mouse.get_pos()

            # Define buttons and their positions
            button_1 = pygame.Rect(360, 100, 200, 50)
            button_2 = pygame.Rect(360, 200, 200, 50)
            button_3 = pygame.Rect(360, 300, 200, 50)
            button_4 = pygame.Rect(360, 400, 200, 50)


            #render button text
            button_1_text = FONT.render('Play Game', True, WHITE)
            button_2_text = FONT.render('Difficulty Level', True, WHITE)
            button_3_text = FONT.render('Settings', True, WHITE)
            button_4_text = FONT.render('Quit', True, WHITE)


            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    difficulty_level()
            if button_3.collidepoint((mx, my)):
                if click:
                    settings()
            if button_4.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()


            #draw buttons on screen
            pygame.draw.rect(screen, GRAY if button_1.collidepoint((mx, my)) else BLACK, button_1)
            pygame.draw.rect(screen, GRAY if button_2.collidepoint((mx, my)) else BLACK, button_2)
            pygame.draw.rect(screen, GRAY if button_3.collidepoint((mx, my)) else BLACK, button_3)
            pygame.draw.rect(screen, GRAY if button_4.collidepoint((mx, my)) else BLACK, button_4)


            #draw text on button
            screen.blit(button_1_text, (button_1.x + 10, button_1.y + 10))
            screen.blit(button_2_text, (button_2.x + 10, button_2.y + 10))
            screen.blit(button_3_text, (button_3.x + 10, button_3.y + 10))
            screen.blit(button_4_text, (button_4.x + 10, button_4.y + 10))


        # Update the display and set the frame rate
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


# Set up initial state
music_on = False
sound_on = False

# Run the main menu
main_menu()
