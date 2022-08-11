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

        # 设定字体
        self.font = pygame.font.SysFont('Calibri', 30, True, False)

        debug("主页面初始化完成", type='success', who=self.__class__.__name__)

    def show_text(self, content: str, x, y):
        text = self.font.render(content, True, globles.black)
        self.screen.blit(text, [x, y])
        return text

    # 显示主页面
    def display_screen(self):

        debug("进入主页面循环体", who=self.__class__.__name__)

        # 主循环体
        while not self.done:

            # 检测退出页面
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            # 主页面背景
            self.screen.fill(globles.white)

            # 主页面欢迎文本
            self.show_text("Welcome to", 20, 10)
            text_ro = self.show_text("Ro", 20, 40)
            text_adv = self.show_text("Adv", 55, 40)
            text_start = self.show_text("Click to Start", 250, 250)

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
