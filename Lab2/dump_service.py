from parsers.JSON import json
from parsers.TOML import TOML
from parsers.YAML import YAML

def get_format(format):
    if format == 'json':
        return json()
    elif format == 'yaml' or format == 'yml':
        return YAML()
    elif format == 'toml':
         return TOML()
    else:
        raise ValueError('Unknown parser.')

def dumps(format,obj):
    dumper = get_format(format)
    return dumper.dumps(obj)

def dump(format, obj, filepath):
    dumper = get_format(format)
    dumper.dump(obj, filepath)

def loads(format, string):
    dumper = get_format(format)
    return dumper.loads(string)

def load(format, filepath):
    dumper = get_format(format)
    return dumper.load(filepath)
