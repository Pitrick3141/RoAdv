import sys

import pygame
import Globles
from debugOutp import debug

global form_home


class FormHome:
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设定屏幕尺寸
        self.screen = pygame.display.set_mode(Globles.get_screen_size())

        # 设定页面标题
        pygame.display.set_caption("RoAdv-Home")

        # 设定时钟
        self.clock = pygame.time.Clock()

        # 是否完成
        self.done = False

        # 初始化阶段
        Globles.init_stage()

        debug("开始页面初始化完成", type='success', who=self.__class__.__name__)
        debug("新的开始", type='Jie_Z')

    # 显示开始页面
    def display_screen(self):

        debug("进入开始页面循环体", who=self.__class__.__name__)
        debug("生命中每一个伟大都源于一次尝试。", type='Jie_Z')
        Globles.next_stage()

        # 动画参数，用于文本动画等
        ro_x = 20
        man_y = -50
        adv_x = 55
        en_y = -50
        click_alpha = 0
        click_color = 'black'
        about_alpha = 0
        reverse = 0

        # 循环文本列表
        about_texts = ["By Jie Z. and Yichen W.",
                       "For our beloved and lovely girlfriends",
                       "Happy Birthday!",
                       "生日快乐！",
                       "お誕生日おめでとう!",
                       "Joyeux anniversaire!",
                       "人间烟火，山河远阔",
                       "无一是你，无一不是你",
                       "水有舟可渡，山有径可寻",
                       "所爱隔山海，山海皆可平"]

        # 当前显示的循环文本序号
        about_index = 0
        # 用于循环文本动画的参数
        about_reverse = 0

        # 主循环体
        while not self.done:
            # 事件循环处理
            for event in pygame.event.get():
                # 退出程序
                if event.type == pygame.QUIT:
                    debug("触发退出事件,当前时刻{}".format(pygame.time.get_ticks()), who=self.__class__.__name__)
                    self.done = True
                    sys.exit(0)
                # 点击鼠标
                if event.type == pygame.MOUSEBUTTONDOWN:
                    debug("触发鼠标点击事件,当前时刻{}".format(pygame.time.get_ticks()), who=self.__class__.__name__)
                    if Globles.get_stage() == 0:
                        click_alpha = 255
                        reverse = 0
                        pygame.display.set_caption("RomanticAdventure-Home")
                        Globles.next_stage()
                        debug(
                            "加东时间八月十日晚上八点四十五分，我和王老师开始走出生命中那已经拿下的九十一分，我们开始向着那真正璀璨的九分迈进。",
                            type='Jie_Z')
                    if Globles.get_stage() >= 2:
                        self.done = True
                        debug("希望一路顺利。", type='Jie_Z')

            # 开始页面背景
            self.screen.fill(Globles.get_color('white'))

            # 根据阶段改变文本参数
            # 阶段0 点击开始提示闪烁
            if Globles.get_stage() == 0:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 50:
                    reverse *= -1
                click_alpha += 5 * reverse
            # 阶段1 文字移动，显示全部标题，点击开始提示交替变色，逐渐消失
            elif Globles.get_stage() == 1:
                click_color = 'title_blue' if Globles.get_span() // 100 % 2 == 0 else 'title_red'
                adv_x += 1
                if man_y < 40:
                    man_y += 1
                    en_y += 1
                if click_alpha > 0:
                    click_alpha -= 3
                if Globles.get_span() >= 1500:
                    Globles.next_stage()
            # 阶段2 完成一次文本循环后点击开始提示重新出现并闪烁
            elif Globles.get_stage() == 3:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 100:
                    reverse *= -1
                click_alpha += 5 * reverse
            # 阶段2后 关于文本出现，闪烁并循环
            if Globles.get_stage() >= 2:
                Globles.show_text(self.screen, about_texts[about_index], 20, 70,
                                  color='black', alpha=about_alpha, size=15, bold=False)
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
                    if about_index < len(about_texts) - 1:
                        about_index += 1
                    else:
                        # 完成一次循环
                        about_index = 0
                    if about_index == 2 and Globles.get_stage() == 2:
                        # 后面的太长了可以提前点击屏幕继续
                        Globles.next_stage()
                about_alpha += 3 * about_reverse

            # 开始页面标题文本
            Globles.show_text(self.screen, "Welcome to the", 20, 10)
            Globles.show_text(self.screen, "Ro", ro_x, 40)
            Globles.show_text(self.screen, "mantic", 55, man_y, color='title_red')
            Globles.show_text(self.screen, "Adv", adv_x, 40)
            Globles.show_text(self.screen, "enture !", 195, en_y, color='title_red')

            # 点击开始提示文本
            Globles.show_text(self.screen, "*Click to Start*", 250, 250, color=click_color, alpha=click_alpha)

            # 更新页面
            pygame.display.flip()

            # 设定页面更新速率
            self.clock.tick(60)

        # 关闭页面
        debug("开始页面播放完成", type='success', who=self.__class__.__name__)
        pygame.quit()


def init():
    # 初始化开始页面
    global form_home
    form_home = FormHome()


def display():
    # 显示开始页面
    form_home.display_screen()
