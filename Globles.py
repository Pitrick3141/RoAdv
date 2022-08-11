# 全局变量和函数
import pygame
from debugOutp import debug

global globles


class Globles:

    def __init__(self):
        debug("全局变量初始化完成", type='success', who=self.__class__.__name__)

        """
        预设的色彩，以rgb格式保存
        格式:
        color = (red, green, blue)
        0 <= red, green, blue <= 255
        """

        self._colors = {'black': (0, 0, 0),
                        'white': (255, 255, 255),
                        'green': (0, 255, 0),
                        'red': (255, 0, 0),
                        'title_blue': (198, 219, 218),
                        'title_red': (254, 225, 232)}

        """
        屏幕大小
        格式:
        size = (width, height)
        单位: pixel
        """

        self._screen_size = (700, 500)

        """
        阶段记录，用于设置动画等
        
        """

        self._stage = -1
        self._enter_stage = []

        """
        角色素材
        """

        self._chara_images = {'yichen': [[], [], [], [], []]}
        for i in range(1, 12):
            self._chara_images['yichen'][0].append(pygame.image.load("images\\chara\\yichen\\idle_{}.png".format(i)))
        for i in range(1, 7):
            self._chara_images['yichen'][1].append(pygame.image.load("images\\chara\\yichen\\walk_{}.png".format(i)))
        for i in range(1, 9):
            self._chara_images['yichen'][2].append(pygame.image.load("images\\chara\\yichen\\attack_{}.png".format(i)))
        for i in range(1, 13):
            self._chara_images['yichen'][3].append(pygame.image.load("images\\chara\\yichen\\skill1_{}.png".format(i)))
        for i in range(1, 10):
            self._chara_images['yichen'][4].append(pygame.image.load("images\\chara\\yichen\\skill2_{}.png".format(i)))

        self._chara_images['jie'] = [[], [], [], [], []]
        for i in range(1, 7):
            self._chara_images['jie'][0].append(pygame.image.load("images\\chara\\jie\\idle_{}.png".format(i)))
        for i in range(1, 9):
            self._chara_images['jie'][1].append(pygame.image.load("images\\chara\\jie\\walk_{}.png".format(i)))
        for i in range(1, 6):
            self._chara_images['jie'][2].append(pygame.image.load("images\\chara\\jie\\attack_{}.png".format(i)))
        for i in range(1, 7):
            self._chara_images['jie'][3].append(pygame.image.load("images\\chara\\jie\\skill1_{}.png".format(i)))
        for i in range(1, 25):
            self._chara_images['jie'][4].append(pygame.image.load("images\\chara\\jie\\skill2_{}.png".format(i)))

        """
        角色攻击/技能偏移参数，用于调整图片显示位置
        """
        self._chara_attack_adjustment = {'yichen': [(-40, -27), (-40, -20), (-40, -27)],
                                         'yichen_reverse': [(-90, -27), (-75, -20), (-90, -27)],
                                         'jie': [(-10, -15), (-10, -15), (-15, -15)],
                                         'jie_reverse': [(-25, -15), (-40, -15), (-20, -15)]}

        """
        角色属性
        [速度, 攻速, 最大生命, 攻击力, 防御力, 技能冷却]
        """
        self._chara_stat = {'yichen': [3, 130, 20, 5, 2, [3500, 8000]],
                            'jie': [6, 100, 30, 3, 5, [4000, 10000]]}

        """
        特效素材
        """

        self._effect_images = {'fireball': [],
                               'wind': []}
        for i in range(1, 19):
            self._effect_images['fireball'].append(pygame.image.load("images\\effects\\fireball_{}.png".format(i)))
        for i in range(1, 18):
            self._effect_images['wind'].append(pygame.image.load("images\\effects\\wind_{}.png".format(i)))

        """
        精灵列表
        """
        self._all_sprites_list = pygame.sprite.LayeredUpdates()
        self._bullet_list = pygame.sprite.Group()
        self._monster_list = pygame.sprite.Group()
        self._item_list = pygame.sprite.Group()

    def next_stage(self):
        # 进入下一个阶段
        self._stage += 1
        # 记录阶段开始的时间
        self._enter_stage.append(pygame.time.get_ticks())
        debug("进入阶段{},当前时刻{}".format(self._stage, self._enter_stage[self._stage]), who=self.__class__.__name__)

    def init_stage(self):
        # 初始化阶段，在进入新窗口时使用
        self._stage = -1
        self._enter_stage = []
        debug("阶段初始化完成", type='success', who=self.__class__.__name__)

    def get_span(self):
        # 返回从进入阶段到现在的时间
        return pygame.time.get_ticks() - self._enter_stage[self._stage]

    def get_stage(self):
        # 返回当前阶段
        return self._stage

    def get_color(self, color):
        # 获取颜色
        color_rgb = (0, 0, 0)
        if color in self._colors.keys():
            color_rgb = self._colors.get(color)
        else:
            debug("请求的{}颜色不存在".format(color), type='error', who=self.__class__.__name__)
        return color_rgb

    def get_screen_size(self):
        # 获取屏幕尺寸
        return self._screen_size

    def get_chara_image(self, chara):
        # 获取角色素材
        chara_img = None
        if chara in self._chara_images.keys():
            chara_img = self._chara_images.get(chara)
        else:
            debug("请求的{}角色素材不存在".format(chara), type='error', who=self.__class__.__name__)
        return chara_img

    def get_effect_image(self, eff):
        # 获取特效素材
        eff_img = None
        if eff in self._effect_images.keys():
            eff_img = self._effect_images.get(eff)
        else:
            debug("请求的{}角色素材不存在".format(eff), type='error', who=self.__class__.__name__)
        return eff_img

    def add_sprite(self, sprite, layer):
        # 添加精灵到精灵列表
        self._all_sprites_list.add(sprite, layer=layer)

    def remove_sprite(self, sprite):
        # 从精灵列表移除精灵
        self._all_sprites_list.remove(sprite)

    def update_sprites(self, screen):
        # 更新精灵列表
        self._all_sprites_list.update(screen)

    def draw_sprites(self, screen):
        # 绘制精灵列表
        self._all_sprites_list.draw(screen)

    def add_bullet(self, sprite, layer):
        # 添加子弹到子弹列表
        self._bullet_list.add(sprite)
        self._all_sprites_list.add(sprite, layer=layer)

    def remove_bullet(self, sprite):
        # 从子弹列表移除子弹
        self._bullet_list.remove(sprite)
        self._all_sprites_list.remove(sprite)

    def get_bullet_list(self):
        # 返回子弹列表
        return self._bullet_list

    def add_monster(self, sprite):
        # 添加敌人到敌人列表
        self._monster_list.add(sprite)
        self._all_sprites_list.add(sprite, layer=2)

    def remove_monster(self, sprite):
        # 从敌人列表移除敌人
        self._monster_list.remove(sprite)
        self._all_sprites_list.remove(sprite)

    def get_monster_list(self):
        # 返回敌人列表
        return self._monster_list

    def get_attack_adjustment(self, hero_name, attack_index, reflect):
        # 获取攻击偏移参数
        if reflect:
            hero_name = hero_name + '_reverse'
        att_adj = self._chara_attack_adjustment.get(hero_name)[attack_index]
        return att_adj

    def get_chara_stat(self, hero_name, stat_index):
        return self._chara_stat[hero_name][stat_index]

    def bulletMech(self):
        enemy_hit_list = []
        (screen_w, screen_h) = self._screen_size
        for bullet in self._bullet_list:
            enemy_hit_list = pygame.sprite.spritecollide(bullet, self._monster_list, False)
            # Remove the bullet if it flies up off the screen
            if not 0 < bullet.rect.x < screen_w or not 0 < bullet.rect.y < screen_h and bullet.self_destroy:
                self.remove_bullet(bullet)
            for enemy in enemy_hit_list:
                # enemy.hp -= bullet.damage
                self.remove_bullet(bullet)


