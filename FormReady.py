import sys

import pygame
import Globles
import PygameObject
from debugOutp import debug

global form_ready


class FormReady:
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设定屏幕尺寸
        self.screen = pygame.display.set_mode(Globles.get_screen_size())

        # 设定页面标题
        pygame.display.set_caption("RomanticAdventure-Ready")

        # 设定时钟
        self.clock = pygame.time.Clock()

        # 是否完成
        self.done = False

        # 初始化阶段
        Globles.init_stage()

        # 英雄列表
        self.hero_list = ['yichen', 'jie']

        # 英雄的显示名
        self.hero_display_name = ['Yichen W.', 'Jie Z.']

        # 当前英雄序号
        self.hero_index = 0

        # 当前英雄名称
        self.hero_name = 'yichen'

        # 实例化英雄对象
        self.hero = PygameObject.Character('yichen', 30, 60)

        self.hero.skills_cd = [0, 0]

        # 添加英雄对象到精灵列表
        Globles.add_sprite(self.hero, 1)

        debug("准备页面初始化完成", type='success', who=self.__class__.__name__)

    def display_screen(self):

        debug("进入准备页面循环体", who=self.__class__.__name__)

        # 按钮尺寸
        button_dimension = [Globles.get_screen_size()[0] / 2, 400, 450, 30]

        PygameObject.spawn_enemy('stump', 300, 70)

        # 主循环体
        while not self.done:

            # 获取当前鼠标位置
            mouse = pygame.mouse.get_pos()

            # 事件循环处理
            for event in pygame.event.get():
                # 退出事件
                if event.type == pygame.QUIT:
                    debug("触发退出事件,当前时刻{}".format(pygame.time.get_ticks()), who=self.__class__.__name__)
                    self.done = True
                    sys.exit(0)
                # 按下键盘事件
                if event.type == pygame.KEYDOWN:
                    key_list = pygame.key.get_pressed()
                    # 按下H切换英雄，必须在非施法状态使用
                    if key_list[pygame.K_h] and self.hero.is_attacking == -1:
                        # 按顺序切换英雄，若是最后一个则回到第一个英雄
                        if self.hero_index < len(self.hero_list) - 1:
                            self.hero_index += 1
                        else:
                            self.hero_index = 0
                        # 更改当前英雄名称
                        self.hero_name = self.hero_list[self.hero_index]
                        # 从精灵列表移除当前英雄
                        Globles.remove_sprite(self.hero)
                        # 实例化新的英雄继承当前的朝向和位置
                        new_hero = PygameObject.Character(self.hero_name,
                                                          self.hero.rect.x,
                                                          self.hero.rect.y)
                        if self.hero.reflect:
                            new_hero.reflect = True
                        # 用新的英雄代替当前英雄
                        self.hero = new_hero
                        # 清除冷却时间
                        self.hero.skills_cd = [0, 0]
                        # 将新的英雄加入精灵列表
                        Globles.add_sprite(self.hero, 1)
                        debug("已将英雄切换为{}".format(self.hero_display_name[self.hero_index]), type='success',
                              who=self.__class__.__name__)
                    elif key_list[pygame.K_t]:
                        PygameObject.spawn_enemy('stump', self.hero.rect.x, 70)
                        debug("已生成新的木桩".format(self.hero_display_name[self.hero_index]), type='success',
                              who=self.__class__.__name__)
                # 点击鼠标
                if event.type == pygame.MOUSEBUTTONDOWN:
                    debug("触发鼠标点击事件,当前时刻{}".format(pygame.time.get_ticks()),
                          who=self.__class__.__name__)
                    if button_dimension[0] - button_dimension[2] / 2 < mouse[0] < button_dimension[0] + \
                            button_dimension[2] / 2 \
                            and button_dimension[1] - button_dimension[3] / 2 < mouse[1] < button_dimension[1] + \
                            button_dimension[3] / 2:
                        debug("鼠标点击继续按钮区域,当前时刻{}".format(pygame.time.get_ticks()),
                              who=self.__class__.__name__)
                        if self.hero_index == 0:
                            Globles.set_protagonist(1)
                        elif self.hero_index == 1:
                            Globles.set_protagonist(3)
                        self.done = True

            # 准备页面背景
            self.screen.fill(Globles.get_color('white'))

            # 准备页面文本显示
            # 操作教程
            Globles.show_text(self.screen, "Select and try your Hero!", 20, 10, bold=False, size=20, color='black')
            Globles.show_text(self.screen, "HIT ME!", 290, 40, size=20, color='black')
            Globles.show_text(self.screen, "Press A and D to walk, "
                                           "Press J to attack, "
                                           "Press I and O to use skills", 20, 160, bold=False, size=20, color='black')
            # 当前英雄
            Globles.show_text(self.screen, "Press H to switch Hero, Current Hero: {}".format(
                self.hero_display_name[self.hero_index]),
                              20, 190, bold=False, size=20, color='black')
            # 速度，移速，最大生命值
            Globles.show_text(self.screen, "Speed: {:.1f} Attack Speed: {:.2f} Max HP: {:.1f}".format(self.hero.speed,
                                                                                                      200 / self.hero.attack_speed,
                                                                                                      self.hero.max_hp),
                              20, 250, bold=False, size=20, color='black')
            # 攻击力，防御力
            Globles.show_text(self.screen, "Attack: {:.1f} Defence: {:.1f}".format(self.hero.attack,
                                                                                   self.hero.defence),
                              20, 280, bold=False, size=20, color='black')

            # 继续按钮
            if button_dimension[0] - button_dimension[2] / 2 < mouse[0] < button_dimension[0] + button_dimension[2] / 2 \
                    and button_dimension[1] - button_dimension[3] / 2 < mouse[1] < button_dimension[1] + \
                    button_dimension[3] / 2:
                Globles.show_text(self.screen,
                                  "Click to Continue with {}".format(self.hero_display_name[self.hero_index]),
                                  button_dimension[0], button_dimension[1], size=30, color='title_red', middle=True)
            else:
                Globles.show_text(self.screen,
                                  "Click to Continue with {}".format(self.hero_display_name[self.hero_index]),
                                  button_dimension[0], button_dimension[1], size=30, middle=True)

            # 更新精灵列表
            Globles.update_sprites(self.screen)
            # 子弹物理计算
            PygameObject.bulletMech()
            # 在屏幕上绘制精灵列表
            Globles.draw_sprites(self.screen)
            # 更新文本
            Globles.update_texts(self.screen)

            # 更新页面
            pygame.display.flip()

            # 设定页面更新速率
            self.clock.tick(60)

        # 关闭页面
        Globles.remove_sprite(self.hero)
        for enemy in Globles.get_monster_list():
            Globles.remove_monster(enemy)
        Globles.next_wave()
        pygame.quit()
        debug("准备页面播放完成", type='success', who=self.__class__.__name__)


def init():
    # 初始化准备页面
    global form_ready
    form_ready = FormReady()


def display():
    # 显示准备页面
    form_ready.display_screen()
