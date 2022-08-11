import FormHome
import FormReady
import Globles
from debugOutp import debug

if __name__ == '__main__':
    debug("主程序已启动，开始初始化", who='main')
    # 初始化全局变量
    Globles.init()
    # 初始化开始页面
    FormHome.init()
    # 显示开始页面
    FormHome.display()
    # 初始化开始页面
    FormReady.init()
    # 显示开始页面
    FormReady.display()
