import pygame
import Globles


class PygameObject(pygame.sprite.Sprite):
    """
    This class represents all the objects in the game
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, imageset, gesture, speed, x, y) -> None:
        super().__init__()
        self.type = 'object'
        self.name = 'object'
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
        self.type = 'character'
        self.name = hero_name
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
        self.skill1_cast = -100000
        self.skill2_cast = -100000
        self.bullet_launched = False
        self.buff_list = {}

    def update(self, screen):

        # 攻击/施法动画
        if self.is_attacking != -1:
            # 结束攻击/施法状态
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
            # 攻击/施法
            else:
                image_index = (pygame.time.get_ticks() - self.last_move) // self.attack_speed % len(
                    self.imageset[self.gesture])
                image_index = int(image_index)
                self.image = self.imageset[self.gesture][image_index]
                (att_adj_x, att_adj_y) = Globles.get_attack_adjustment(self.name, self.is_attacking, self.reflect)
                self.rect.x = self.attack_x + att_adj_x
                self.rect.y = self.attack_y + att_adj_y
                # 判断朝向
                if self.reflect:
                    self.image = pygame.transform.flip(self.image, True, False)
                # 技能效果
                if self.name == 'jie':
                    if image_index == 1 and not self.bullet_launched:
                        if self.is_attacking == 1:
                            bullet = Bullet('fireball', 5, self.reflect, 5, False, 50, True)
                            bullet.rect.x = (self.attack_x - 20) if self.reflect else (self.attack_x + 20)
                            bullet.rect.y = self.attack_y - 20
                            Globles.add_bullet(bullet)
                            self.bullet_launched = True
                        elif self.is_attacking == 2:
                            Globles.add_buff(self, 'mhp_up', 15, 1.5)
                            Globles.add_buff(self, 'def_up', 15, 1.5)
                            Globles.add_buff(self, 'heal', 5, 5)
                            bullet = Bullet('wind', 0, self.reflect, 5, False, 150, False)
                            bullet.rect.x = self.attack_x - 70
                            bullet.rect.y = self.attack_y - 70
                            Globles.add_bullet(bullet, 0)
                            self.bullet_launched = True
                elif self.name == 'yichen':
                    if image_index == 1 and not self.bullet_launched:
                        if self.is_attacking == 2:
                            ratio = self.hp / self.max_hp
                            if ratio >= 0.8:
                                Globles.add_buff(self, 'def_down', 10, 2)
                                Globles.add_buff(self, 'atk_up', 10, 2)
                                Globles.add_buff(self, 'poison', 3, 2)
                                Globles.add_buff(self, 'agi_up', 3, 2)
                            elif ratio >= 0.6:
                                Globles.add_buff(self, 'def_down', 10, 1.5)
                                Globles.add_buff(self, 'atk_up', 10, 1.5)
                                Globles.add_buff(self, 'poison', 3)
                                Globles.add_buff(self, 'agi_up', 3, 1.5)
                            elif ratio >= 0.4:
                                Globles.add_buff(self, 'def_up', 10, 1.5)
                                Globles.add_buff(self, 'atk_down', 10, 1.5)
                            else:
                                Globles.add_buff(self, 'def_up', 10, 2)
                                Globles.add_buff(self, 'atk_down', 10, 2)
                                Globles.add_buff(self, 'heal', 3)
                            self.bullet_launched = True
        # 播放当前动作
        elif not self.halt:
            self.image = self.imageset[self.gesture][pygame.time.get_ticks() // 200 % len(self.imageset[self.gesture])]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)
        # 停止当前动作
        else:
            self.image = self.imageset[0][0]
            if self.reflect:
                self.image = pygame.transform.flip(self.image, True, False)

        # Buff结算
        self.defence = Globles.get_chara_stat(self.name, 4)
        self.attack = Globles.get_chara_stat(self.name, 3)
        self.max_hp = Globles.get_chara_stat(self.name, 2)
        self.attack_speed = Globles.get_chara_stat(self.name, 1)
        self.speed = Globles.get_chara_stat(self.name, 0)
        for buff_name in self.buff_list.keys():
            if buff_name in ['Skill1_CD', 'Skill2_CD', 'Casting/Attacking']:
                continue
            buff = self.buff_list.get(buff_name, False)
            if not buff[0]:
                continue
            if buff[0] >= pygame.time.get_ticks() or buff[0] is True:
                if buff_name == 'def_up':
                    self.defence *= buff[1]
                if buff_name == 'def_down':
                    self.defence /= buff[1]
                if buff_name == 'atk_up':
                    self.attack *= buff[1]
                if buff_name == 'atk_down':
                    self.attack /= buff[1]
                if buff_name == 'mhp_up':
                    self.max_hp *= buff[1]
                if buff_name == 'mhp_down':
                    self.max_hp /= buff[1]
                if buff_name == 'agi_up':
                    self.speed *= buff[1]
                    self.attack_speed /= buff[1]
                if buff_name == 'agi_down':
                    self.speed /= buff[1]
                    self.attack_speed *= buff[1]
                if buff_name == 'heal':
                    if self.hp < self.max_hp:
                        self.hp += 0.02 * buff[1]
                if buff_name == 'poison':
                    if self.hp > self.max_hp * 0.2:
                        self.hp -= 0.02 * buff[1]

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        # 显示HP和Buff
        if self.is_attacking != -1:
            self.buff_list['Casting/Attacking'] = True
            ShowHP(screen, self.attack_x, self.attack_y, self.hp, self.max_hp, True)
            show_buff(screen, self.attack_x, self.attack_y, self.buff_list, True)
        else:
            self.buff_list['Casting/Attacking'] = False
            ShowHP(screen, self.rect.x, self.rect.y, self.hp, self.max_hp, True)
            show_buff(screen, self.rect.x, self.rect.y, self.buff_list, True)

        # 技能冷却检测和技能图标显示
        Globles.show_text(screen, "J", 500, 475, color='black', size=18)
        Globles.show_text(screen, "I", 570, 475, color='black', size=18)
        Globles.show_text(screen, "O", 640, 475, color='black', size=18)
        if self.is_attacking == -1:
            screen.blit(Globles.get_buff_image('attack'), (480, 430))
        else:
            screen.blit(Globles.get_buff_image('attack_cd'), (480, 430))
        if pygame.time.get_ticks() - self.skill2_cast <= self.skills_cd[1]:
            self.buff_list['Skill2_CD'] = True
            screen.blit(Globles.get_buff_image('{}_skill_2_cd'.format(self.name)), (620, 430))
            Globles.show_text(screen,
                              str(round((self.skill2_cast + self.skills_cd[1] - pygame.time.get_ticks()) / 1000, 1)),
                              645, 455, size=18, color='red', middle=True)
        else:
            self.buff_list['Skill2_CD'] = False
            if self.is_attacking == -1:
                screen.blit(Globles.get_buff_image('{}_skill_2'.format(self.name)), (620, 430))
            else:
                screen.blit(Globles.get_buff_image('{}_skill_2_cd'.format(self.name)), (620, 430))
        if pygame.time.get_ticks() - self.skill1_cast <= self.skills_cd[0]:
            self.buff_list['Skill1_CD'] = True
            screen.blit(Globles.get_buff_image('{}_skill_1_cd'.format(self.name)), (550, 430))
            Globles.show_text(screen,
                              str(round((self.skill1_cast + self.skills_cd[0] - pygame.time.get_ticks()) / 1000, 1)),
                              575, 455, size=18, color='red', middle=True)
        else:
            self.buff_list['Skill1_CD'] = False
            if self.is_attacking == -1:
                screen.blit(Globles.get_buff_image('{}_skill_1'.format(self.name)), (550, 430))
            else:
                screen.blit(Globles.get_buff_image('{}_skill_1_cd'.format(self.name)), (550, 430))

        # 按键检测
        key_list = pygame.key.get_pressed()
        if self.isMoveAllowed and self.is_attacking == -1:
            if key_list[pygame.K_o] and self.buff_list.get('Skill2_CD') is False:
                self.halt = False
                self.is_attacking = 2
                self.attack_x = self.rect.x
                self.attack_y = self.rect.y
                self.gesture = 4
                self.last_move = pygame.time.get_ticks()
                self.bullet_launched = False
            elif key_list[pygame.K_i] and self.buff_list.get('Skill1_CD') is False:
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
        self.type = 'effect'
        self.name = effect_name
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
            self.image = self.imageset[
                (pygame.time.get_ticks() - self.create_time) // self.effect_speed % len(self.imageset)]
        if self.reflect:
            self.image = pygame.transform.flip(self.image, True, False)
        if pygame.time.get_ticks() - self.create_time >= len(self.imageset) * self.effect_speed:
            Globles.remove_bullet(self)


def ShowHP(screen, x, y, hp, max_hp, is_player=False):
    ratio = hp / max_hp
    if ratio < 0:
        ratio = 0
    if is_player:
        length = 100 + max_hp * 2
        x = 180
        y = 450
        position_g = (x, y - 10, length * ratio, 25)
        position_r = (x + length * ratio, y - 10, length - length * ratio, 25)
        pygame.draw.rect(screen, Globles.get_color('green'), position_g, width=0)
        pygame.draw.rect(screen, Globles.get_color('red'), position_r, width=0)
        Globles.show_text(screen, "HP: {:.1f}/{:.1f}".format(hp, max_hp), 10, 435,
                          color='black' if ratio > 0.3 else 'red')
    else:
        length = 20 + max_hp * 0.4
        position_g = (x, y - 10, length * ratio, 5)
        position_r = (x + length * ratio, y - 10, length - length * ratio, 5)
        pygame.draw.rect(screen, Globles.get_color('green'), position_g, width=0)
        pygame.draw.rect(screen, Globles.get_color('red'), position_r, width=0)


def show_buff(screen, x, y, buff_list, is_player=False):
    if is_player:
        x_shift = 10
        for buff_name in buff_list.keys():
            if buff_name in ['Skill1_CD', 'Skill2_CD', 'Casting/Attacking']:
                continue
            buff = buff_list.get(buff_name, False)
            if not buff[0]:
                continue
            if buff[0] >= pygame.time.get_ticks() or buff[0] is True:
                buff_image = Globles.get_buff_image(buff_name)
                buff_image.set_alpha((buff[0] - pygame.time.get_ticks()) // 10)
                if buff[0] is True:
                    buff_image.set_alpha(255)
                screen.blit(buff_image, (x_shift, 470))
                x_shift += 25
    else:
        y_shift = -35
        x_shift = -5
        cnt = 0
        for buff_name in buff_list.keys():
            if buff_name in ['Skill1_CD', 'Skill2_CD', 'Casting/Attacking']:
                continue
            buff = buff_list.get(buff_name, False)
            if not buff[0]:
                continue
            if buff[0] >= pygame.time.get_ticks() or buff[0] is True:
                buff_image = Globles.get_buff_image(buff_name)
                buff_image.set_alpha((buff[0] - pygame.time.get_ticks()) // 10)
                if buff[0] is True:
                    buff_image.set_alpha(255)
                screen.blit(buff_image, (x + x_shift, y + y_shift))
                x_shift += 20
                cnt += 1
                if cnt % 5 == 0:
                    y_shift -= 30
                    x_shift = -20


def CheckMove(x, y, dx, dy):
    des_x = x + dx
    des_y = y + dy
    (screen_w, screen_h) = Globles.get_screen_size()
    if 0 < des_x < screen_w and 0 < des_y < screen_h:
        return True
    else:
        return False
