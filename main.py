import FormHome
from debugOutp import debug

if __name__ == '__main__':
    debug("主程序已启动，开始初始化", who='main')
    # 初始化开始页面
    FormHome.init()
    # 显示开始页面
    FormHome.display()
