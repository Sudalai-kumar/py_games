import pygame
import random
import math
def Retry(score_value,h_score,scores):
    #retry_button
    retry_img=pygame.image.load('retry-button.png')
    retryX=170
    retryY=330
    retry_width = retry_img.get_width()
    retry_height = retry_img.get_height()
    #score
    font=pygame.font.Font('freesansbold.ttf',32)
    scoreX=30
    scoreY=20
    h_scoreX=230
    h_scoreY=20
    def show_score(x,y):
            score = font.render("SCORE  " + str(score_value), True, (255, 255, 255))
            screen.blit(score, (x, y))
    def high_score(x,y):
        best_score = font.render("BEST  " + str(h_score), True, (255, 255, 255))
        screen.blit(best_score, (x, y))
    def  retry(x,y):
        screen.blit(retry_img,(x,y))

    # Game loop
    running = True
    while running:
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
    #Car1
    car1_img=pygame.image.load('car1.png')
    car1X=136
    car1Y=580
    car1X_change=0

    #Car2
    car2_img=pygame.image.load('car2.png')
    car2X=236
    car2Y=580
    car2X_change=0

    #targets
    b_target=[]
    r_target=[]
    target_speed=0.5
    n1=[]
    n2=[]
    lst=[1,2,3,4,5]
    b_targetX=[]#136
    b_targetY=[-100]
    b_targetY_change=[]
    r_targetX=[]#136
    r_targetY=[-100]
    r_targetY_change=[]                      
    #1st targets
    n1.append(random.choice(lst))
    if n1[0]%2==0:
        b_target.append(pygame.image.load('bcircle.png'))
        b_targetX.append(random.choice([136,34]))
        b_targetY_change.append(target_speed)
    else:
        b_target.append(pygame.image.load('bsquare.png'))
        b_targetX.append(random.choice([136,34]))
        b_targetY_change.append(target_speed)

    n2.append(random.choice(lst))
    if n2[0]%2==0:
        r_target.append(pygame.image.load('rcircle.png'))
        r_targetX.append(random.choice([236,336]))
        r_targetY_change.append(target_speed)
    else:
        r_target.append(pygame.image.load('rsquare.png'))
        r_targetX.append(random.choice([236,336]))
        r_targetY_change.append(target_speed)

    for j in range(1,150):
        n1.append(random.choice(lst))
        if n1[j]%2==0:
            b_target.append(pygame.image.load('bcircle.png'))
            b_targetY.append(random.randint(b_targetY[j-1]-230,b_targetY[j-1]-170))
            b_targetX.append(random.choice([136,34]))
            b_targetY_change.append(target_speed)
        else:
            b_target.append(pygame.image.load('bsquare.png'))
            b_targetY.append(random.randint(b_targetY[j-1]-230,b_targetY[j-1]-170))
            b_targetX.append(random.choice([136,34]))
            b_targetY_change.append(target_speed)
        
        n2.append(random.choice(lst))
        if n2[j]%2==0:
            r_target.append(pygame.image.load('rcircle.png'))
            r_targetY.append(random.randint(b_targetY[j-1]-230,b_targetY[j-1]-170))
            r_targetX.append(random.choice([236,336]))
            r_targetY_change.append(target_speed)
        else:
            r_target.append(pygame.image.load('rsquare.png'))
            r_targetY.append(random.randint(b_targetY[j-1]-230,b_targetY[j-1]-170))
            r_targetX.append(random.choice([236,336]))
            r_targetY_change.append(target_speed)
        
    #score
    
    score_value=0
    font=pygame.font.Font('freesansbold.ttf',32)
    textX=350
    textY=10
    def show_score(x,y):
            score = font.render("" + str(score_value), True, (255, 255, 255))
            screen.blit(score, (x, y))
        
    def  car1(x,y):
        screen.blit(car1_img,(x,y))
    def car2(x,y):
        screen.blit(car2_img,(x,y))

    def car1_target(x,y,i):
        screen.blit(b_target[i],(x,y))
    def car2_target(x,y,i):
        screen.blit(r_target[i],(x,y)) 

    def iscollision_1(car1X, car1Y, targetX, targetY):
        car_rect = car1_img.get_rect(topleft=(car1X, car1Y))
        target_rect = b_target[0].get_rect(topleft=(targetX, targetY))
        return car_rect.colliderect(target_rect)
    def iscollision_2(car2X, car2Y, targetX, targetY):
        car_rect = car2_img.get_rect(topleft=(car2X, car2Y))
        target_rect = r_target[0].get_rect(topleft=(targetX, targetY))
        return car_rect.colliderect(target_rect)

    # Game loop
    running = True
    game_over = False
    k_press1 = False
    k_press2 = False

    while running:
        screen.blit(background_img, (0, 0))
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # for car1
                if event.key == pygame.K_f and not k_press1:
                    car1X_change = -5
                    k_press1 = True
                elif event.key == pygame.K_f and k_press1:
                    car1X_change = 5
                    k_press1 = False
                # for car2
                if event.key == pygame.K_j and not k_press2:
                    car2X_change = 5
                    k_press2 = True
                elif event.key == pygame.K_j and k_press2:
                    car2X_change = -5
                    k_press2 = False

        if not game_over:
            # cars
            car1X += car1X_change
            if car1X < 34:
                car1X = 34
            elif car1X > 136:
                car1X = 136

            car2X += car2X_change
            if car2X < 236:
                car2X = 236
            elif car2X > 336:
                car2X = 336

            # targets
            for i in range(150):
                b_targetY[i] += b_targetY_change[i]
                r_targetY[i] += r_targetY_change[i]

                # Car 1 targets
                if n1[i] % 2 == 0:
                    car1_target(b_targetX[i], b_targetY[i], i)
                    collision1 = iscollision_1(car1X, car1Y, b_targetX[i], b_targetY[i])
                    if collision1:
                       
                        b_targetY[i]=1000
                        score_value += 1
                         # Check if the circle missed the car
                    elif b_targetY[i] > 670 and b_targetY[i] < 800:
                        pass
                        game_over = True
                else:
                    car1_target(b_targetX[i], b_targetY[i], i)
                    collision2 = iscollision_1(car1X, car1Y, b_targetX[i], b_targetY[i])
                    if collision2:
                        pass
                        game_over = True
                   

                # Car 2 targets
                if n2[i] % 2 == 0:
                    car2_target(r_targetX[i], r_targetY[i], i)
                    collision3 = iscollision_2(car2X, car2Y, r_targetX[i], r_targetY[i])
                    if collision3:
                        
                        r_targetY[i]=1000
                        score_value += 1
                         # Check if the circle missed the car
                    elif r_targetY[i] > 670 and r_targetY[i] < 800:
                        pass
                        game_over = True
                else:
                    car2_target(r_targetX[i], r_targetY[i], i)
                    collision4 = iscollision_2(car2X, car2Y, r_targetX[i], r_targetY[i])
                    if collision4:
                        pass
                        game_over = True
                   
            
            show_score(textX, textY)
            car1(car1X, car1Y)
            car2(car2X, car2Y)
            pygame.display.update()

        if game_over:
            scores.append(score_value)
            h_score=max(scores)
            Retry(score_value,h_score,scores)
        


#main
#initializeing pygame
pygame.init()
screen=pygame.display.set_mode((400,700))

#background image
background_img=pygame.image.load('road1.png')

#logo and caption
pygame.display.set_caption("Two Cars")
logo=pygame.image.load('logo.png')
pygame.display.set_icon(logo)
#play_button
play_img=pygame.image.load('play-button.png')
playX=170
playY=330
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
