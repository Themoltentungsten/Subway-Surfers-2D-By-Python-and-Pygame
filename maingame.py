import pygame, random, time, os, sys
from pygame.locals import *
from mainimg import *

# Required constants
x = 0
y = 0
width = 800
height = 800
position = 365
bgcolour = (0,0,0)
coin_x = 0
coin_y = 0
coins_collected = 0
show_coin = False

# Setting up the game screen
screen = pygame.display.set_mode((width,height))

trains = [train1,train2,train3,train4,train5,train6,train7,train8]
random_train = random.choice(trains)
Blockers = [Blocker,Blocker1,Blocker2]
random_Blocker = random.choice(Blockers)
random_Blocker2 = random.choice(Blockers[0:2])

pygame.init()
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Subway Surfers by group 3")

# Defining some fonts
font = pygame.font.SysFont(None,40)
font1 = pygame.font.SysFont('monospace',30)
font2 = pygame.font.SysFont('monospace',25)
font3 = pygame.font.SysFont(None,70)
font4 = pygame.font.SysFont('monospace',40)

# Reading the stored high score from a file.
read=open("highscore.txt",'r')
topScore = float(read.readline())
read.close()

# Initializing music.
pygame.mixer.init()
swish = pygame.mixer.Sound("soundfiles/swish.ogg")
coin_sound = pygame.mixer.Sound("soundfiles/coin.wav")

def buttons(xpos,ypos,colour,text,width,height):
    pygame.draw.rect(screen,colour,(xpos,ypos,width,height))
    msg = font.render(text,1,(0,0,0))
    screen.blit(msg,(xpos+25,ypos+12))

def start():
    pygame.mixer.music.load("soundfiles/menumusic.mp3")
    pygame.mixer.music.play(-1)
    while(1):
        screen.blit(bgimage,(0,0))
        screen.blit(Subway_Surfers,(0,150))
        label = font.render("Press 'Enter' or click below to start.",1,(255,255,0))
        screen.blit(label,(130,470))
        buttons(270,530,(229,158,36),"LETS GO!!",200,60)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if(270 < mouse[0] < 470 and 530 < mouse[1] < 590):
            buttons(270,530,(220,160,220),"LETS GO!!",200,60)
            if click[0] == 1:
                return 1
        pygame.display.update()
        command = pygame.event.poll()
        if(command.type == pygame.KEYDOWN):
            if(command.key == pygame.K_RETURN):
                return 1
        if command.type == pygame.QUIT:
                pygame.quit()
                quit()

def gameover():
        while(1):
            screen.blit(bgimage,(0,0))
            screen.blit(Subway_Surfers,(0,150))
            label = font3.render("GAME OVER",1,(255,255,0))
            screen.blit(label,(250,380))
            label2 = font4.render("PLAY AGAIN ???",1,(255,165,0))
            screen.blit(label2,(230,450))
            final_coins = font2.render(f"Coins Collected: {coins_collected}",1,(255,255,0))
            screen.blit(final_coins,(280,420))
            buttons(250,500,(0,150,0),"YES",100,50)
            buttons(420,500,(150,0,0),"QUIT",100,50)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if(250 < mouse[0] < 350 and 500 < mouse[1] < 550):
                buttons(250,500,(220,160,220),"YES",100,50)
                if click[0] == 1:
                    return 1
            if(420 < mouse[0] < 520 and 500 < mouse[1] < 550):
                buttons(420,500,(220,160,220),"QUIT",100,50)
                if click[0] == 1:
                    pygame.quit()
                    quit()
            pygame.display.update()
            command = pygame.event.poll()
            if command.type == pygame.QUIT:
                    pygame.quit()
                    quit()

