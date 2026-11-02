import os
        
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