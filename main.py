import os
import sys
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError
from datetime import datetime

# 读取yaml文件
def load():
    global yaml, yaml_data, yaml_filename, update_time, categories_list, category_name_list, cancel_code
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml_filename = "aasy_sources.yaml"
    cancel_code = "/e"
    
    # 寻找文件+异常处理
    if not os.path.exists(yaml_filename):
        clear(f"!错误：找不到文件{yaml_filename}。")
        return False
    
    # 读取文件+异常处理
    try:
        with open(yaml_filename, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(f)
    except YAMLError:
        clear("!错误：YAML语法错误。")
        return False
    
    # 空值检测+异常处理
    if not yaml_data:
        clear("!错误：YAML为空。")
        return False
    
    # 核心赋值+异常处理
    try:
        update_time = yaml_data.get("metadata").get("update_time")
        categories_list = yaml_data.get("categories",[])
        category_name_list = []
        for category in categories_list:
            category_name_list.append(category.get("name",""))
    except (AttributeError, TypeError):
        clear("!错误：YAML结构错误。")
        '''后续可以加入自动修复/提供标准结构的功能'''
        return False
        
    return True

# 清屏
def clear(error_info):
    os.system('cls' if os.name == 'nt' else 'clear')
    if error_info:
        print(f"{error_info}\n")

# 等待操作
def wait():
    temp = input("\n按下回车键继续。")
    clear(0)
# 退出    
def aasy_exit():
    sys.exit(0)

# 主菜单
def main_menu():
    action_code = input(f"AASY主菜单\n目标文件：{yaml_filename}\n\n1.查看概况\n2.搜索应用\n3.添加应用\n\n请输入编号，输入 {cancel_code} 退出应用。\n").strip()
    try:
        action_code = int(action_code)
        # 检查yaml文件
        if not load():
            return
        clear(0)
        if action_code == 1:
            view()
        elif action_code == 2:
            search()
        elif action_code == 3:
            add()
        else:
            clear("!错误：输入内容有误。\n")
    except:
        if action_code == cancel_code:
            aasy_exit()
        else:
            clear("!错误：输入内容有误。\n")
    
# 查看概况
def view():    
    total_count = 0    
    
    # 打印分类项目计数
    print(f"更新于{update_time}\n")
    for index, category in enumerate(categories_list):
        category_name = category_name_list[index]
        apps_list = category.get("apps", [])
        apps_count = len(apps_list)
        total_count += apps_count
        print(f"{index + 1}. {category_name}: {apps_count} 个项目")
    print(f"\n0. 合计：{total_count}个项目")
    
    # 询问是否打印详细应用列表
    view_category = input(f"\n输入分类编号查询对应分类应用列表（0~{len(category_name_list)}），输入 {cancel_code} 返回。\n").strip()
    try:
        view_category = int(view_category) - 1
        if view_category < -1 or view_category >= len(category_name_list):
            view_category = ""
            clear("!错误：编号错误。\n")
            return
        else: 
            clear(0)
            if view_category == -1:
                view_start, view_end = 0, len(category_name_list)
            else:
                view_start, view_end = view_category, view_category + 1
            for index in range(view_start, view_end): 
                apps_list = categories_list[index].get("apps", [])
                print(f"\n========================\n{category_name_list[index]} ({len(apps_list)})\n========================")
                
                for app in apps_list:
                    print(app.get("name"))
                    
        wait()
    except:
        if view_category == cancel_code:
            clear("已取消操作。\n")
        else:
            clear("!错误：输入内容有误。\n")
        return

# 搜索应用
# 待添加功能：1 需要在查询到结果时返回对应完整内容；2 后续可能会有重名软件，需要同时显示所有符合的结果；3 没有搜索到结果时，显示相似的结果   
def search():
    search_name = input(f"请输入要查询的安卓应用名称，输入 {cancel_code} 返回。 \n").strip()
    result_list = []
    clear(0)
    if search_name == cancel_code:
        return
    for category in categories_list:
        apps_list = category.get("apps", [])

        for app in apps_list:
            app_name = app.get("name")
            
            if app_name and app_name.lower() == search_name.lower():
                # 创建列表，存储应用真实名称和所在行数信息
                result_list = [app_name, app.lc.line + 1]
                print(f"\n{result_list[0]}已存在。\n位置在{yaml_filename}的第{result_list[1]}行。")
    if not result_list:
        clear(f"未找到 {search_name}。")
    wait()

# 添加应用
def add():
    # 创建列表=[应用名称, 所属分类, fdroid链接, github链接, official链接，类型]
    new_app_list = ["","","","","",""]
    print(f"过程中输入 {cancel_code} 可取消操作。\n")
    
    # 输入过程
    new_app_list[0] = input("请输入要添加的应用名称。\n").strip()
    if len(new_app_list[0]) < 1 or len(new_app_list[0]) > 100:
        print("!错误：输入长度有误。\n")
        return
    elif new_app_list[0].lower() == cancel_code:
        print("已取消操作。\n")
        return
        
    print("\n")
    for index, category in enumerate(category_name_list):
        print(f"{index + 1}. {category}")
    new_app_list[1] = input(f"\n请输入新应用所属分类编号（1~{len(category_name_list)}）。\n").strip()
    try:
        new_app_list[1] = int(new_app_list[1]) - 1
        if new_app_list[1] < 0 or new_app_list[1] >= len(category_name_list):
            new_app_list[1] = ""
            print("!错误：编号错误。\n")
            return
    except:
        if new_app_list[1] == cancel_code:
            print("已取消操作。\n")
        else:
            print("!错误：输入内容有误。\n")
        return
    new_app_list[2] = input("\n请输入新应用的F-Droid链接，没有则留空。\n").strip()
    if len(new_app_list[2]) > 100:
        print("!错误：输入长度有误。\n")
        return
    elif new_app_list[2].lower() == cancel_code:
        print("已取消操作。\n")
        return
        
    new_app_list[3] = input("\n请输入新应用的Github链接，没有则留空。\n").strip()
    if len(new_app_list[3]) > 100:
        print("!错误：输入长度有误。\n")
        return
    elif new_app_list[3].lower() == cancel_code:
        print("已取消操作。\n")
        return
    
    new_app_list[4] = input("\n请输入新应用的官网链接。官网必须提供免登录可用的下载链接。没有则留空。\n").strip()
    if len(new_app_list[4]) > 100:
        print("!错误：输入长度有误。\n")
        return
    elif new_app_list[4].lower() == cancel_code:
        print("已取消操作。\n")
        return
    
    # 判断类型
    if not new_app_list[2] and not new_app_list[3] and not new_app_list[4]:
        print("!错误：没有输入任一链接。")
        return
    elif new_app_list[2] or new_app_list[3]:
        new_app_list[5] = "foss"
    else:
        new_app_list[5] = "closed"
    
    # 输出新应用详情预览
    print(f"\n新应用详细信息\n名称：{new_app_list[0]}\n分类：{category_name_list[new_app_list[1]]}\n类型：{new_app_list[5]}\n")
    if new_app_list[2]:
        print(f"F-Droid链接：{new_app_list[2]}")
    if new_app_list[3]:
        print(f"Github链接：{new_app_list[3]}") 
    if new_app_list[4]:
        print(f"官网链接：{new_app_list[4]}") 

    # 二次确认
    sec_confirm = input("\n请确认信息无误。(y/n) ").strip()
    if sec_confirm.lower() != "y":
        print("已取消操作。\n")
        return
    
    # 写入yaml中对应的分类
    sources_list = []
    if new_app_list[2]:
        sources_list.append({"type": "fdroid", "url": new_app_list[2]})
    if new_app_list[3]:
        sources_list.append({"type": "github", "url": new_app_list[3]})
    if new_app_list[4]:
        sources_list.append({"type": "official", "url": new_app_list[4]})
    new_app_dict = {"name": new_app_list[0],"type": new_app_list[5],"sources": sources_list}
    
    target_apps_list = categories_list[new_app_list[1]].get("apps", [])
    target_apps_list.append(new_app_dict)
    update()
    print("\n已成功添加新应用。")
    wait()

# 排序并更新
def update():
    # 排序
    for category in categories_list:
        apps_list = category.get("apps", [])
        apps_list.sort(key=lambda x: x.get('name', '').lower())
        
    # 更新
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    yaml_data['metadata']['update_time'] = current_time
    with open(yaml_filename, "w", encoding="utf-8") as f:
        yaml.dump(yaml_data, f)
    
if __name__ == "__main__":
    # 检查yaml文件
    if not load():
        print("已退出AASY。\n")
        exit()
    clear(0)
    while True:
        main_menu()