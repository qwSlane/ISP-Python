from parsers.factory_method import ISerializable
from parsers.core.dumper import Dumper
from parsers.core.format import serialize_dict, serialize_list, deserialize


class TOML(ISerializable):

    def __init__(self):
        self.dumper = Dumper()

    def dumps(self,obj):
        
        data = self.dumper.pack(obj)

        str_data = "\n Object_data = '''\n"
        str_data += serialize_dict(data)
        str_data += "\n'''"

        return str_data

    def dump(self,obj, filepath):
        with open(filepath, 'w') as file:
            file.writelines(self.dumps(obj))

    def loads(self,string):
        data = string.split('\n')
        unpacked = deserialize(data[3:len(data)-3])
        return self.dumper.unpack(unpacked)

    def load(self, filepath):
        with open(filepath, 'r') as file:
            data = file.read()
            return self.loads(data)

