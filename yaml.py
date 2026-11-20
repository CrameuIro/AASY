from ruamel.yaml import YAML
from init import get_aasy_config
import os
from cli import cli_print,cli_exit

# 读取应用来源yaml文件。若有误返回False
def get_source_yaml():
    src_yaml_path = get_aasy_config("src_yaml_path")
    yaml_error = 0
    
    # 1. 文件不存在
    if not os.path.exists(src_yaml_path):
        yaml_error = 1
    
    # 读取yaml以继续检查内容
    yaml = YAML(typ="safe")
    try:
        with open(src_yaml_path, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(f)
    except:
        # 2. yaml解析出错
        yaml_error = 2
    
    # 3. yaml内容出错
    # 第一层：字典
    expected = {"metadata": list, "category": list, "codetype": list, "app": list}
    target_cont = yaml_data
    if not (expected.keys() == target_cont.keys() and all(isinstance(expected[val], target_cont[val])) for val in target_cont):
        yaml_error = 3
    
    # （未完成）
    
    # 若有误，打印检查结果
    if not yaml_error:
        return yaml_data
    elif yaml_error == 1:
        cli_print(["/cs", f"'File {src_yaml_path}' not found."])
    elif yaml_error == 2:
        cli_print(["/cs", f"Unable to parse file '{src_yaml_path}'."])
    elif yaml_error == 3:
        cli_print(["/cs", f"The content of File '{src_yaml_path}' is incorrect."])

    SL_source_yaml()
    return False

        

        
# 没有可用的应用来源yaml文件，备份旧的&创建新的。
def SL_source_yaml()
    src_yaml_path = get_aasy_config("src_yaml_path")
    bad_yaml_path = get_aasy_config("bad_yaml_path")
    
    # 询问用户是否继续
    cli_print(["", f"You need a new '{src_yaml_path}' file.", "It will rename your old file, if it exists:", "'{src_yaml_path}' -> '{bad_yaml_path}'.", "Continue? (y/n)"])
    if not input().strip().lower() == 'y':
        cli_exit()
    
    # 备份旧的（未完成）
    
    # 创建新的（未完成）
    yaml_data = {}