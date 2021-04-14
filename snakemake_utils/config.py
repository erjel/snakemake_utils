import yaml
from  pathlib import Path
import hashlib

def seed_from_config(filename):
    with open(filename, 'r') as f:
        config_str = f.read() + filename.name
        seed = int(hashlib.md5(config_str.encode('utf-8')).hexdigest(), 16)  % (2**32 -1)
    return seed

def read_config(filename, key=None):
    assert(Path(filename).is_file())
    with open(filename, 'r') as f:
        config_dict = yaml.load(f, Loader=yaml.FullLoader)
    if key is not None:
        return config_dict[key]
    else:
        return config_dict