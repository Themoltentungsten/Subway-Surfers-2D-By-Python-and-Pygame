# maingame.py  (web-ready for pygbag)
import pygame, random, asyncio, os, sys
from pygame.locals import *
from mainimg import *

width, height = 800, 800
bgcolour = (0, 0, 0)

position = 365
y = 0
coins_collected = 0
show_coin = False
coin_x = 0
coin_y = 0

screen = None
CLOCK = None

def is_web():
    return sys.platform == "emscripten"

def hs_path():
    return "/data/highscore.txt" if is_web() else "highscore.txt"

def load_top_score():
    try:
        with open(hs_path(), "r") as f:
            s = f.read().strip()
            return float(s) if s else 0.0
    except Exception:
        return 0.0

def save_top_score(score: float):
    try:
        if is_web():
            os.makedirs("/data", exist_ok=True)
        with open(hs_path(), "w") as f:
            f.write(str(score))
    except Exception:
        pass

def first_existing(*candidates):
    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def load_music(name_no_ext):
    path = first_existing(f"soundfiles/{name_no_ext}.ogg", f"soundfiles/{name_no_ext}.mp3")
    if path:
        pygame.mixer.music.load(path)

def load_sound(name_no_ext):
    path = first_existing(f"soundfiles/{name_no_ext}.ogg", f"soundfiles/{name_no_ext}.wav", f"soundfiles/{name_no_ext}.mp3")
    return pygame.mixer.Sound(path) if path else None

def draw_button(xpos, ypos, colour, text, w, h):
    pygame.draw.rect(screen, colour, (xpos, ypos, w, h), border_radius=10)
    msg = FONT.render(text, True, (0, 0, 0))
    screen.blit(msg, (xpos + 25, ypos + 12))

def init_pygame():
    global screen, CLOCK, FONT, FONT1, FONT2, FONT3, FONT4
    pygame.init()
    pygame.display.set_caption("Subway Surfers by group 3 (web)")
    screen = pygame.display.set_mode((width, height))
    CLOCK = pygame.time.Clock()

    FONT  = pygame.font.Font(None, 40)
    FONT1 = pygame.font.Font(None, 30)
    FONT2 = pygame.font.Font(None, 25)
    FONT3 = pygame.font.Font(None, 70)
    FONT4 = pygame.font.Font(None, 40)

    try:
        pygame.mixer.init()
    except Exception:
        pass

async def start_screen():
    try:
        load_music("menumusic")
        pygame.mixer.music.play(-1)
    except Exception:
        pass

    while True:
        screen.blit(bgimage, (0, 0))
        screen.blit(Subway_Surfers, (0, 150))
        label = FONT.render("Press ENTER or click below to start", True, (255, 255, 0))
        screen.blit(label, (130, 470))
        draw_button(270, 530, (229, 158, 36), "LET'S GO!!", 200, 60)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 270 < mouse[0] < 470 and 530 < mouse[1] < 590:
            draw_button(270, 530, (220, 160, 220), "LET'S GO!!", 200, 60)
            if click[0]:
                return

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RETURN:
                return

        pygame.display.update()
        await asyncio.sleep(0)

async def game_over_screen():
    while True:
        screen.blit(bgimage, (0, 0))
        screen.blit(Subway_Surfers, (0, 150))
        label = FONT3.render("GAME OVER", True, (255, 255, 0))
        screen.blit(label, (250, 380))
        label2 = FONT4.render("PLAY AGAIN ???", True, (255, 165, 0))
        screen.blit(label2, (230, 450))
        final_coins = FONT2.render(f"Coins Collected: {coins_collected}", True, (255, 255, 0))
        screen.blit(final_coins, (280, 420))
        draw_button(250, 500, (0, 150, 0), "YES", 100, 50)
        draw_button(420, 500, (150, 0, 0), "QUIT", 100, 50)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 250 < mouse[0] < 350 and 500 < mouse[1] < 550:
            draw_button(250, 500, (220, 160, 220), "YES", 100, 50)
            if click[0]:
                return True
        if 420 < mouse[0] < 520 and 500 < mouse[1] < 550:
            draw_button(420, 500, (220, 160, 220), "QUIT", 100, 50)
            if click[0]:
                return False

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False

        pygame.display.update()
        await asyncio.sleep(0)

