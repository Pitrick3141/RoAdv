import pygame
import globles
from debugOutp import debug

global form_home


class FormHome:
    def __init__(self):
        # 初始化pygame
        pygame.init()

        # 设定屏幕尺寸
        self.screen = pygame.display.set_mode(globles.screen_size)

        # 设定页面标题
        pygame.display.set_caption("RoAdv-Home")

        # 设定时钟
        self.clock = pygame.time.Clock()

        # 是否完成
        self.done = False

        # 当前阶段和进入各个阶段的时间
        self.stage = 0
        self.enter_stage = [pygame.time.get_ticks()]

        debug("开始页面初始化完成", type='success', who=self.__class__.__name__)
        debug("新的开始", type='Jie_Z')

    def next_stage(self):
        # 进入下一个阶段
        self.stage += 1
        # 记录阶段开始的时间
        self.enter_stage.append(pygame.time.get_ticks())

    def get_span(self):
        # 返回从进入阶段到现在的时间
        return pygame.time.get_ticks() - self.enter_stage[self.stage]

    def show_text(self, content: str, x, y, **kwargs):
        # 在主页面上显示文本

        # 可选参数
        # 颜色 默认 title_blue
        color = kwargs.get('color') if 'color' in kwargs.keys() else globles.title_blue
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
        text = font.render(content, True, color)

        # 设置文字透明度
        text.set_alpha(alpha)

        # 在屏幕上显示文字
        self.screen.blit(text, [x, y])

    # 显示开始页面
    def display_screen(self):

        debug("进入开始页面循环体", who=self.__class__.__name__)
        debug("生命中每一个伟大都源于一次尝试。", type='Jie_Z')

        # 动画参数，用于文本动画等
        ro_x = 20
        man_y = -50
        adv_x = 55
        en_y = -50
        click_alpha = 0
        click_color = globles.black
        about_alpha = 0
        reverse = 0

        # 循环文本列表
        about_texts = ["By Jie Z. and Yichen W.",
                       "For our beloved lovely girlfriends",
                       "Happy Birthday!",
                       "生日快乐！"]

        # 当前显示的循环文本序号
        about_index = 0
        # 用于循环文本动画的参数
        about_reverse = 0
        # 是否已经完成一次循环
        about_finished = False

        # 主循环体
        while not self.done:
            # 事件循环处理
            for event in pygame.event.get():
                # 退出程序
                if event.type == pygame.QUIT:
                    self.done = True
                # 点击鼠标
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.stage == 0:
                        click_alpha = 255
                        reverse = 0
                        pygame.display.set_caption("RomanticAdventure-Home")
                        self.next_stage()
                        debug(
                            "加东时间八月十日晚上八点四十五分，我和王老师开始走出生命中那已经拿下的九十一分，我们开始向着那真正璀璨的九分迈进。",
                            type='Jie_Z')
                    if self.stage >= 2:
                        self.done = True
                        debug("希望一路顺利。", type='Jie_Z')

            # 主页面背景
            self.screen.fill(globles.white)

            # 根据阶段改变文本参数
            # 阶段0 点击开始提示闪烁
            if self.stage == 0:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 50:
                    reverse *= -1
                click_alpha += 5 * reverse
            # 阶段1 文字移动，显示全部标题，点击开始提示交替变色，逐渐消失
            elif self.stage == 1:
                click_color = globles.title_blue if self.get_span() // 100 % 2 == 0 else globles.title_red
                adv_x += 1
                if man_y < 40:
                    man_y += 1
                    en_y += 1
                if click_alpha > 0:
                    click_alpha -= 3
                if self.get_span() >= 1500:
                    self.next_stage()
            # 阶段2 完成一次文本循环后点击开始提示重新出现并闪烁
            elif self.stage == 2 and about_finished:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 50:
                    reverse *= -1
                click_alpha += 5 * reverse
            # 阶段2后 关于文本出现，闪烁并循环
            if self.stage >= 2:
                self.show_text(about_texts[about_index], 20, 70, color=globles.black, alpha=about_alpha, size=15, bold=False)
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
                        about_finished = True
                about_alpha += 3 * about_reverse

            # 开始页面标题文本
            self.show_text("Welcome to", 20, 10)
            self.show_text("Ro", ro_x, 40)
            self.show_text("mantic", 55, man_y, color=globles.title_red)
            self.show_text("Adv", adv_x, 40)
            self.show_text("enture", 195, en_y, color=globles.title_red)

            # 点击开始提示文本
            self.show_text("*Click to Start*", 250, 250, color=click_color, alpha=click_alpha)

            # 更新页面
            pygame.display.flip()

            # 设定页面更新速率
            self.clock.tick(60)

        # 关闭页面
        pygame.quit()


def init():
    # 初始化开始页面
    global form_home
    form_home = FormHome()


def display():
    # 显示开始页面
    form_home.display_screen()
