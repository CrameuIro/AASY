from cli import cli_print, artistic_print, cli_exit

# 主菜单
def main_menu():
    while True:
        cli_print(["/cs"])
        artistic_print("AASY")
        cli_print(["1) App Overview", "2) Search Apps", "3) Add Apps", "0) Exit", ""])
        action = input().strip()
        if action == "0":
            cli_exit()
        elif action == "1":
            app_overview()
        elif action == "2":
            app_search()
        elif action == "3":
            app_add()
        
# 应用概览
def app_overview():

# 应用搜索
def app_search():

# 应用添加
def app_add():


if __name__ == '__main__':
    main_menu()