async def run_one_game():
    global position, y, coins_collected, show_coin, coin_x, coin_y

    a = b = FPS_change = 0
    FPS = 40
    score = 0.0
    coins_collected = 0
    show_coin = False
    position = 365
    y = 0
    running = True

    trains = [train1,train2,train3,train4,train5,train6,train7,train8]
    random_train = random.choice(trains)
    Blockers = [Blocker, Blocker1, Blocker2]
    random_Blocker = random.choice(Blockers)
    random_Blocker2 = random.choice(Blockers[0:2])
    obstacle_strategy = random.randint(0, 6)

    swish = load_sound("swish")
    coin_snd = load_sound("coin")
    try:
        load_music("bgmusic")
        pygame.mixer.music.play(-1)
    except Exception:
        pass

    topScore = load_top_score()

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if position == 615:
                    if swish: swish.play()
                    position = 115
                else:
                    if swish: swish.play()
                    position += 250
            if event.key == pygame.K_LEFT:
                if position == 115:
                    if swish: swish.play()
                    position = 615
                else:
                    if swish: swish.play()
                    position -= 250

        screen.fill(bgcolour)
        rel_y = y % Track.get_rect().height
        screen.blit(Track, (200, rel_y - Track.get_rect().height))
        if rel_y < height: screen.blit(Track, (200, rel_y))
        screen.blit(Rail, (10, rel_y - Rail.get_rect().height))
        if rel_y < height: screen.blit(Rail, (10, rel_y))
        screen.blit(Rail, (515, rel_y - Rail.get_rect().height))
        if rel_y < height: screen.blit(Rail, (515, rel_y))
        y += 10

        screen.blit(Jake, (position, 500))

        if not show_coin and random.randint(0, 100) < 2:
            show_coin = True
            coin_x = random.choice([115, 365, 615])
            coin_y = -50

        if show_coin:
            screen.blit(Coin, (coin_x, coin_y))
            coin_y += 10
            if position == coin_x and 450 < coin_y < 550:
                coins_collected += 1
                show_coin = False
                if coin_snd: coin_snd.play()
            if coin_y > 800:
                show_coin = False

        def crash():
            try:
                load_music("accident")
                pygame.mixer.music.play(1)
            except Exception:
                pass
            return False

        if obstacle_strategy == 0:
            screen.blit(random_Blocker, (30, a - 500)); a += 10
            if a > 1300:
                a = 0; random_Blocker = random.choice(Blockers); obstacle_strategy = random.randint(0, 6)
            if position == 115 and a - 500 == 200:
                running = crash()

        if obstacle_strategy == 1:
            screen.blit(random_train, (350, a - 200)); a += 15
            if a > 900:
                a = 0; random_train = random.choice(trains); obstacle_strategy = random.randint(0, 6)
            if position == 365 and 310 <= a - 200 <= 550:
                running = crash()

        if obstacle_strategy == 2:
            screen.blit(random_Blocker2, (550, a - 500)); a += 10
            if a > 1300:
                a = 0; random_Blocker2 = random.choice(Blockers[0:2]); obstacle_strategy = random.randint(0, 6)
            if position == 615 and a - 500 == 200:
                running = crash()

        if obstacle_strategy == 3:
            screen.blit(random_Blocker2, (550, a - 500))
            screen.blit(random_Blocker, (30, a - 500)); a += 10
            if a > 1300:
                a = 0; random_Blocker = random.choice(Blockers); random_Blocker2 = random.choice(Blockers[0:2]); obstacle_strategy = random.randint(0, 6)
            if (position == 615 and a - 500 == 200) or (position == 115 and a - 500 == 200):
                running = crash()

        if obstacle_strategy == 4:
            screen.blit(random_train, (350, b - 200)); b += 15
            screen.blit(random_Blocker, (30, a - 500));  a += 10
            if a > 1300 and b > 900:
                a = b = 0; random_Blocker = random.choice(Blockers); random_train = random.choice(trains); obstacle_strategy = random.randint(0, 6)
            if (position == 365 and 310 <= b - 200 <= 550) or (position == 115 and a - 500 == 200):
                running = crash()

        if obstacle_strategy == 5:
            screen.blit(random_train, (350, b - 200)); b += 15
            screen.blit(random_Blocker2, (550, a - 500)); a += 10
            if a > 1300 and b > 900:
                a = b = 0; random_Blocker2 = random.choice(Blockers[0:2]); random_train = random.choice(trains); obstacle_strategy = random.randint(0, 6)
            if (position == 365 and 310 <= b - 200 <= 550) or (position == 615 and a - 500 == 200):
                running = crash()

        if obstacle_strategy == 6:
            screen.blit(random_train, (350, b - 200)); b += 15
            screen.blit(random_Blocker,  (30,  a - 500))
            screen.blit(random_Blocker2, (550, a - 500)); a += 10
            if a > 1300 and b > 900:
                a = b = 0
                random_Blocker  = random.choice(Blockers)
                random_Blocker2 = random.choice(Blockers[0:2])
                random_train    = random.choice(trains)
                obstacle_strategy = random.randint(0, 6)
            if (position == 365 and 310 <= b - 200 <= 550) or ((position == 115 or position == 615) and a - 500 == 200):
                running = crash()

        score += 0.1
        score_value = FONT.render("Score : " + str(round(score, 1)), True, (255,153,52))
        high_score  = FONT.render("Top Score: " + str(round(topScore, 1)), True, (255,153,52))
        coin_text   = FONT.render("Coins: " + str(coins_collected), True, (255,215,0))
        screen.blit(score_value, (10, 10))
        screen.blit(high_score,  (10, 40))
        screen.blit(coin_text,   (10, 70))

        pygame.display.update()
        if score > topScore:
            save_top_score(score)
            topScore = score

        FPS_change += 1
        if FPS_change % 200 == 0:
            FPS += 5

        CLOCK.tick(FPS)
        await asyncio.sleep(0)

    return True

async def main():
    init_pygame()
    await start_screen()
    keep_playing = True
    while keep_playing:
        alive = await run_one_game()
        if not alive:
            break
        keep_playing = await game_over_screen()
