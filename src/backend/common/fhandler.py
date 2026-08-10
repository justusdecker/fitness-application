from yaml import safe_load

type JSONLike = dict | list

def file_read(filepath : str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def yaml_read(filepath : str, encoding='utf-8') -> JSONLike:
    with open(
        file = filepath, 
        mode = 'r', 
        encoding = encoding) as f:
        return safe_load(f)