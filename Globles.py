# 全局变量和函数
import pygame
import sys
import pathlib
from debugOutp import debug

global globles

is_debug = False


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
                        'title_red': (254, 225, 232),
                        'orange': (255, 128, 0),
                        'purple': (128, 0, 255)}

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
        self._chara_path = pathlib.Path.cwd() / "images/chara"

        self._chara_images = {'yichen': [[], [], [], [], []]}
        for i in range(1, 12):
            self._chara_images['yichen'][0].append(pygame.image.load(self._chara_path / "yichen/idle_{}.png".format(i)))
        for i in range(1, 7):
            self._chara_images['yichen'][1].append(pygame.image.load(self._chara_path / "yichen/walk_{}.png".format(i)))
        for i in range(1, 9):
            self._chara_images['yichen'][2].append(
                pygame.image.load(self._chara_path / "yichen/attack_{}.png".format(i)))
        for i in range(1, 13):
            self._chara_images['yichen'][3].append(
                pygame.image.load(self._chara_path / "yichen/skill1_{}.png".format(i)))
        for i in range(1, 10):
            self._chara_images['yichen'][4].append(
                pygame.image.load(self._chara_path / "yichen/skill2_{}.png".format(i)))

        self._chara_images['jie'] = [[], [], [], [], []]
        for i in range(1, 7):
            self._chara_images['jie'][0].append(pygame.image.load(self._chara_path / "jie/idle_{}.png".format(i)))
        for i in range(1, 9):
            self._chara_images['jie'][1].append(pygame.image.load(self._chara_path / "jie/walk_{}.png".format(i)))
        for i in range(1, 6):
            self._chara_images['jie'][2].append(pygame.image.load(self._chara_path / "jie/attack_{}.png".format(i)))
        for i in range(1, 7):
            self._chara_images['jie'][3].append(pygame.image.load(self._chara_path / "jie/skill1_{}.png".format(i)))
        for i in range(1, 25):
            self._chara_images['jie'][4].append(pygame.image.load(self._chara_path / "jie/skill2_{}.png".format(i)))

        """
        角色攻击/技能偏移参数，用于调整图片显示位置
        """
        self._chara_attack_adjustment = {'yichen': [(-40, -27), (-40, -20), (-40, -27)],
                                         'yichen_reverse': [(-90, -27), (-75, -20), (-90, -27)],
                                         'jie': [(-10, -15), (-10, -15), (-15, -15)],
                                         'jie_reverse': [(-25, -15), (-40, -15), (-20, -15)]}

        """
        角色属性
        [速度, 攻速, 最大生命, 攻击力, 防御力, 技能冷却, 攻击距离, 技能倍率]
        """
        self._chara_stat = {'yichen': [3, 130, 20, 5, 2, [12000, 20000], [100, 70, 90], [1, 1, 3]],
                            'jie': [6, 100, 30, 2, 5, [10000, 25000], [25, 0, 0], [1, 3, 7.5]]}

        """
        敌人属性
        [速度, 最大生命, 攻击力, 防御力]
        """
        self._enemy_stat = {'bat': [2, 5, 1, 1],
                            'scorpion': [1, 10, 2, 2],
                            'stump': [0, 200, 0, 0]}

        """
        敌人素材
        """

        self._enemy_path = pathlib.Path.cwd() / "images/enemy"
        self._enemy_images = {'butterfly': [[]]}
        for i in range(1, 4):
            self._enemy_images['butterfly'][0].append(
                pygame.image.load(self._enemy_path / "butterfly_{}.png".format(i)))

        self._enemy_images['cat'] = [[]]
        for i in range(1, 4):
            self._enemy_images['cat'][0].append(pygame.image.load(self._enemy_path / "cat_{}.png".format(i)))

        self._enemy_images['chicken'] = [[]]
        for i in range(1, 4):
            self._enemy_images['chicken'][0].append(pygame.image.load(self._enemy_path / "chicken_{}.png".format(i)))

        self._enemy_images['cow'] = [[]]
        for i in range(1, 4):
            self._enemy_images['cow'][0].append(pygame.image.load(self._enemy_path / "cow_{}.png".format(i)))

        self._enemy_images['dog'] = [[]]
        for i in range(1, 4):
            self._enemy_images['dog'][0].append(pygame.image.load(self._enemy_path / "dog_{}.png".format(i)))

        self._enemy_images['horse'] = [[]]
        for i in range(1, 4):
            self._enemy_images['horse'][0].append(pygame.image.load(self._enemy_path / "horse_{}.png".format(i)))

        self._enemy_images['sheep'] = [[]]
        for i in range(1, 4):
            self._enemy_images['sheep'][0].append(pygame.image.load(self._enemy_path / "sheep_{}.png".format(i)))

        self._enemy_images['bat'] = [[]]
        for i in range(1, 4):
            self._enemy_images['bat'][0].append(pygame.image.load(self._enemy_path / "bat_{}.png".format(i)))

        self._enemy_images['scorpion'] = [[]]
        for i in range(1, 4):
            self._enemy_images['scorpion'][0].append(pygame.image.load(self._enemy_path / "scorpion_{}.png".format(i)))

        self._enemy_images['stump'] = [[]]
        for i in range(1, 10):
            self._enemy_images['stump'][0].append(pygame.image.load(self._enemy_path / "stump_{}.png".format(i)))

        """
        特效素材
        """
        self._effect_path = pathlib.Path.cwd() / "images/effects"
        self._effect_images = {'fireball': [],
                               'wind': [],
                               'purify': [],
                               'explosion': []}
        for i in range(1, 19):
            self._effect_images['fireball'].append(pygame.image.load(self._effect_path / "fireball_{}.png".format(i)))
        for i in range(1, 18):
            self._effect_images['wind'].append(pygame.image.load(self._effect_path / "wind_{}.png".format(i)))
        for i in range(1, 4):
            self._effect_images['purify'].append(pygame.image.load(self._effect_path / "purify_{}.png".format(i)))
        for i in range(1, 11):
            self._effect_images['explosion'].append(pygame.image.load(self._effect_path / "explosion_{}.png".format(i)))

        """
        背景素材
        """
        self._background_path = pathlib.Path.cwd() / "images/background"
        self._background_images = {'bg': pygame.image.load(self._background_path / "bg.png"),
                                   'bg_2': pygame.image.load(self._background_path / "bg_2.png"),
                                   'forestleft': [
                                       pygame.image.load(self._background_path / "forestleft_{}.png".format(i)) for i in
                                       range(1, 5)
                                   ],
                                   'forestright': [
                                       pygame.image.load(self._background_path / "forestright_{}.png".format(i)) for i
                                       in range(1, 5)
                                   ],
                                   'treeleft': [
                                       pygame.image.load(self._background_path / "treeleft_{}.png".format(i)) for i
                                       in range(1, 9)
                                   ],
                                   'treeright': [
                                       pygame.image.load(self._background_path / "treeright_{}.png".format(i)) for i
                                       in range(1, 9)
                                   ],
                                   'fountain': [
                                       pygame.image.load(self._background_path / "fountain_{}.png".format(i)) for i
                                       in range(1, 13)
                                   ],
                                   'fountainnight': [
                                       pygame.image.load(self._background_path / "fountainnight_{}.png".format(i)) for i
                                       in range(1, 5)
                                   ],
                                   'palace': [
                                       pygame.image.load(self._background_path / "palace_{}.png".format(i)) for i
                                       in range(1, 17)
                                   ],
                                   }

        """
        状态素材
        """
        self._buff_path = pathlib.Path.cwd() / "images/buff"
        self._buff_name_list = ['yichen_skill_1', 'yichen_skill_2', 'jie_skill_1', 'jie_skill_2',
                                'yichen_skill_1_cd', 'yichen_skill_2_cd', 'jie_skill_1_cd', 'jie_skill_2_cd',
                                'attack', 'attack_cd',
                                'atk_up', 'mhp_up', 'def_up', 'agi_up',
                                'atk_down', 'mhp_down', 'def_down', 'agi_down',
                                'heal', 'poison',
                                'yin', 'yang',
                                'unknown']
        self._buff_images = {}
        for buff_name in self._buff_name_list:
            self._buff_images[buff_name] = pygame.image.load(self._buff_path / "{}.png".format(buff_name))

        """
        精灵列表
        子弹列表
        
        
        
        
        """
        self._all_sprites_list = pygame.sprite.LayeredUpdates()
        self._bullet_list = pygame.sprite.Group()
        self._monster_list = pygame.sprite.Group()
        self._item_list = pygame.sprite.Group()

        """
        人物名称列表
        """
        self._chara_names = {'zh': ["角色",
                                    "王奕辰",
                                    "侯申然",
                                    "张杰",
                                    "Nana",
                                    "理塘顶真一郎",
                                    "麦克肯威"],
                             'en': ["Character",
                                    "Yichen W",
                                    "Shenran H",
                                    "Jie Z",
                                    "Nana",
                                    "LTDZ",
                                    "MacKenway"]}

        self._protagonist = 1

        """
        战斗阶段
        _is_battle 战斗状态 0:未开始 1:进行中 2:已结束
        """
        self._is_battle = 0
        self._remain_enemies = 0
        self._current_wave = 0

        """
        可移动区域
        """
        self._movable_l = 0
        self._movable_r = 700

        """
        英雄复苏及助战
        """
        self._is_defeated = False
        self._assist_left = 1
        self._last_wave = -1

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
            debug("请求的名为\"{}\"的颜色不存在".format(color), type='error', who=self.__class__.__name__)
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
            debug("请求的名为\"{}\"的角色素材不存在".format(chara), type='error', who=self.__class__.__name__)
        return chara_img

    def get_enemy_image(self, enemy_name):
        # 获取敌人素材
        enemy_img = None
        if enemy_name in self._enemy_images.keys():
            enemy_img = self._enemy_images.get(enemy_name)
        else:
            debug("请求的名为\"{}\"的敌人素材不存在".format(enemy_name), type='error', who=self.__class__.__name__)
        return enemy_img

    def get_effect_image(self, eff):
        # 获取特效素材
        eff_img = None
        if eff in self._effect_images.keys():
            eff_img = self._effect_images.get(eff)
        else:
            debug("请求的名为\"{}\"的特效素材不存在".format(eff), type='error', who=self.__class__.__name__)
        return eff_img

    def get_background_image(self, bg):
        # 获取背景素材
        bg_img = None
        if bg in self._background_images.keys():
            bg_img = self._background_images.get(bg)
        else:
            debug("请求的名为\"{}\"的背景素材不存在".format(bg), type='error', who=self.__class__.__name__)
        # 判断是否为动态背景
        if isinstance(bg_img, list):
            bg_img = bg_img[get_span() // 100 % len(bg_img)]
        return bg_img

    def get_buff_image(self, buff_name):
        # 获取背景素材
        buff_img = self._buff_images['unknown']
        if buff_name in self._buff_images.keys():
            buff_img = self._buff_images.get(buff_name)
        else:
            debug("请求的名为\"{}\"的状态素材不存在".format(buff_name), type='error', who=self.__class__.__name__)
        return buff_img

    def add_sprite(self, sprite, layer):
        # 添加精灵到精灵列表
        self._all_sprites_list.add(sprite, layer=layer)
        debug("成功在第{}层添加精灵{}({})".format(layer, sprite.name, sprite.type), type='success',
              who=self.__class__.__name__)

    def remove_sprite(self, sprite):
        # 从精灵列表移除精灵
        self._all_sprites_list.remove(sprite)
        debug("成功移除精灵{}({})".format(sprite.name, sprite.type), type='success', who=self.__class__.__name__)

    def update_sprites(self, screen):
        # 更新精灵列表
        self._all_sprites_list.update(screen)

    def draw_sprites(self, screen):
        # 绘制精灵列表
        self._all_sprites_list.draw(screen)

    def add_bullet(self, sprite, layer):
        # 添加子弹到子弹列表
        debug("成功添加子弹/特效: {}".format(sprite.name), type='success', who=self.__class__.__name__)
        self._bullet_list.add(sprite)
        self._all_sprites_list.add(sprite, layer=layer)

    def remove_bullet(self, sprite):
        # 从子弹列表移除子弹
        debug("成功移除子弹/特效: {}".format(sprite.name), type='success', who=self.__class__.__name__)
        self._bullet_list.remove(sprite)
        self._all_sprites_list.remove(sprite)

    def get_bullet_list(self):
        # 返回子弹列表
        return self._bullet_list

    def add_monster(self, sprite):
        # 添加敌人到敌人列表
        debug("成功添加敌人: {}".format(sprite.name), type='success', who=self.__class__.__name__)
        self._monster_list.add(sprite)
        self._all_sprites_list.add(sprite, layer=2)
        self._remain_enemies += 1
        if not self._is_battle:
            self.start_battle()

    def remove_monster(self, sprite):
        # 从敌人列表移除敌人
        debug("成功移除敌人: {}".format(sprite.name), type='success', who=self.__class__.__name__)
        self._monster_list.remove(sprite)
        self._all_sprites_list.remove(sprite)
        self._remain_enemies -= 1
        if self._remain_enemies == 0:
            self.end_battle()

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
        # 获取角色属性
        if hero_name in self._chara_stat.keys():
            chara_stat = self._chara_stat.get(hero_name)
        else:
            debug("请求的名为\"{}\"的角色属性不存在".format(hero_name), type='error', who=self.__class__.__name__)
            return None
        return chara_stat[stat_index]

    def get_chara_name(self, role, lang):
        if role == "prot":
            # 返回主角的名字
            return self._chara_names[lang][self._protagonist]
        elif role == "anta":
            # 返回大反派的名字
            return self._chara_names[lang][5]
        elif role == "couple":
            """
            1 -> 2 
            2 -> 1
            3 -> 4
            4 -> 3
            反正就是返回各自的对象啦~
            """
            return self._chara_names[lang][
                (self._protagonist + 1) if self._protagonist % 2 == 1 else (self._protagonist - 1)]
        elif role == "friend":
            """
            1 -> 3
            2 -> 4
            3 -> 1
            4 -> 2
            返回各自的同性朋友
            """
            return self._chara_names[lang][
                (self._protagonist + 2) if self._protagonist <= 2 else (self._protagonist - 2)]
        elif role == "friend_cp":
            """
            1 -> 4
            2 -> 3
            3 -> 2
            4 -> 1
            返回各自异性朋友的对象
            """
            return self._chara_names[lang][5 - self._protagonist]
        elif role == "place":
            # 返回故事发生的地方
            return self._chara_names[lang][6]

    def set_protagonist(self, prot):
        # 设置故事的主角
        self._protagonist = prot
        debug("已将故事主角设置为{}({})".format(self._chara_names['zh'][prot], self._chara_names['en'][prot]),
              type='success', who=self.__class__.__name__)

    def get_protagonist(self):
        # 返回故事的主角
        return self._protagonist

    def add_buff(self, sprite, buff_name, last_time, coefficient):
        # 为精灵添加Buff
        # 检测精灵对象是否可以添加Buff
        if sprite.type not in ['character', 'enemy']:
            debug("为对象{}添加Buff失败: 种类为{}的对象不可添加Buff".format(sprite.name, sprite.type),
                  type='error', who=self.__class__.__name__)
            return
        if buff_name not in self._buff_name_list:
            debug("为对象{}添加Buff失败: 名称为{}的Buff不存在".format(sprite.name, buff_name),
                  type='error', who=self.__class__.__name__)
            return
        if last_time == -1:
            sprite.buff_list[buff_name] = (True, coefficient)
            last_time = "∞"
        else:
            sprite.buff_list[buff_name] = (pygame.time.get_ticks() + last_time * 1000, coefficient)
        debug("成功为对象{}添加名称为{}的Buff, 持续时间{}s, 倍率系数{}".format(
            sprite.name,
            buff_name,
            last_time,
            coefficient),
            type='success', who=self.__class__.__name__)

    def get_enemy_stat(self, enemy_name, stat_index):
        # 获取敌人属性
        if enemy_name in self._enemy_stat.keys():
            enemy_stat = self._enemy_stat.get(enemy_name)
        else:
            debug("请求的名为\"{}\"的敌人属性不存在".format(enemy_name), type='error', who=self.__class__.__name__)
            return None
        return enemy_stat[stat_index]

    def get_battle_state(self):
        # 获取当前战斗状态
        return self._is_battle

    def start_battle(self):
        # 开始一场战斗
        if self._is_battle == 0:
            self._is_battle = 1
            debug("已开始一场战斗!当前波次{}".format(self._current_wave), type='success', who=self.__class__.__name__)
        elif self._is_battle == 2:
            self._is_battle = 1
            debug("已重新开始一场战斗!当前波次{}".format(self._current_wave), type='success',
                  who=self.__class__.__name__)
        else:
            debug("战斗阶段正在进行中!当前波次{}".format(self._current_wave), type='error', who=self.__class__.__name__)

    def get_remain_enemies(self):
        # 获取剩余敌人数量
        return self._remain_enemies

    def get_current_wave(self):
        # 获取当前波次
        return self._current_wave

    def end_battle(self):
        # 结束当前战斗
        self._is_battle = 2
        debug("已结束当前战斗, 当前波次{}".format(self._current_wave), type='info', who=self.__class__.__name__)

    def next_wave(self):
        # 下一波次
        self._is_battle = 0
        self._current_wave += 1
        debug("已进入波次{}".format(self._current_wave), type='info', who=self.__class__.__name__)

    def set_movable_area(self, left, right):
        self._movable_l = left
        self._movable_r = right
        debug("已将可移动区域设置为({}, {})".format(left, right), type='info', who=self.__class__.__name__)

    def get_movable_area(self):
        return self._movable_l, self._movable_r

    def get_all_sprites(self):
        return self._all_sprites_list

    def hero_defeat(self):
        self._is_defeated = True
        titles.clear()
        self._last_wave = self._current_wave
        TitleText("英雄已倒下···", "Hero Defeated", "red", 40)
        TitleText("按R复苏并重新挑战本关", "Press R to revive and reset the level", "orange", 30)
        TitleText("按F召唤{}助战".format(get_chara_name("friend", "zh")),
                  "Press F to summon {} to assist you".format(get_chara_name("friend", "en")),
                  "orange", 30)

    def is_defeated(self):
        return self._is_defeated

    def revive_hero(self):
        self._current_wave = self._last_wave - 1
        title_pool.clear()
        titles.clear()
        for monster in self._monster_list:
            remove_monster(monster)
        TitleText("英雄已复苏！", "Hero Revived", "red", 40)


# 标题池和悬浮文字池
title_pool = []
titles = []
float_texts = []


class TitleText:
    # 展示闪烁标题
    def __init__(self, text_zh, text_en, color, size=50):
        self.text_zh = text_zh
        self.text_en = text_en
        self.color = color
        self.alpha = 0
        self.size = size
        self.reverse = False
        title_pool.append(text_zh)
        titles.append(self)
        debug("显示标题文字:{}({})".format(text_zh, text_en), type='success', who='Globles')

    def update(self, screen) -> None:
        show_text(screen,
                  self.text_zh,
                  get_screen_size()[0] / 2, 140,
                  color=self.color,
                  alpha=self.alpha, size=self.size, middle=True)
        show_text(screen,
                  self.text_en,
                  get_screen_size()[0] / 2, 150 + self.size,
                  color=self.color,
                  alpha=self.alpha, size=self.size, middle=True)
        if not self.reverse:
            self.alpha += 3
            if self.alpha > 500:
                self.reverse = True
        if self.reverse:
            self.alpha -= 3
        if self.alpha < 0:
            titles.remove(self)
            del self


class FloatText:
    # 展示悬浮文字
    def __init__(self, text, color, x, y, alpha=255):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.alpha = alpha
        self.reverse = False
        float_texts.append(self)
        debug("在({}, {})显示悬浮文字:{}".format(x, y, text), type='success', who='Globles')

    def update(self, screen):
        if not self.reverse:
            self.alpha += 3
            if self.alpha >= 255:
                self.reverse = True
        if self.reverse:
            show_text(screen, self.text, self.x, self.y, color=self.color, size=20, middle=True, alpha=self.alpha)
            self.alpha -= 3
            self.y -= 1
        if self.alpha < 0:
            float_texts.remove(self)
            del self


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
    # 是否按坐标居中 默认 否
    is_middle = kwargs.get('middle') if 'middle' in kwargs.keys() else False

    # 字体 微软雅黑
    if sys.platform == 'win32':
        font = pygame.font.SysFont('Microsoft Yahei', size, is_bold)
    else:
        if is_bold:
            font = pygame.font.Font('fonts/Yahei_Bold.ttf', size)
        else:
            font = pygame.font.Font('fonts/Yahei.ttf', size)

    # 文字渲染 抗锯齿开启
    text = font.render(content, True, color_rgb)

    # 设置文字透明度
    text.set_alpha(alpha)

    # 在屏幕上显示文字
    text_rect = [x, y]
    if is_middle:
        text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


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


def get_effect_image(eff):
    return globles.get_effect_image(eff)


def get_background_image(bg):
    return globles.get_background_image(bg)


def get_chara_name(role, lang='en'):
    return globles.get_chara_name(role, lang)


def set_protagonist(prog):
    globles.set_protagonist(prog)


def get_buff_image(buff_name):
    return globles.get_buff_image(buff_name)


def get_protagonist():
    return globles.get_protagonist()


def add_buff(sprite, buff_name, last_time, coefficient=1):
    globles.add_buff(sprite, buff_name, last_time, coefficient)


def get_enemy_stat(enemy_name, stat_index):
    if stat_index != 0:
        stat_index -= 1
    return globles.get_enemy_stat(enemy_name, stat_index)


def get_enemy_image(enemy_name):
    return globles.get_enemy_image(enemy_name)


def add_monster(monster):
    globles.add_monster(monster)


def remove_monster(monster):
    globles.remove_monster(monster)


def get_battle_state():
    return globles.get_battle_state()


def get_remain_enemies():
    return globles.get_remain_enemies()


def get_current_wave():
    return globles.get_current_wave()


def next_wave():
    globles.next_wave()
    remove_all_purified()


def update_texts(screen):
    # 更新标题文本和悬浮文本
    if len(titles) > 0:
        titles[0].update(screen)
    for float_text in float_texts:
        float_text.update(screen)


def set_movable_area(left, right):
    globles.set_movable_area(left, right)


def get_movable_area():
    return globles.get_movable_area()


def remove_all_purified():
    sprites_list = globles.get_all_sprites()
    for sprite in sprites_list:
        if sprite.type == 'purified_enemy':
            globles.remove_sprite(sprite)
    debug("已移除所有净化的敌人", type='success', who='Globles')


def hero_defeat():
    globles.hero_defeat()


def is_defeated():
    return globles.is_defeated()


def revive_hero():
    globles.revive_hero()
