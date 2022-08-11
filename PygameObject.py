import pygame
import Globles


class PygameObject(pygame.sprite.Sprite):
    """
    This class represents all the objects in the game
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, imageset, gesture, speed, x, y) -> None:
        super().__init__()
        self.speed = speed
        self.imageset = imageset
        self.image = imageset[gesture][0]
        self.gesture = gesture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.reflect = False

    def reset_location(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_left(self):
        if CheckMove(self.rect.x, self.rect.y, -self.speed, 0):
            self.rect.x -= self.speed
        self.gesture = 1
        self.reflect = True

    def move_right(self):
        if CheckMove(self.rect.x + self.rect.width, self.rect.y, self.speed, 0):
            self.rect.x += self.speed
        self.gesture = 1
        self.reflect = False

    def idle(self):
        self.gesture = 0

    def update(self, screen):
        if self.reflect:
            self.image = pygame.transform.flip(self.imageset[self.gesture][0], True, False)


class Character(PygameObject):
    def __init__(self, hero_name, x, y) -> None:
        super().__init__(Globles.get_chara_image(hero_name), 0, Globles.get_chara_stat(hero_name, 0), x, y)
        self.hero_name = hero_name
        self.isMoveAllowed = True
        self.max_hp = Globles.get_chara_stat(hero_name, 2)
        self.hp = self.max_hp
        self.last_move = -1
        self.halt = False
        self.is_attacking = False
        self.attack_speed = Globles.get_chara_stat(hero_name, 1)
        self.attack = Globles.get_chara_stat(hero_name, 3)
        self.defence = Globles.get_chara_stat(hero_name, 4)
        self.attack_x = 0
        self.attack_y = 0

    def update(self, screen):
        if self.is_attacking:
            if pygame.time.get_ticks() - self.last_move >= self.attack_speed * len(self.imageset[self.gesture]):
                self.is_attacking = False
                self.gesture = 0
                self.halt = True
                self.rect.x = self.attack_x
                self.rect.y = self.attack_y
                self.image = self.imageset[0][0]
            else:
                self.image = self.imageset[self.gesture][(pygame.time.get_ticks() - self.last_move) // self.attack_speed % len(self.imageset[self.gesture])]
                (att_adj_x, att_adj_y) = Globles.get_attack_adjustment(self.hero_name, 0, self.reflect)
                self.rect.x = self.attack_x + att_adj_x
                self.rect.y = self.attack_y + att_adj_y
                if self.reflect:
                    self.image = pygame.transform.flip(self.image, True, False)
        elif not self.halt:
            self.image = self.imageset[self.gesture][pygame.time.get_ticks() // 200 % len(self.imageset[self.gesture])]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.imageset[0][0]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)
        if self.is_attacking:
            ShowHP(screen, self.attack_x, self.attack_y, self.hp, self.max_hp)
        else:
            ShowHP(screen, self.rect.x, self.rect.y, self.hp, self.max_hp)
        key_list = pygame.key.get_pressed()
        if self.isMoveAllowed and not self.is_attacking:
            if key_list[pygame.K_j]:
                self.halt = False
                self.is_attacking = True
                self.attack_x = self.rect.x
                self.attack_y = self.rect.y
                self.gesture = 2
                self.last_move = pygame.time.get_ticks()
            elif key_list[pygame.K_d]:
                self.halt = False
                self.move_right()
                self.last_move = pygame.time.get_ticks()
            elif key_list[pygame.K_a]:
                self.halt = False
                self.move_left()
                self.last_move = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - self.last_move > 2500:
                self.halt = False
                self.idle()
            else:
                self.halt = True


def ShowHP(screen, x, y, hp, max_hp):
    ratio = hp / max_hp
    if ratio < 0:
        ratio = 0
    length = 20 + max_hp * 0.4
    position_g = (x, y - 10, length * ratio, 5)
    position_r = (x + length * ratio, y - 10, length - length * ratio, 5)
    pygame.draw.rect(screen, Globles.get_color('green'), position_g, width=0)
    pygame.draw.rect(screen, Globles.get_color('red'), position_r, width=0)


def CheckMove(x, y, dx, dy):
    des_x = x + dx
    des_y = y + dy
    (screen_w, screen_h) = Globles.get_screen_size()
    if 0 < des_x < screen_w and 0 < des_y < screen_h:
        return True
    else:
        return False
