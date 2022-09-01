import random
import sys
import pygame
import Globles
import PygameObject
from debugOutp import debug

global form_game


class FormGame:
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设定屏幕尺寸
        self.screen = pygame.display.set_mode(Globles.get_screen_size())

        # 设定页面标题
        pygame.display.set_caption("RomanticAdventure")

        # 设定时钟
        self.clock = pygame.time.Clock()

        # 是否完成
        self.done = False

        # 剩余敌人数量
        self.enemy_cnt = 0

        # 初始化阶段
        Globles.init_stage()

        debug("游戏页面初始化完成", type='success', who=self.__class__.__name__)

    def display_screen(self):

        debug("进入游戏页面循环体", who=self.__class__.__name__)
        Globles.next_stage()

        # 背景文本列表
        about_texts_en = ["A Long, Long Time ago",
                          "There was a small town called {}".format(Globles.get_chara_name('place')),
                          "People all lived happily in the town",
                          "However,",
                          "one day the evil {} came to the town".format(Globles.get_chara_name('anta')),
                          "He Spread his terrible curse all over the town",
                          "All people cursed became weak and pale,",
                          "which includes {} and {}".format(Globles.get_chara_name('couple'),
                                                            Globles.get_chara_name('friend_cp')),
                          "What's even worse,",
                          "The animals around the town are affected",
                          "and transferred into terrible monsters",
                          "The guardian of the town, {}".format(Globles.get_chara_name('prot')),
                          "and the best teammate, {}".format(Globles.get_chara_name('friend')),
                          "set off to save {}".format(Globles.get_chara_name('place')),
                          "The curse that {} and {} suffered from".format(Globles.get_chara_name('couple'),
                                                                          Globles.get_chara_name('friend_cp')),
                          "can only be removed by defeating {}".format(Globles.get_chara_name('anta'))]

        about_texts_zh = ["很久，很久以前",
                          "有一座叫做{}的小镇".format(Globles.get_chara_name('place', 'zh')),
                          "小镇的居民全都安居乐业",
                          "然而，",
                          "一天邪恶的{}来到了镇上".format(Globles.get_chara_name('anta', 'zh')),
                          "他向整个小镇散播了他可怕的诅咒",
                          "中了诅咒的人变得虚弱无力，",
                          "这其中就包括了{}和{}".format(
                              Globles.get_chara_name('couple', 'zh'),
                              Globles.get_chara_name('friend_cp', 'zh')),
                          "更糟糕的是,",
                          "小镇附近的动物都被邪恶力量控制",
                          "变成了可怕的魔物",
                          "小镇的守护者{}".format(Globles.get_chara_name('prot', 'zh')),
                          "和最棒的队友{}".format(Globles.get_chara_name('friend', 'zh')),
                          "踏上了拯救{}的旅程".format(Globles.get_chara_name('place', 'zh')),
                          "只有击败{}".format(Globles.get_chara_name('anta', 'zh')),
                          "才能解除{}和{}身上的诅咒".format(
                              Globles.get_chara_name('couple', 'zh'),
                              Globles.get_chara_name('friend_cp', 'zh'))]

        # 当前显示的背景文本序号
        about_index = 0
        # 用于背景文本动画的参数
        about_reverse = 0
        about_alpha = 0
        about_speed = 2

        # 当前的背景序号
        bg_index = 0
        # 背景列表
        bg_list = ['bg', 'bg_2', 'forestleft', 'forestright']

        # 英雄列表
        hero_list = ['none', 'yichen', 'shenran', 'jie', 'yinuo']

        # 实例化英雄对象
        hero = PygameObject.Character(hero_list[Globles.get_protagonist()], 30, 180)

        # 添加英雄对象到精灵列表
        Globles.add_sprite(hero, 1)

        while not self.done:
            # 事件循环处理
            for event in pygame.event.get():
                # 退出程序
                if event.type == pygame.QUIT:
                    debug("触发退出事件,当前时刻{}".format(pygame.time.get_ticks()), who=self.__class__.__name__)
                    self.done = True
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    key_list = pygame.key.get_pressed()
                    # 按下Q跳过剧情
                    if key_list[pygame.K_q] and Globles.get_stage() == 0:
                        Globles.next_stage()
                        about_reverse = 0
                        about_alpha = 0
                        debug("已跳过剧情", type='info', who=self.__class__.__name__)
                        bg_index = 2
                    if key_list[pygame.K_LCTRL] or key_list[pygame.K_RCTRL]:
                        if about_speed == 2:
                            about_speed = 4
                            debug("剧情播放速度2x", type='info', who=self.__class__.__name__)
                        elif about_speed == 4:
                            about_speed = 8
                            debug("剧情播放速度4x", type='info', who=self.__class__.__name__)
                        else:
                            about_speed = 2
                            debug("剧情播放速度1x", type='info', who=self.__class__.__name__)

            bg = Globles.get_background_image(bg_list[bg_index])
            bg = pygame.transform.scale(bg, Globles.get_screen_size())
            self.screen.blit(bg, (0, 0))

            if Globles.get_stage() == 0:
                if about_index == 4:
                    text_color = 'red'
                    text_shake_x = 0
                    text_shake_y = 0
                elif about_index == 5 or about_index == 10:
                    text_color = 'red'
                    text_shake_x = random.randint(-5, 5)
                    text_shake_y = random.randint(-3, 3)
                else:
                    text_color = 'black'
                    text_shake_x = 0
                    text_shake_y = 0
                Globles.show_text(self.screen,
                                  about_texts_en[about_index],
                                  Globles.get_screen_size()[0] / 2 + text_shake_x, 180 + text_shake_y,
                                  color=text_color, alpha=about_alpha, size=25, middle=True)
                Globles.show_text(self.screen,
                                  about_texts_zh[about_index],
                                  Globles.get_screen_size()[0] / 2 + text_shake_x, 140 + text_shake_y,
                                  color=text_color, alpha=about_alpha, size=30, middle=True)
                if about_reverse == 0:
                    about_alpha += 3
                    if about_alpha > 255:
                        about_reverse = -1
                elif about_alpha > 255:
                    about_reverse = -1
                    about_alpha = 255
                elif about_alpha < 0:
                    about_reverse = 1
                    about_alpha = 0
                    if about_index < len(about_texts_en) - 1:
                        about_index += 1
                        if bg_index == 0 and about_index == 5:
                            bg_index = 1
                    else:
                        # 完成一次循环
                        Globles.next_stage()
                        about_reverse = 0
                        about_alpha = 0
                        bg_index = 2
                about_alpha += about_speed * about_reverse
                Globles.show_text(self.screen, "按Q跳过剧情, 按Ctrl加速剧情", 20, 450,
                                  color='black', alpha=about_alpha, size=15, bold=False)
                Globles.show_text(self.screen, "Press Q to Skip, Press Ctrl to Speed UP", 20, 470,
                                  color='black', alpha=about_alpha, size=15, bold=False)
                if about_speed == 4:
                    Globles.show_text(self.screen, "2X>>", 550, 20,
                                      color='red', alpha=about_alpha, size=25)
                elif about_speed == 8:
                    Globles.show_text(self.screen, "4X>>>>", 550, 20,
                                      color='red', alpha=about_alpha, size=25)
            elif Globles.get_stage() == 1:
                if bg_index == 2:
                    if "序章" not in Globles.title_pool:
                        Globles.TitleText("序章", "Prologue", 'black')
                        Globles.TitleText("0-1", "", 'black')
                    if Globles.get_battle_state() == 0:
                        Globles.set_movable_area(0, 680)
                        PygameObject.spawn_enemy('bat', 250, 180)
                    if Globles.get_battle_state() == 2:
                        if "完成" not in Globles.title_pool:
                            Globles.titles.clear()
                            Globles.TitleText("完成", "Finished", 'orange')
                        if hero.rect.x > 620:
                            bg_index = 3
                            hero.rect.x = 80
                            Globles.next_wave()
                            Globles.title_pool.remove("完成")
                elif bg_index == 3:
                    for enemy in Globles.get_monster_list():
                        if enemy.rect.x > 300:
                            enemy.reflect = True
                        if enemy.rect.x < 80:
                            enemy.reflect = False
                    if "0-2" not in Globles.title_pool:
                        Globles.titles.clear()
                        Globles.TitleText("0-2", "", 'black')
                    if Globles.get_battle_state() == 0:
                        Globles.set_movable_area(80, 350)
                        PygameObject.spawn_enemy('scorpion', 280, 210)
                        PygameObject.spawn_enemy('scorpion', 250, 210)
                        PygameObject.spawn_enemy('bat', 150, 180)
                    if Globles.get_battle_state() == 2:
                        if "完成" not in Globles.title_pool:
                            Globles.titles.clear()
                            Globles.TitleText("完成", "Finished", 'orange')
                        if hero.rect.x > 300:
                            bg_index = 4
                            hero.rect.x = 80
                            Globles.next_wave()
                            Globles.title_pool.remove("完成")
                    elif hero.rect.x > 300:
                        hero.rect.x = 300

            if Globles.get_stage() >= 1:
                PygameObject.bulletMech()
                Globles.update_sprites(self.screen)
                Globles.draw_sprites(self.screen)

            # 显示标题和悬浮文本
            Globles.update_texts(self.screen)

            # 更新页面
            pygame.display.flip()

            # 设定页面更新速率
            self.clock.tick(60)

        # 关闭页面
        debug("开始页面播放完成", type='success', who=self.__class__.__name__)
        pygame.quit()


def init():
    # 初始化开始页面
    global form_game
    form_game = FormGame()


def display():
    # 显示开始页面
    form_game.display_screen()
