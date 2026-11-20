aasy_config = {"cancel_code": "/e", "src_yaml_path": "aasy_source.yaml", "bad_yaml_path": "CORRUPTED_aasy_source.yaml"}

# 获取aasy配置
def get_aasy_config(key = ""):
    if key:
        return aasy_config[key]
    else:
        return aasy_config