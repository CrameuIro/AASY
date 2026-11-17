config = ["cancel_code" = "/e"]

def get_config(key = ""):
    if key:
        return config[key]
    else:
        return config