def init():
    global globles
    globles = Globles()


def show_text(screen, content: str, x, y, **kwargs):
    # 在主页面上显示文本

    # 可选参数
    # 颜色 默认 title_blue
    color = kwargs.get('color') if 'color' in kwargs.keys() else 'title_blue'
    color_rgb = globles.get_color(color)
    # 透明度 默认 255
    alpha = kwargs.get('alpha') if 'alpha' in kwargs.keys() else 255
    # 大小 默认 25
    size = kwargs.get('size') if 'size' in kwargs.keys() else 25
    # 是否加粗 默认 是
    is_bold = kwargs.get('bold') if 'bold' in kwargs.keys() else True
    # 是否斜体 默认 否
    is_italic = kwargs.get('italic') if 'italic' in kwargs.keys() else False

    # 字体 微软雅黑
    font = pygame.font.SysFont('Microsoft Yahei', size, is_bold, is_italic)

    # 文字渲染 抗锯齿开启
    text = font.render(content, True, color_rgb)

    # 设置文字透明度
    text.set_alpha(alpha)

    # 在屏幕上显示文字
    screen.blit(text, [x, y])


def next_stage():
    globles.next_stage()


def init_stage():
    globles.init_stage()


def get_span():
    return globles.get_span()


def get_stage():
    return globles.get_stage()


def get_color(color):
    return globles.get_color(color)


def get_screen_size():
    return globles.get_screen_size()


def get_chara_image(chara):
    return globles.get_chara_image(chara)


def add_sprite(sprite, layer=0):
    globles.add_sprite(sprite, layer)


def remove_sprite(sprite):
    globles.remove_sprite(sprite)


def update_sprites(screen):
    globles.update_sprites(screen)


def draw_sprites(screen):
    globles.draw_sprites(screen)


def get_attack_adjustment(hero_name, attack_index, reflect):
    return globles.get_attack_adjustment(hero_name, attack_index, reflect)


def get_chara_stat(hero_name, stat_index):
    return globles.get_chara_stat(hero_name, stat_index)


def add_bullet(bullet, layer=3):
    globles.add_bullet(bullet, layer)


def remove_bullet(bullet):
    globles.remove_bullet(bullet)


def get_bullet_list():
    return globles.get_bullet_list()


def get_monster_list():
    return globles.get_monster_list()


def bulletMech():
    globles.bulletMech()


def get_effect_image(eff):
    return globles.get_effect_image(eff)