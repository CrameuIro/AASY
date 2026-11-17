from cli import cli_print, artistic_print

# 主菜单
def main_menu():
    while True:
        cli_print(["/cs"])
        artistic_print("AASY")
        cli_print(["1) App Overview", "2) Search Apps", "3) Add Apps", "0) Exit", ""])
        action = input()
    
if __name__ == '__main__':
    main_menu()