start()
# Loop to initialize variables and restart game loop.
while(1):
    a = 0
    b = 0
    FPS_change = 0
    FPS = 40
    score = 0
    coins_collected = 0
    show_coin = False
    running = 1
    pygame.mixer.music.load("soundfiles/bgmusic.mp3")
    pygame.mixer.music.play(-1)
    position = 365
    obstacle_strategy = random.randint(0,6)
    
    # Main game loop.
    while (running):
        w = 0
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        screen.fill(bgcolour)
        if event.type == pygame.KEYDOWN:
            # Assigning keys for player movement.
                if event.key == pygame.K_RIGHT:
                    if position == 615:
                        pygame.mixer.Sound.play(swish)
                        position = 115
                    else:
                        pygame.mixer.Sound.play(swish)
                        position = position + 250
                if event.key == pygame.K_LEFT:
                    if position == 115:
                        pygame.mixer.Sound.play(swish)
                        position = 615
                    else:
                        pygame.mixer.Sound.play(swish)
                        position = position - 250

        # CONTINUOUS SCROLLING OF Track AND Rail.
        rel_y = y%Track.get_rect().height
        screen.blit(Track,(200,rel_y - Track.get_rect().height))
        if(rel_y < height):
            screen.blit(Track, (200,rel_y))
        screen.blit(Rail,(10,rel_y - Rail.get_rect().height))
        if(rel_y < height):
            screen.blit(Rail, (10,rel_y))
        screen.blit(Rail,(515,rel_y - Rail.get_rect().height))
        if(rel_y < height):
            screen.blit(Rail, (515,rel_y))
        y += 10
        screen.blit(Jake,(position,500))

        # Coin Logic
        if not show_coin and random.randint(0, 100) < 2:  # 2% chance to spawn coin
            show_coin = True
            coin_x = random.choice([115, 365, 615])  # Random track position
            coin_y = -50  # Start above screen

        if show_coin:
            screen.blit(Coin, (coin_x, coin_y))
            coin_y += 10  # Move coin down
            
            # Check if player collected coin
            if position == coin_x and 450 < coin_y < 550:
                coins_collected += 1
                show_coin = False
                pygame.mixer.Sound.play(coin_sound)
            
            # Reset coin if it goes off screen
            if coin_y > 800:
                show_coin = False

        # COLLISION CHECKS:
        if(obstacle_strategy == 0):
            screen.blit(random_Blocker,(30,a-500))
            a += 10
            if(a > 1300):
                a = 0
                random_Blocker = random.choice(Blockers)
                obstacle_strategy = random.randint(0,6)
            if(position == 115 and a-500 == 200):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 1):
            screen.blit(random_train,(350,a-200))
            a += 15
            if(a > 900):
                a = 0
                random_train = random.choice(trains)
                obstacle_strategy = random.randint(0,6)
            if(position == 365 and a-200 >= 310 and a-200 <= 550):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 2):
            screen.blit(random_Blocker2,(550,a-500))
            a += 10
            if(a > 1300):
                a = 0
                random_Blocker2 = random.choice(Blockers[0:2])
                obstacle_strategy = random.randint(0,6)
            if(position == 615 and a-500 == 200):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 3):
            screen.blit(random_Blocker2,(550,a-500))
            screen.blit(random_Blocker,(30,a-500))
            a += 10
            if(a > 1300):
                chek = 1
                a = 0
                random_Blocker = random.choice(Blockers)
                random_Blocker2 = random.choice(Blockers[0:2])
                obstacle_strategy = random.randint(0,6)
            if((position == 615 and a-500 == 200) or (position == 115 and a-500 == 200)):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 4):
            screen.blit(random_train,(350,b-200))
            b += 15
            screen.blit(random_Blocker,(30,a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_Blocker = random.choice(Blockers)
                random_train = random.choice(trains)
                obstacle_strategy = random.randint(0,6)
            if((position == 365 and b-200 >= 310 and b-200 <= 550) or (position == 115 and a-500 == 200)):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 5):
            screen.blit(random_train,(350,b-200))
            b += 15
            screen.blit(random_Blocker2,(550,a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_Blocker2 = random.choice(Blockers[0:2])
                random_train = random.choice(trains)
                obstacle_strategy = random.randint(0,6)
            if((position == 365 and b-200 >= 310 and b-200 <= 550) or (position == 615 and a-500 == 200)):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        if(obstacle_strategy == 6):
            screen.blit(random_train,(350,b-200))
            b += 15
            screen.blit(random_Blocker,(30,a-500))
            screen.blit(random_Blocker2,(550,a-500))
            a += 10
            if(a > 1300 and b > 900):
                a = 0
                b = 0
                random_Blocker = random.choice(Blockers)
                random_Blocker2 = random.choice(Blockers[0:2])
                random_train = random.choice(trains)
                obstacle_strategy = random.randint(0,6)
            if((position == 365 and b-200 >= 310 and b-200 <= 550) or ((position == 115 or position == 615) and a-500 == 200)):
                pygame.mixer.music.load("soundfiles/accident.mp3")
                pygame.mixer.music.play(1)
                running = 0

        # SCORE AND COIN DISPLAY
        score += 0.1
        score_value = font.render("Score : "+str(score),1,(255,153,52))
        high_score = font.render("Top Score: "+str(topScore),1,(255,153,52))
        coin_text = font.render("Coins: " + str(coins_collected), 1, (255,215,0))
        screen.blit(score_value,(10,10))
        screen.blit(high_score,(10,40))
        screen.blit(coin_text,(10,70))

        pygame.display.update()
        FPS_change += 1
        if(FPS_change%200 == 0):
            FPS += 5
        CLOCK.tick(FPS)
        if score > topScore:
                Change=open("highscore.txt",'w')
                Change.write(str(score))
                Change.close()
                topScore = score
    gameover()