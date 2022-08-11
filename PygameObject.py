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
        self.is_attacking = -1
        self.attack_speed = Globles.get_chara_stat(hero_name, 1)
        self.attack = Globles.get_chara_stat(hero_name, 3)
        self.defence = Globles.get_chara_stat(hero_name, 4)
        self.attack_x = 0
        self.attack_y = 0
        self.skills_cd = Globles.get_chara_stat(hero_name, 5)
        self.skill1_cast = 0
        self.skill2_cast = 0
        self.bullet_launched = False

    def update(self, screen):
        if self.is_attacking != -1:
            if pygame.time.get_ticks() - self.last_move >= self.attack_speed * len(self.imageset[self.gesture]):
                if self.is_attacking == 1:
                    self.skill1_cast = pygame.time.get_ticks()
                elif self.is_attacking == 2:
                    self.skill2_cast = pygame.time.get_ticks()
                self.is_attacking = -1
                self.gesture = 0
                self.halt = True
                self.rect.x = self.attack_x
                self.rect.y = self.attack_y
                self.image = self.imageset[0][0]
            else:
                image_index = (pygame.time.get_ticks() - self.last_move) // self.attack_speed % len(self.imageset[self.gesture])
                self.image = self.imageset[self.gesture][image_index]
                (att_adj_x, att_adj_y) = Globles.get_attack_adjustment(self.hero_name, self.is_attacking, self.reflect)
                self.rect.x = self.attack_x + att_adj_x
                self.rect.y = self.attack_y + att_adj_y
                if self.reflect:
                    self.image = pygame.transform.flip(self.image, True, False)
                if image_index == 1 and not self.bullet_launched:
                    if self.hero_name == 'jie':
                        if self.is_attacking == 1:
                            bullet = Bullet('fireball', 5, self.reflect, 5, False, 50, True)
                            bullet.rect.x = (self.attack_x - 20) if self.reflect else (self.attack_x + 20)
                            bullet.rect.y = self.attack_y - 20
                            Globles.add_bullet(bullet)
                            self.bullet_launched = True
                        elif self.is_attacking == 2:
                            bullet = Bullet('wind', 0, self.reflect, 5, False, 150, False)
                            bullet.rect.x = self.attack_x - 70
                            bullet.rect.y = self.attack_y - 70
                            Globles.add_bullet(bullet, 0)
                            self.bullet_launched = True
        elif not self.halt:
            self.image = self.imageset[self.gesture][pygame.time.get_ticks() // 200 % len(self.imageset[self.gesture])]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.imageset[0][0]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)
        if self.is_attacking != -1:
            ShowHP(screen, self.attack_x, self.attack_y, self.hp, self.max_hp)
        else:
            ShowHP(screen, self.rect.x, self.rect.y, self.hp, self.max_hp)
        key_list = pygame.key.get_pressed()
        if self.isMoveAllowed and self.is_attacking == -1:
            if key_list[pygame.K_o] and pygame.time.get_ticks() - self.skill2_cast > self.skills_cd[1]:
                self.halt = False
                self.is_attacking = 2
                self.attack_x = self.rect.x
                self.attack_y = self.rect.y
                self.gesture = 4
                self.last_move = pygame.time.get_ticks()
                self.bullet_launched = False
            elif key_list[pygame.K_i] and pygame.time.get_ticks() - self.skill1_cast > self.skills_cd[0]:
                self.halt = False
                self.is_attacking = 1
                self.attack_x = self.rect.x
                self.attack_y = self.rect.y
                self.gesture = 3
                self.last_move = pygame.time.get_ticks()
                self.bullet_launched = False
            elif key_list[pygame.K_j]:
                self.halt = False
                self.is_attacking = 0
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


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self, effect_name, speed, reflect, damage, simple, effect_speed, self_destroy):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.imageset = Globles.get_effect_image(effect_name)
        self.image = self.imageset[0]
        self.speed = speed
        self.effect_speed = effect_speed
        self.rect = self.image.get_rect()
        self.reflect = reflect
        self.simple = simple
        self.damage = damage
        self.create_time = pygame.time.get_ticks()
        self.self_destroy = self_destroy

    def update(self, screen):
        if self.reflect:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if not self.simple:
            self.image = self.imageset[(pygame.time.get_ticks() - self.create_time) // self.effect_speed % len(self.imageset)]
        if self.reflect:
            self.image = pygame.transform.flip(self.image, True, False)
        if pygame.time.get_ticks() - self.create_time >= len(self.imageset) * self.effect_speed:
            Globles.remove_bullet(self)


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
