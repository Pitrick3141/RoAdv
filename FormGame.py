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

        # 暂停
        is_hold = False

        # 助战
        is_assisted = False

        # 重新挑战
        is_reset = False

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
        bg_list = ['bg', 'bg_2', 'forestleft', 'forestright', "treeleft", "treeright", "fountain", "fountainnight",
                   "palace"]

        # 控制每关敌人
        enemies = {'forestleft': [('bat', 600, 180)],
                   'forestright': [('scorpion', 280, 210),
                                   ('scorpion', 250, 210),
                                   ('bat', 150, 180)],
                   'treeleft': [('scorpion', 200, 360),
                                ('scorpion', 220, 360),
                                ('scorpion', 240, 360),
                                ('scorpion', 280, 360),
                                ('bat', 150, 340),
                                ('bat', 250, 340),
                                ('bat', 300, 340)],
                   'treeright': [('scorpion', 200, 360),
                                 ('scorpion', 220, 360),
                                 ('scorpion', 240, 360),
                                 ('scorpion', 280, 360),
                                 ('scorpion', 320, 360),
                                 ('scorpion', 360, 360),
                                 ('bat', 150, 340),
                                 ('bat', 250, 340),
                                 ('bat', 300, 340)],
                   'fountain': [('scorpion', 200, 380),
                                ('scorpion', 220, 380),
                                ('scorpion', 240, 380),
                                ('scorpion', 280, 380),
                                ('scorpion', 320, 380),
                                ('scorpion', 360, 380),
                                ('bat', 150, 360),
                                ('bat', 200, 360),
                                ('bat', 250, 360),
                                ('bat', 300, 360),
                                ('bat', 350, 360)],
                   'fountainnight': [('scorpion', 200, 380),
                                    ('scorpion', 220, 380),
                                    ('scorpion', 240, 380),
                                    ('scorpion', 260, 380),
                                    ('scorpion', 280, 380),
                                    ('scorpion', 300, 380),
                                    ('scorpion', 320, 380),
                                    ('scorpion', 340, 380),
                                     ('bat', 150, 360),
                                     ('bat', 250, 360),
                                     ('bat', 350, 360),
                                     ('bat', 400, 360),
                                     ('bat', 450, 360),
                                     ('bat', 500, 360),
                                     ('bat', 550, 360)],
                   'palace': [('scorpion', 200, 380),
                                    ('scorpion', 220, 380),
                                    ('scorpion', 240, 380),
                                    ('scorpion', 260, 380),
                                    ('scorpion', 280, 380),
                                    ('scorpion', 300, 380),
                                    ('scorpion', 320, 380),
                                    ('scorpion', 340, 380),
                                    ('scorpion', 400, 380),
                                    ('scorpion', 450, 380),
                                    ('scorpion', 500, 380),
                                     ('bat', 150, 360),
                                     ('bat', 250, 360),
                                     ('bat', 350, 360),
                                     ('bat', 400, 360),
                                     ('bat', 450, 360),
                                     ('bat', 500, 360),
                                     ('bat', 550, 360),
                                     ('bat', 600, 360),
                                     ('bat', 650, 360)],
                   }

        # 控制每关标题
        titles = {'forestleft': [("序章", "Prologue"), ("0-1", ""), ("净化所有敌人", "Purify all enemies")],
                  'forestright': [("0-2", "")],
                  'treeleft': [("第一章", "Chapter 1"), ("1-1", "")],
                  'treeright': [("1-2", "")],
                  'fountain': [("第二章", "Chapter 2"), ("2-1", "")],
                  'fountainnight': [("2-2", "")],
                  'palace': [("终章", "Final")]}

        # 控制剧情播放
        plots_before = {'forestleft': [("{}和{}做好了准备，".format(Globles.get_chara_name('prot', 'zh'), Globles.get_chara_name('friend', 'zh')),
                                        "{} and {} get everything prepared".format(Globles.get_chara_name('prot', 'en'),
                                                                                   Globles.get_chara_name('friend', 'en')),
                                        20),
                                       ("进入了小镇边的森林。",
                                        "and went into the forest besides the town.",
                                        20),
                                       ("突然一只黑影从树丛中穿出，",
                                        "Suddenly a shadow dashed from the bush,",
                                        20),
                                       ("{}定睛一看，是一只漆黑的蝙蝠，正向他冲来。".format(Globles.get_chara_name('prot', 'zh')),
                                        "{} found that it was a black bat charging towards him.".format(Globles.get_chara_name('prot', 'en')),
                                        20)],
                        'forestright': [("随着{}和{}逐渐深入森林,".format(Globles.get_chara_name('prot', 'zh'), Globles.get_chara_name('friend', 'zh')),
                                         "As {} and {} went further into the forest".format(Globles.get_chara_name('prot', 'en'),
                                                                                            Globles.get_chara_name('friend', 'en')),
                                         20),
                                        ("越来越多的魔物从阴影中涌现。",
                                         "more and more monsters emerged from the shades.",
                                         20),
                                        ("他们高举武器，冲向魔物。",
                                         "They raised their weapons and headed these monsters.",
                                         20),
                                        ("拯救{}的使命就在他们的身上".format(Globles.get_chara_name('place', 'zh')),
                                         "The mission of saving {} is on their back.".format(Globles.get_chara_name('place', 'en')),
                                         20), ],
                        'treeleft': [("战前剧情_1_1", "Placeholder", 20)],
                        'treeright': [("战前剧情_1_2", "Placeholder", 20)],
                        'fountain': [("战前剧情_2_1", "Placeholder", 20)],
                        'fountainnight': [("战前剧情_2_2", "Placeholder", 20)],
                        'palace': [("战前剧情_终章", "Placeholder", 20)]}

        plots_after = {'forestleft': [("战后剧情_0_1", "Placeholder", 20)],
                       'forestright': [("战后剧情_0_2", "Placeholder", 20)],
                       'treeleft': [("战后剧情_1_1", "Placeholder", 20)],
                       'treeright': [("战后剧情_1_2", "Placeholder", 20)],
                       'fountain': [("战后剧情_2_1", "Placeholder", 20)],
                       'fountainnight': [("战后剧情_2_2", "Placeholder", 20)],
                       'palace': [("战后剧情_终章", "Placeholder", 20)]}

        # 控制每关移动范围
        movable_limits = {'forestleft': (0, 680, 180),
                          'forestright': (60, 330, 180),
                          'treeleft': (40, 700, 360),
                          'treeright': (0, 700, 360),
                          'fountain': (0, 700, 360),
                          'fountainnight': (0, 700, 360),
                          'palace': (0, 700, 360)}

        # 英雄列表
        hero_list = ['none', 'yichen', 'shenran', 'jie', 'nana']

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
                    if key_list[pygame.K_q]:
                        if Globles.get_stage() == 0:
                            Globles.next_stage()
                            about_reverse = 0
                            about_alpha = 0
                            debug("已跳过剧情", type='info', who=self.__class__.__name__)
                            bg_index = 2
                        else:
                            Globles.titles.clear()
                            debug("已跳过剧情", type='info', who=self.__class__.__name__)
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
                    if key_list[pygame.K_r]:
                        # 复苏英雄
                        if Globles.is_defeated():
                            is_reset = True
                            is_assisted = False
                            Globles.revive_hero()
                            hero = PygameObject.Character(hero_list[Globles.get_protagonist()], 30, 180)
                            Globles.add_sprite(hero, 1)
                            hero.rect.x = movable_limits.get(bg_list[bg_index])[0]
                            hero.rect.y = movable_limits.get(bg_list[bg_index])[2]
                            Globles.next_wave()
                    if key_list[pygame.K_f]:
                        # 召唤助战
                        if Globles.is_defeated():
                            is_assisted = True
                            is_reset = False
                            Globles.revive_hero()
                            hero = PygameObject.Character(hero_list[3 if Globles.get_protagonist() == 1 else 1], 30, 180)
                            Globles.add_sprite(hero, 1)
                            hero.rect.x = movable_limits.get(bg_list[bg_index])[0]
                            hero.rect.y = movable_limits.get(bg_list[bg_index])[2]
                            Globles.next_wave()

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
                if is_reset or is_assisted:
                    if "过了一会，" not in Globles.title_pool:
                        is_hold = True
                        if is_reset:
                            Globles.TitleText("过了一会，", "After a while,", 'black', 20)
                            Globles.TitleText("在他们返回营地休整一番之后，",
                                            "After a preparation back in their camp,", 'black', 20)
                            Globles.TitleText("{}和{}重新踏上了冒险的旅途".format(Globles.get_chara_name('prot', 'zh'), Globles.get_chara_name('friend', 'zh')),
                                            "{} and {} returned to the adventure again.".format(
                                                Globles.get_chara_name('prot', 'en'),
                                                Globles.get_chara_name('friend', 'en')), 'black', 20)
                        else:
                            Globles.TitleText("过了一会，", "After a while,", 'black', 20)
                            Globles.TitleText("{}扶起倒地的{}，".format(Globles.get_chara_name('friend', 'zh'), Globles.get_chara_name('prot', 'zh')),
                                            "{} helped {} to stand up again,".format(Globles.get_chara_name('friend', 'en'),
                                                                                    Globles.get_chara_name('prot', 'en')),
                                            'black', 20)
                            Globles.TitleText("并将他在营地安顿好，", "and settle him back at their camp,", 'black', 20)
                            Globles.TitleText("在他休整的时候替他净化前方的敌人，",
                                            "assisting him to purify all enemies during his preparation.", 'black', 20)
                elif plots_before.get(bg_list[bg_index])[0][0] not in Globles.title_pool:
                    is_hold = True
                    Globles.titles.clear()
                    for plot in plots_before.get(bg_list[bg_index]):
                        Globles.TitleText(plot[0], plot[1], 'black', plot[2])
                if not Globles.titles:
                    is_hold = False
                if titles.get(bg_list[bg_index])[0][0] not in Globles.title_pool and not is_hold:
                    for title in titles.get(bg_list[bg_index]):
                        Globles.TitleText(title[0], title[1], 'red' if bg_list[bg_index] == 'palace' else 'black')
                if Globles.get_battle_state() == 0:
                    movable_area = movable_limits.get(bg_list[bg_index])
                    Globles.set_movable_area(movable_area[0], movable_area[1])
                    for enemy in enemies.get(bg_list[bg_index]):
                        PygameObject.spawn_enemy(enemy[0], enemy[1], enemy[2])
                if Globles.get_battle_state() == 2:
                    if plots_after.get(bg_list[bg_index])[0][0] not in Globles.title_pool:
                        Globles.titles.clear()
                        for plot in plots_after.get(bg_list[bg_index]):
                            Globles.TitleText(plot[0], plot[1], 'black', plot[2])
                    if "关卡完成" not in Globles.title_pool:
                        Globles.TitleText("关卡完成", "Level Finished", 'orange')
                    if hero.rect.x > movable_limits.get(bg_list[bg_index])[1] - hero.rect.width - 10 and not Globles.titles:
                        if bg_list[bg_index] == 'palace':
                            Globles.next_stage()
                        else:
                            bg_index += 1
                            hero.rect.x = movable_limits.get(bg_list[bg_index])[0]
                            hero.rect.y = movable_limits.get(bg_list[bg_index])[2]
                            Globles.next_wave()
                            Globles.title_pool.remove("关卡完成")
                            is_reset = False
                            if is_assisted:
                                is_assisted = False
                                Globles.remove_sprite(hero)
                                hero = PygameObject.Character(hero_list[Globles.get_protagonist()], 30, 180)
                                Globles.add_sprite(hero, 1)


            if Globles.get_stage() >= 1:
                if not is_hold:
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
