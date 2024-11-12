import pygame

# Backgrounds
Track = pygame.image.load("pictures/Track.png")
Track = pygame.transform.scale(Track,(500,800))
Rail = pygame.image.load("pictures/Rail.jpg")
Rail = pygame.transform.scale(Rail,(500,800))

# Player sprite
Jake = pygame.image.load("pictures/Jake.png")
Jake = pygame.transform.scale(Jake,(130,140))

# Coin sprite
Coin = pygame.image.load("pictures/coin.png")
Coin = pygame.transform.scale(Coin,(80,80))

# Obstacles sprites
train1 = pygame.image.load("pictures/train1.png")
train1 = pygame.transform.scale(train1,(120,240))
train2 = pygame.image.load("pictures/train2.png")
train2 = pygame.transform.scale(train2,(120,240))
train3 = pygame.image.load("pictures/train3.png")
train3 = pygame.transform.scale(train3,(120,240))
train4 = pygame.image.load("pictures/train4.png")
train4 = pygame.transform.scale(train4,(120,240))
train5 = pygame.image.load("pictures/train5.png")
train5 = pygame.transform.scale(train5,(120,240))
train6 = pygame.image.load("pictures/train6.png")
train6 = pygame.transform.scale(train6,(120,240))
train7 = pygame.image.load("pictures/train7.png")
train7 = pygame.transform.scale(train7,(120,240))
train8 = pygame.image.load("pictures/train8.png")
train8 = pygame.transform.scale(train8,(120,240))

Blocker = pygame.image.load("pictures/Blocker.png")
Blocker = pygame.transform.scale(Blocker,(204,208))
Blocker1 = pygame.image.load("pictures/Blocker1.png")
Blocker1 = pygame.transform.scale(Blocker1,(204,208))
Blocker2 = pygame.image.load("pictures/Blocker2.png")
Blocker2 = pygame.transform.scale(Blocker2,(204,208))

bgimage = pygame.image.load("pictures/Background1.jpg")
bgimage = pygame.transform.scale(bgimage,(800,800))  # Added proper scaling for background
Subway_Surfers = pygame.image.load("pictures/Subway_Surfers.png")
Subway_Surfers = pygame.transform.scale(Subway_Surfers,(800,300))