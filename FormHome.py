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

        debug("主页面初始化完成", type='success', who=self.__class__.__name__)

    def next_stage(self):
        # 进入下一个阶段
        self.stage += 1
        self.enter_stage.append(pygame.time.get_ticks())

    def get_span(self):
        # 返回从进入阶段到现在的时间
        return pygame.time.get_ticks() - self.enter_stage[self.stage]

    def show_text(self, content: str, x, y, **kwargs):
        # 在主页面上显示文本
        color = kwargs.get('color') if 'color' in kwargs.keys() else globles.title_blue
        alpha = kwargs.get('alpha') if 'alpha' in kwargs.keys() else 255
        size = kwargs.get('size') if 'size' in kwargs.keys() else 25
        is_bold = kwargs.get('bold') if 'bold' in kwargs.keys() else True
        is_italic = kwargs.get('italic') if 'italic' in kwargs.keys() else False
        font = pygame.font.SysFont('Microsoft Yahei', size, is_bold, is_italic)
        text = font.render(content, True, color)
        text.set_alpha(alpha)
        self.screen.blit(text, [x, y])
        return text

    # 显示主页面
    def display_screen(self):

        debug("进入主页面循环体", who=self.__class__.__name__)

        # 动画参数
        ro_x = 20
        man_y = -50
        adv_x = 55
        en_y = -50
        click_alpha = 0
        click_color = globles.black
        about_alpha = 0
        reverse = 0

        # 循环文本
        about_texts = ["By Jie Z. and Yichen W.",
                       "For our beloved lovely girlfriends",
                       "Happy Birthday!",
                       "生日快乐！"]
        about_index = 0
        about_reverse = 0

        # 主循环体
        while not self.done:
            # 检测退出页面
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.stage == 0:
                        click_alpha = 255
                        reverse = 0
                        pygame.display.set_caption("RomanticAdventure-Home")
                        self.next_stage()

            # 主页面背景
            self.screen.fill(globles.white)

            # 根据阶段改变文本参数
            if self.stage == 0:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 50:
                    reverse *= -1
                click_alpha += 5 * reverse
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
            elif self.stage == 2:
                if reverse == 0:
                    click_alpha += 5
                    if click_alpha > 255:
                        reverse = -1
                elif click_alpha > 255 or click_alpha < 50:
                    reverse *= -1
                click_alpha += 5 * reverse
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
                        about_index = 0
                about_alpha += 3 * about_reverse

            # 主页面欢迎文本
            self.show_text("Welcome to", 20, 10)
            self.show_text("Ro", ro_x, 40)
            self.show_text("Adv", adv_x, 40)
            self.show_text("*Click to Start*", 250, 250, color=click_color, alpha=click_alpha)
            self.show_text("mantic", 55, man_y, color=globles.title_red)
            self.show_text("enture", 195, en_y, color=globles.title_red)

            # 更新页面
            pygame.display.flip()

            # 设定更新速率
            self.clock.tick(60)

        # 关闭页面
        pygame.quit()


def init():
    global form_home
    form_home = FormHome()


def display():
    form_home.display_screen()
