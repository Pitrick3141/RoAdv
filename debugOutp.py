import time

"""
调试输出静态函数，请勿随意编辑
使用方法
在代码头加入
from debugOutp import debug
调用函数
debug(内容，参数)
参数 type 调试类型
参数 who 来自哪个类

"""


def debug(text: str, **kwargs):
    # 读取当前时间
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # 信息来源
    info_from = "未知来源"
    if kwargs.get('who') == 'main':
        info_from = "主程序"
    if kwargs.get('who') == 'FormHome':
        info_from = "开始页面"

    # 错误信息
    if kwargs.get('type') == 'error':
        output_message = " [Error@{}] {}".format(info_from, text)
    # 警告信息
    elif kwargs.get('type') == 'warn':
        output_message = " [Warn@{}] {}".format(info_from, text)
    # 成功信息
    elif kwargs.get('type') == 'success':
        output_message = " [Success@{}] {}".format(info_from, text)
    # 作者言
    elif kwargs.get('type') == 'Jie_Z':
        output_message = " Jie Zhang: \"{}\"".format(text)
    elif kwargs.get('type') == 'Yichen_W':
        output_message = " Yichen Wang: \"{}\"".format(text)
    # 其他信息
    else:
        output_message = " [Info@{}] {}".format(info_from, text)

    # 输出调试信息
    print(current_time + output_message)
