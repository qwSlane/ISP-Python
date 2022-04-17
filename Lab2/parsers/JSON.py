
from parsers.factory_method import ISerializable
from parsers.core.dumper import Dumper
from parsers.core.format import serialize_dict, deserialize


class json(ISerializable):

    def __init__(self):
        self.dumper = Dumper()

    def dumps(self,obj):
        return serialize_dict(self.dumper.pack(obj))

    def dump(self,obj, filepath):
        with open(filepath, 'w') as file:
            file.writelines(self.dumps(obj))

    def loads(self, string):
        data = string.split('\n')
        return self.dumper.unpack(deserialize(data[1:len(data)-2]))

    def load(self,filepath):
        with open(filepath, 'r') as file:
            data = file.read()
            return self.loads(data)





    