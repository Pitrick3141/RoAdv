import pygame
# 全局变量

"""
预设的色彩，以rgb格式保存
格式:
color = (red, green, blue)
0 <= red, green, blue <= 255
"""

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

"""
屏幕大小
格式:
size = (width, height)
单位: pixel
"""

screen_size = (700, 500)

"""
字体
"""


def show_text(screen, content: str, font, x, y):
    text = font.render(content, True, black)
    screen.blit(text, [x, y])
