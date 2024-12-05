import pygame
import random
def Retry(score,h_score,scores):
    #initializeing pygame
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    #background image
    background_img=pygame.image.load('background.png')

    #logo and caption
    pygame.display.set_caption("Word Falling Game")
    logo=pygame.image.load('icon.png')
    pygame.display.set_icon(logo)
    #retry_button
    retry_img=pygame.image.load('reload.png')
    retryX=360
    retryY=270
    retry_width = retry_img.get_width()
    retry_height = retry_img.get_height()
    #score
    font=pygame.font.Font('freesansbold.ttf',32)
    scoreX=250
    scoreY=20
    h_scoreX=450
    h_scoreY=20
    def show_score(x,y):
            score_value = font.render("SCORE  " + str(score), True, (255, 255, 255))
            screen.blit(score_value, (x, y))
    def high_score(x,y):
        best_score = font.render("BEST  " + str(h_score), True, (255, 255, 255))
        screen.blit(best_score, (x, y))
    def  retry(x,y):
        screen.blit(retry_img,(x,y))

    # Game loop
    running = True
    while running:
        screen.blit(background_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    retry_button_rect = pygame.Rect(300, 350, retry_width, retry_height)
                    if retry_button_rect.collidepoint(mouse_x, mouse_y):
                        game(scores)
                        running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    game(scores)
                    running=False

        retry(retryX,retryY)
        show_score(scoreX,scoreY)
        high_score(h_scoreX,h_scoreY)
        pygame.display.update()

    # Quit pygame
    pygame.quit()
    
def game(scores):
    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Fonts
    font_size = 36  # Initial font size
    font = pygame.font.Font(None, font_size)
    #initializeing pygame
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    #background image
    background_img=pygame.image.load('background.png')

    #logo and caption
    pygame.display.set_caption("Word Falling Game")
    logo=pygame.image.load('icon.png')
    pygame.display.set_icon(logo)
    # Game variables
    score = 0
    life = 5
    falling_speed = 0.5  # Initial speed
    speed_increase_interval = 10  # Score interval for speed increase
    speed_increase_amount = 0.5  # Amount to increase speed
    computer_science_words = [
        'mail', 'engine', 'version', 'update', 'hosting', 'web', 'buttons', 'upload', 'ethernet', 'devices',
        'suite', 'linux', 'microsoft', 'ram', 'authentication', 'development', 'server', 'machine', 'cd', 'macos',
        'backup', 'service', 'creative', 'processor', 'attack', 'virtual', 'networks', 'ruby', 'terminal', 'lan',
        'python', 'joystick', 'rack', 'bluetooth', 'cpu', 'programming', 'memory', 'mechanical', 'search', 'software',
        'interpreter', 'viruses', 'code', 'wan', 'scanner', 'interface', 'network', 'android', 'modem', 'sound', 'user',
        'folder', 'css', 'download', 'mousepad', 'computer', 'device', 'adsl', 'app', 'computing', 'address', 'megabyte',
        'pixel', 'kilobytes', 'usb', 'windows', 'cli', 'learning', 'java', 'hacking', 'algorithm', 'input', 'firewall',
        'office', 'filter', 'client', 'usb port', 'developer', 'storage', 'microphone', 'artificial', 'ip', 'bug',
        'resolution', 'multitasking', 'cybersecurity', 'javascript', 'gigabytes', 'html', 'cache', 'sql', 'cable',
        'analysis', 'firmware', 'center', 'domain', 'malware', 'file', 'monitor', 'adobe', 'disk', 'encryption',
        'database', 'flash', 'components', 'drive', 'biometric', 'pc', 'electronic', 'experience', 'mouse', 'api',
        'reality', 'floppy', 'antivirus', 'router', 'malicious', 'intelligence', 'boot', 'provider', 'debugger', 'iot',
        'cyber', 'biometrics', 'power', 'printers', 'spreadsheet', 'spam', 'language', 'virus', 'control', 'ios', 'vpn',
        'output', 'card', 'gpu', 'spyware', 'ram', 'peripheral', 'robotics', 'debugging', 'bytes', 'word', 'operating',
        'email', 'motherboard', 'internet', 'audio', 'gaming', 'data', 'troubleshooting', 'hardware', 'compiler',
        'presentation', 'website', 'console', 'graphics', 'scanners', 'browser', 'system', 'webcam', 'recovery', 'deep',
        'keyboard', 'cloud', 'augmented'
    ]

    falling_word = ""
    falling_word_x = random.randint(0, 800 - len("git") * font_size)  # Initial x-position for falling word
    falling_word_y = 0  # Initial y-position for falling word

    # Red line position
    red_line_y = 600 - 50

    # Main game loop
    running = True
    words = []
    def generate_new_falling_word():
        word = random.choice(computer_science_words)
        words.append(word)
        return word

    falling_word = generate_new_falling_word()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in range(97, 123) or (event.key in range(65, 91) and pygame.key.get_mods() & pygame.KMOD_SHIFT):  
                    # Check if the key pressed is a lowercase letter or uppercase letter with SHIFT
                    entered_letter = chr(event.key)
                    if entered_letter.lower() in falling_word.lower():
                        # Remove the entered letter from the falling word
                        falling_word = falling_word.replace(entered_letter, "", 1)

        # Update falling word and speed
        falling_word_y += falling_speed

        # Check if the word has passed the red line
        if falling_word_y > red_line_y:
            life -= 1
            falling_word = generate_new_falling_word()
            falling_word_x = random.randint(0, 800 - len(falling_word) * font_size)  # Reset x-position
            falling_word_y = 0  # Reset y-position

        # Check if the word is fully entered
        if not falling_word:
            score += 1
            computer_science_words.remove(words.pop())
            falling_word = generate_new_falling_word()
            falling_word_x = random.randint(0, 800 - len(falling_word) * font_size)  # Reset x-position
            falling_word_y = 0  # Reset y-position

            # Increase speed based on score
            if score % speed_increase_interval == 0:
                falling_speed += speed_increase_amount

        # Draw background
        screen.blit(background_img, (0, 0))

        # Draw red line
        pygame.draw.line(screen, RED, (0, red_line_y), (800, red_line_y), 2)

        # Draw falling word
        text = font.render(falling_word, True, WHITE)
        screen.blit(text, (int(falling_word_x), int(falling_word_y)))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw life
        life_text = font.render(f"Lifes: {life}", True, WHITE)
        screen.blit(life_text, (520, 10))
        
        # Check if the score is less than 0 to end the game
        if life <= 0:
            scores.append(score)
            h_score=max(scores)
            Retry(score,h_score,scores)
            running = False

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

#main
    
#initializeing pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

#background image
background_img=pygame.image.load('background.png')

#logo and caption
pygame.display.set_caption("Word Falling Game")
logo=pygame.image.load('icon.png')
pygame.display.set_icon(logo)
#play_button
play_img=pygame.image.load('play.png')
playX=360
playY=270
play_width = play_img.get_width()
play_height = play_img.get_height()

#score
scores=[]
def  play(x,y):
    screen.blit(play_img,(x,y))

# Game loop
running = True
while running:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_button_rect = pygame.Rect(300, 350, play_width, play_height)
            if play_button_rect.collidepoint(mouse_x, mouse_y):
                game(scores)
                running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game(scores)
                running=False

    play(playX,playY)
    pygame.display.update()

# Quit pygame
pygame.quit()
