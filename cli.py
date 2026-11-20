import os
from pyfiglet import Figlet
import sys
        
''' 命令行打印，输入列表，依次打印每项。当列表项为以下值时不打印，执行对应功能：
/cs 清屏
/ps 打印“按下回车键继续。”并等待用户操作
'''
def cli_print(cont: list = [""]):
    for row in cont:
        if row == "/cs":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif row == "/ps":
            input("按下回车键继续。\n")
        else:
            print(row)
       
''' 打印艺术字
通过这个查看已有字体样式：pyfiglet.FigletFont.getFonts()
'''
def artistic_print(text = "", ffont = "ansi_shadow"):
    f = Figlet(font = ffont)
    print(f.renderText(text))

''' 退出命令行'''    
def cli_exit():
    sys.exit(0)