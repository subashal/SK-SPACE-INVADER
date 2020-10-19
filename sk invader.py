import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((750, 650))
pygame.display.set_caption("  SPACE INVADER")

white = (255, 255, 255)

green = (0, 255, 0)

navy = (0,0,128)
red = (255,0,0)

black = (0, 0, 0)

purple=(199,0,200)
grey =(128, 128, 128)

game_over=False



# class for ship
class Ship(pygame.sprite.Sprite):  # it is used to show object on screen just like a import state, use information
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # it is used to initiliaze the sprite
        self.image = pygame.Surface([50,25])
        self.image.fill(green)

        self.rect = self.image.get_rect()
        self.live = 5
        self.level = 1
        self.score = 0
        self.highscore = 0

    def dra(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# class for enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([15,15])
        self.image.fill(red)

        self.rect = self.image.get_rect()


# class for bunker
class bunk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(navy)
        self.rect = self.image.get_rect()

#class for missile 1 and shooting direction
class mis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 25

#class for missile 2 and shooting direction
class mis2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 25

#class for missile 3 and shooting direction
class mis3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 25

#class for missile 4 and shooting direction
class mis4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 25

#class for bomb 1 and shooting direction
class bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(red)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 10

#class for bomb 2 and shooting direction
class bomb2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(red)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 10

#class for bomb 3 and shooting directionand shooting direction
class bomb3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(red)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 10

#class for bomb 4 and shooting direction
class bomb4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 5])
        self.image.fill(red)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 10


ship = Ship()
ship.rect.x = 375
ship.rect.y = 300

enemy_list_1 = pygame.sprite.Group()
enemy_list_2 = pygame.sprite.Group()
enemy_list_3 = pygame.sprite.Group()
enemy_list_4 = pygame.sprite.Group()

bunker = bunk()
bunker_list = pygame.sprite.Group()
bunker_list_2 = pygame.sprite.Group()
bunker_list_3 = pygame.sprite.Group()
bunker_list_4 = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
missile_list_2 = pygame.sprite.Group()
missile_list_3 = pygame.sprite.Group()
missile_list_4 = pygame.sprite.Group()

bomb_list = pygame.sprite.Group()
bomb_list_2 = pygame.sprite.Group()
bomb_list_3 = pygame.sprite.Group()
bomb_list_4 = pygame.sprite.Group()
bomb_chance = ship.level * 2
# missile
missile = mis()


enemy_change_size_row = ship.level + 3
enemy_change_size_col = ship.level + 3


def enemies():
    for row in range(4):
        for col in range(enemy_change_size_col):
            enemy_1 = Enemy()
            enemy_1.rect.x = 100 + (35 * col)
            enemy_1.rect.y = 10 + (30 * row)
            enemy_list_1.add(enemy_1)
    for row in range(4):
        for col in range(enemy_change_size_col):
            enemy_2 = Enemy()
            enemy_2.rect.x = 100 + (35 * col)
            enemy_2.rect.y = 500 + (30 * row)
            enemy_list_2.add(enemy_2)
    for row in range(enemy_change_size_row):
        for col in range(4):
            enemy_3 = Enemy()
            enemy_3.rect.x = 10 + (30 * col)
            enemy_3.rect.y = 40 + (35 * row)
            enemy_list_3.add(enemy_3)
    for row in range(enemy_change_size_row):
        for col in range(4):
            enemy_4 = Enemy()
            enemy_4.rect.x = 580 + (30 * col)
            enemy_4.rect.y = 40 + (35 * row)
            enemy_list_4.add(enemy_4)


# bunker
bunker_change_size_row=ship.level+7
bunker_change_size_col=ship.level+7
def bunkers():
    # for bun in range(1,5):
    for row in range(bunker_change_size_row):
        for col in range(4):
            bunker = bunk()
            bunker.rect.x = 250 + (11 * col)
            bunker.rect.y = 250 + (11 * row)
            bunker_list.add(bunker)

    for row in range(bunker_change_size_row):
        for col in range(4):
            bunker = bunk()
            bunker.rect.x = 500 + (11 * col)
            bunker.rect.y = 250 + (11 * row)
            bunker_list_2.add(bunker)

    for row in range(4):
        for col in range(bunker_change_size_col):
            bunker = bunk()
            bunker.rect.x = 310 + (11 * col)
            bunker.rect.y = 190 + (11 * row)
            bunker_list_3.add(bunker)
    for bun in range(1, 5):
        for row in range(4):
            for col in range(bunker_change_size_col):
                bunker = bunk()
                bunker.rect.x = 310 + (11 * col)
                bunker.rect.y = 380 + (11 * row)
                bunker_list_4.add(bunker)

