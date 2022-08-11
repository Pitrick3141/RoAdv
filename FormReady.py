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

        self.hero_list = ['yichen', 'jie']
        self.hero_display_name = ['Yichen W.', 'Jie Z.']
        self.hero_index = 0
        self.hero_name = 'yichen'

        self.hero = PygameObject.Character('yichen', 30, 60)

        Globles.add_sprite(self.hero)

        debug("准备页面初始化完成", type='success', who=self.__class__.__name__)

    def display_screen(self):

        debug("进入准备页面循环体", who=self.__class__.__name__)

        # 主循环体
        while not self.done:
            # 事件循环处理
            for event in pygame.event.get():
                # 退出程序
                if event.type == pygame.QUIT:
                    debug("触发退出事件,当前时刻{}".format(pygame.time.get_ticks()), who=self.__class__.__name__)
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    key_list = pygame.key.get_pressed()
                    if key_list[pygame.K_h] and not self.hero.is_attacking:
                        if self.hero_index < len(self.hero_list) - 1:
                            self.hero_index += 1
                        else:
                            self.hero_index = 0
                        self.hero_name = self.hero_list[self.hero_index]
                        Globles.remove_sprite(self.hero)
                        new_hero = PygameObject.Character(self.hero_name,
                                                          self.hero.rect.x,
                                                          self.hero.rect.y)
                        if self.hero.reflect:
                            new_hero.reflect = True
                        self.hero = new_hero
                        Globles.add_sprite(self.hero)
                        debug("已将英雄切换为{}".format(self.hero_display_name[self.hero_index]), type='success',
                              who=self.__class__.__name__)

            # 主页面背景
            self.screen.fill(Globles.get_color('white'))

            Globles.show_text(self.screen, "Select and try your Hero!", 20, 10, bold=False, size=20, color='black')
            Globles.show_text(self.screen, "Press A and D to walk, Press J to attack", 20, 160, bold=False, size=20,
                              color='black')
            Globles.show_text(self.screen, "Press H to switch Hero, Current Hero: {}".format(
                self.hero_display_name[self.hero_index]),
                              20, 190, bold=False, size=20, color='black')
            Globles.show_text(self.screen, "Speed: {} Attack Speed: {} Max HP: {}".format(self.hero.speed,
                                                                                          self.hero.attack_speed,
                                                                                          self.hero.max_hp),
                              20, 250, bold=False, size=20, color='black')
            Globles.show_text(self.screen, "Attack: {} Defence: {}".format(self.hero.attack,
                                                                           self.hero.defence),
                              20, 280, bold=False, size=20, color='black')

            Globles.update_sprites(self.screen)

            Globles.draw_sprites(self.screen)

            # 更新页面
            pygame.display.flip()

            # 设定页面更新速率
            self.clock.tick(60)

        # 关闭页面
        debug("准备页面播放完成", type='success', who=self.__class__.__name__)
        pygame.quit()


def init():
    # 初始化准备页面
    global form_ready
    form_ready = FormReady()


def display():
    # 显示准备页面
    form_ready.display_screen()