#function for game over
def game_over_screen():
    font = pygame.font.SysFont('Courier New', 45)
    for sh in range(1, ship.level + 1):
        if sh == ship.level:
            text = font.render("LEVEL " + str(sh), False, purple)

            textRect = text.get_rect()
            textRect.center = (750 // 2, 190)
            screen.blit(text, textRect)
    font = pygame.font.SysFont('Courier New', 70)
    text = font.render("GAME OVER", False, white)

    textRect = text.get_rect()
    textRect.center = (750 // 2, 300)
    screen.blit(text, textRect)
    font = pygame.font.SysFont('Courier New', 45)
    text = font.render("HIGHSCORE :" + str(ship.highscore), False, red)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 400)
    screen.blit(text, textRect)

    # start message

    text = font.render("PRESS  SPACE TO START", False, green)

    textRect = text.get_rect()
    textRect.center = (750 // 2, 550)
    screen.blit(text, textRect)
    # if ship.level == 1:

#next level on process
def level():
    font = pygame.font.SysFont('Courier New', 55)
    for sh in range(1, ship.level + 1):
        if sh == ship.level:
            text = font.render("LEVEL " + str(sh), False, purple)

            textRect = text.get_rect()
            textRect.center = (750 // 2, 190)
            screen.blit(text, textRect)
    font = pygame.font.SysFont('Courier New', 50)
    text = font.render("NEXT LEVEL ", False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 300)
    screen.blit(text, textRect)
    font = pygame.font.SysFont('Courier New', 50)
    text = font.render("    COMMING SOON ..... ", False, white)
    textRect = text.get_rect()
    textRect.center = (410, 360)
    screen.blit(text, textRect)





# function for collide with other with missile 1
def missile_1():
    for missile in missile_list:
        if missile.rect.y < -10:
            missile_list.remove(missile)
        for enemy in enemy_list_1:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list.remove(missile)
                enemy_list_1.remove(enemy)
        for enemy in enemy_list_2:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list.remove(missile)
                enemy_list_2.remove(enemy)
        for enemy in enemy_list_3:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list.remove(missile)
                enemy_list_3.remove(enemy)
        for enemy in enemy_list_4:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list.remove(missile)
                enemy_list_4.remove(enemy)
        for bun in bunker_list:
            if missile.rect.colliderect(bun.rect):
                missile_list.remove(missile)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if missile.rect.colliderect(bun.rect):
                missile_list.remove(missile)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if missile.rect.colliderect(bun.rect):
                missile_list.remove(missile)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if missile.rect.colliderect(bun.rect):
                missile_list.remove(missile)
                bunker_list_4.remove(bun)

# function for collide with other with missile 2
def missile_2():
    for missile in missile_list_2:
        if missile.rect.y > 780:
            missile_list_2.remove(missile)
        for enemy in enemy_list_1:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_2.remove(missile)
                enemy_list_1.remove(enemy)
        for enemy in enemy_list_2:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_2.remove(missile)
                enemy_list_2.remove(enemy)
        for enemy in enemy_list_3:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_2.remove(missile)
                enemy_list_3.remove(enemy)
        for enemy in enemy_list_4:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_2.remove(missile)
                enemy_list_4.remove(enemy)
        for bun in bunker_list:
            if missile.rect.colliderect(bun.rect):
                missile_list_2.remove(missile)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if missile.rect.colliderect(bun.rect):
                missile_list_2.remove(missile)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if missile.rect.colliderect(bun.rect):
                missile_list_2.remove(missile)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if missile.rect.colliderect(bun.rect):
                missile_list_2.remove(missile)
                bunker_list_4.remove(bun)

# function for collide with other with missile 3
def missile_3():
    for missile in missile_list_3:
        if missile.rect.x < -10:
            missile_list_3.remove(missile)
        for enemy in enemy_list_1:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_3.remove(missile)
                enemy_list_1.remove(enemy)
        for enemy in enemy_list_2:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_3.remove(missile)
                enemy_list_2.remove(enemy)
        for enemy in enemy_list_3:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_3.remove(missile)
                enemy_list_3.remove(enemy)
        for enemy in enemy_list_4:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_3.remove(missile)
                enemy_list_4.remove(enemy)
        for bun in bunker_list:
            if missile.rect.colliderect(bun.rect):
                missile_list_3.remove(missile)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if missile.rect.colliderect(bun.rect):
                missile_list_3.remove(missile)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if missile.rect.colliderect(bun.rect):
                missile_list_3.remove(missile)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if missile.rect.colliderect(bun.rect):
                missile_list_3.remove(missile)
                bunker_list_4.remove(bun)

# function for collide with other with missile 4
def missile_4():
    for missile in missile_list_4:
        if missile.rect.x > +680:
            missile_list_4.remove(missile)
        for enemy in enemy_list_1:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_4.remove(missile)
                enemy_list_1.remove(enemy)
        for enemy in enemy_list_2:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_4.remove(missile)
                enemy_list_2.remove(enemy)

        for enemy in enemy_list_3:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_4.remove(missile)
                enemy_list_3.remove(enemy)
        for enemy in enemy_list_4:
            if missile.rect.colliderect(enemy.rect):
                ship.score += 1
                missile_list_4.remove(missile)
                enemy_list_4.remove(enemy)

        for bun in bunker_list:
            if missile.rect.colliderect(bun.rect):
                missile_list_4.remove(missile)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if missile.rect.colliderect(bun.rect):
                missile_list_4.remove(missile)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if missile.rect.colliderect(bun.rect):
                missile_list_4.remove(missile)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if missile.rect.colliderect(bun.rect):
                missile_list_4.remove(missile)
                bunker_list_4.remove(bun)

# function for collide with other with bomb 1
def boo_1():
    for boo in bomb_list:
        if boo.rect.y > 650:
            bomb_list.remove(boo)
        if boo.rect.colliderect(ship.rect):
            bomb_list.remove(boo)
            ship.live -= 1
        for bun in bunker_list:
            if boo.rect.colliderect(bun.rect):
                bomb_list.remove(boo)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if boo.rect.colliderect(bun.rect):
                bomb_list.remove(boo)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if boo.rect.colliderect(bun.rect):
                bomb_list.remove(boo)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if boo.rect.colliderect(bun.rect):
                bomb_list.remove(boo)
                bunker_list_4.remove(bun)

# function for collide with other with bomb 2
def boo_3():
    for boo in bomb_list_3:
        if boo.rect.x > 700:
            bomb_list_3.remove(boo)
        if boo.rect.colliderect(ship.rect):
            bomb_list_3.remove(boo)
            ship.live -= 1
        for bun in bunker_list:
            if boo.rect.colliderect(bun.rect):
                bomb_list_3.remove(boo)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if boo.rect.colliderect(bun.rect):
                bomb_list_3.remove(boo)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if boo.rect.colliderect(bun.rect):
                bomb_list_3.remove(boo)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if boo.rect.colliderect(bun.rect):
                bomb_list_3.remove(boo)
                bunker_list_4.remove(bun)

# function for collide with other with bomb 3
def boo_2():
    for boo in bomb_list_2:
        if boo.rect.x > 700:
            bomb_list_2.remove(boo)
        if boo.rect.colliderect(ship.rect):
            bomb_list_2.remove(boo)
            ship.live -= 1
        for bun in bunker_list:
            if boo.rect.colliderect(bun.rect):
                bomb_list_2.remove(boo)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if boo.rect.colliderect(bun.rect):
                bomb_list_2.remove(boo)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if boo.rect.colliderect(bun.rect):
                bomb_list_2.remove(boo)
                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if boo.rect.colliderect(bun.rect):
                bomb_list_2.remove(boo)
                bunker_list_4.remove(bun)

# function for collide with other with bomb 4
def boo_4():
    for boo in bomb_list_4:
        if boo.rect.x > 700:
            bomb_list_4.remove(boo)
        if boo.rect.colliderect(ship.rect):
            bomb_list_4.remove(boo)
            ship.live -= 1
        for bun in bunker_list:
            if boo.rect.colliderect(bun.rect):
                bomb_list_4.remove(boo)
                bunker_list.remove(bun)
        for bun in bunker_list_2:
            if boo.rect.colliderect(bun.rect):
                bomb_list_4.remove(boo)
                bunker_list_2.remove(bun)
        for bun in bunker_list_3:
            if boo.rect.colliderect(bun.rect):
                bomb_list_4.remove(boo)

                bunker_list_3.remove(bun)
        for bun in bunker_list_4:
            if boo.rect.colliderect(bun.rect):
                bomb_list_4.remove(boo)
                bunker_list_4.remove(bun)

# function for showing the screen as well as game page and front page
def re_draw():
    screen.fill(black)
    if playing:
        bottom = pygame.draw.rect(screen, green, (50, 600, 650, 15))
        for i in range(ship.live):
            pygame.draw.rect(screen, red, (50 + (i * 130), 615, 130, 15))
        # title
        font = pygame.font.SysFont('Courier New', 30)
        text = font.render("SK INVADER", False, white)
        textRect = text.get_rect()
        textRect.center = (750 // 2, 20)
        screen.blit(text, textRect)
        # level
        font = pygame.font.SysFont('Courier New', 30)
        text = font.render("LEVEL:" + str(ship.level), False, white)
        textRect = text.get_rect()
        textRect.center = (69, 15)
        screen.blit(text, textRect)

        # score
        font = pygame.font.SysFont('Courier New', 30)
        text = font.render("SCORE:" + str(ship.score), False, white)
        textRect = text.get_rect()
        textRect.center = (680, 15)
        screen.blit(text, textRect)

        ship.dra()
        enemy_list_1.draw(screen)
        enemy_list_1.update()
        enemy_list_2.draw(screen)
        enemy_list_2.update()
        enemy_list_3.draw(screen)
        enemy_list_3.update()
        enemy_list_4.draw(screen)
        enemy_list_4.update()
        bunker_list.draw(screen)
        bunker_list_2.draw(screen)
        bunker_list_3.draw(screen)
        bunker_list_4.draw(screen)
        missile_list.update()
        missile_list.draw(screen)
        missile_list_2.update()
        missile_list_2.draw(screen)
        missile_list_3.update()
        missile_list_3.draw(screen)
        missile_list_4.update()
        missile_list_4.draw(screen)
        bomb_list.update()
        bomb_list.draw(screen)
        bomb_list_2.update()
        bomb_list_2.draw(screen)
        bomb_list_3.update()
        bomb_list_3.draw(screen)
        bomb_list_4.update()
        bomb_list_4.draw(screen)
    elif  game_over:

        game_over_screen()
    elif ship.level >= 5:
        level()
    else:
        # title
        font = pygame.font.SysFont('Courier New', 60)
        text = font.render("SK INVADER", False, white)
        textRect = text.get_rect()
        textRect.center = (365, 25)
        screen.blit(text, textRect)

        # highscore
        font = pygame.font.SysFont('Courier New', 45)
        text = font.render("HIGHSCORE :" + str(ship.highscore), False, red)
        textRect = text.get_rect()
        textRect.center = (750 // 2, 350)
        screen.blit(text, textRect)

        # start message

        text = font.render("PRESS  SPACE TO START", False, green)

        textRect = text.get_rect()
        textRect.center = (750 // 2, 550)
        screen.blit(text, textRect)
        # if ship.level == 1:
        for sh in range(1,ship.level+1):
            if sh == ship.level:
                text = font.render("LEVEL "+ str(sh), False,purple)

                textRect = text.get_rect()
                textRect.center = (750 // 2, 240)
                screen.blit(text, textRect)








    pygame.display.update()


bunkers()
run = True
playing = False
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if playing:
        x = ship.rect.x
        y = ship.rect.y
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            # print(type(key))
            ship.rect.x -= 10
            ship.rect.y = y

        if key[pygame.K_RIGHT]:
            # print(type(key))
            ship.rect.x += 10
            ship.rect.y = y
        if key[pygame.K_UP]:
            ship.rect.y -= 10
            ship.rect.x = x
        if key[pygame.K_DOWN]:
            ship.rect.y += 10
            ship.rect.x = x
        if key[pygame.K_w]:
            # print(type(key))

            if len(missile_list) < 10:
                missile = mis()
                missile.rect.x = ship.rect.x + 25
                missile.rect.y = ship.rect.y
                missile_list.add(missile)
        if key[pygame.K_s]:
            if len(missile_list_2) < 10:
                missile = mis2()
                missile.rect.x = ship.rect.x + 25
                missile.rect.y = ship.rect.y
                missile_list_2.add(missile)
        if key[pygame.K_a]:
            if len(missile_list_3) < 10:
                missile = mis3()
                missile.rect.x = ship.rect.x
                missile.rect.y = ship.rect.y+10
                missile_list_3.add(missile)
        if key[pygame.K_d]:
            if len(missile_list_4) < 10:
                missile = mis4()
                missile.rect.x = ship.rect.x + 48
                missile.rect.y =  ship.rect.y+ 10
                missile_list_4.add(missile)

        shoot_chance = random.randint(1,20)
        if shoot_chance < bomb_chance:
            if len(enemy_list_1) > 0:
                random_enemy = random.choice(enemy_list_1.sprites())
                boo = bomb()
                boo.rect.x = random_enemy.rect.x + 12
                boo.rect.y = random_enemy.rect.y + 25
                bomb_list.add(boo)
        if shoot_chance < bomb_chance:
            if len(enemy_list_2) > 0:
                random_enemy = random.choice(enemy_list_2.sprites())
                boo = bomb2()
                boo.rect.x = random_enemy.rect.x + 12
                boo.rect.y = random_enemy.rect.y + 25
                bomb_list_2.add(boo)
        if shoot_chance < bomb_chance:
            if len(enemy_list_3) > 0:
                random_enemy = random.choice(enemy_list_3.sprites())
                boo = bomb3()
                boo.rect.x = random_enemy.rect.x + 12
                boo.rect.y = random_enemy.rect.y + 25
                bomb_list_3.add(boo)
        if shoot_chance < bomb_chance:
            if len(enemy_list_4) > 0:
                random_enemy = random.choice(enemy_list_4.sprites())
                boo = bomb4()
                boo.rect.x = random_enemy.rect.x + 12
                boo.rect.y = random_enemy.rect.y + 25
                bomb_list_4.add(boo)

        # movement of enemy
        for en_mov in enemy_list_1:
            if en_mov.rect.x > 0:
                en_mov.rect.x += ship.level + 8
        for en_mov in enemy_list_1:
            if en_mov.rect.x > 725:
                en_mov.rect.x = 140
        for en_mov in enemy_list_2:
            if en_mov.rect.x > 0:
                en_mov.rect.x += ship.level + 8
        for en_mov in enemy_list_2:
            if en_mov.rect.x > 550:
                en_mov.rect.x = 50
        for en_mov in enemy_list_3:
            if en_mov.rect.x > 0:
                en_mov.rect.y += ship.level + 8
        for en_mov in enemy_list_3:
            if en_mov.rect.y > 450:
                en_mov.rect.y = 0
        for en_mov in enemy_list_4:
            if en_mov.rect.x > 500:
                en_mov.rect.y += ship.level + 8
        for en_mov in enemy_list_4:
            if en_mov.rect.y > 650:
                en_mov.rect.y = 140

        # shoot

        missile_1()
        missile_2()
        missile_3()
        missile_4()
        boo_1()
        boo_3()
        boo_2()
        boo_4()

        if ship.live <= 0:
            game_over = True
            playing = False

            bunkers()
            if ship.score > ship.highscore:
                ship.highscore = ship.score
                ship.score = 0
            ship.live = 5
        if len(enemy_list_1) == 0 and len(enemy_list_2) == 0 and len(enemy_list_3) == 0 and len(enemy_list_4) == 0:
            enemies()
            ship.level += 1
            playing = False


    else:

        bomb_list.empty()
        bomb_list_2.empty()
        bomb_list_3.empty()
        bomb_list_4.empty()
        missile_list.empty()
        missile_list_2.empty()
        missile_list_3.empty()
        missile_list_4.empty()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            playing = True
            ship.rect.x = 375
            ship.rect.y = 300
            enemy_list_1.empty()
            enemy_list_2.empty()
            enemy_list_3.empty()
            enemy_list_4.empty()
            enemies()

    re_draw()
pygame.quit()
