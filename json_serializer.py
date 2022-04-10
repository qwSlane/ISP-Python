from formatter import serialize_dict_json
from dumper import Dumper

class JsonSerializer():

    def __init__(self):
        self.dumper = Dumper() 

    def dumps(self,obj):
        return serialize_dict_json(self.dumper.dump(obj), '')

    def dump(self, obj, filepath):
        self.dumper = Dumper()
        with open(filepath, 'w') as file:
            file.writelines(serialize_dict_json(self.dumper.dump(obj), ''))

    def loads(self,string):
        return self.dumper.unpack(self.deserialize(string))


    def load(self,filepath):
        with open(filepath, 'r') as file:
            data = file.readlines()
            return self.loads(data[1:len(data)-1])

    def deserialize(self,data_list):
        FINAL_DATA = {}
        BRACKET_BUFFER = {
            1: FINAL_DATA
        }
        current_indentation_level = 1
        namespace = []
        tumblers = ['dict']

        space_clear_list = [el.strip('\t \n') for el in data_list]

        for line in space_clear_list:
            if '{' in line:
                tumblers.append('dict')
                parsed_data = [el.strip(' ').strip('"')
                            for el in line.strip(',').split(':')][0]  # key
                current_indentation_level += 1
                BRACKET_BUFFER[current_indentation_level] = {}
                namespace.append(parsed_data)
            elif '[' in line:
                tumblers.append('list')
                parsed_data = [el.strip(' ').strip('"')
                            for el in line.strip(',').split(':')][0]  # key
                current_indentation_level += 1
                BRACKET_BUFFER[current_indentation_level] = []
                namespace.append(parsed_data)
            elif '}' in line or ']' in line:
                tumblers.pop()
                current_indentation_level -= 1
                current_namespace = namespace.pop()
                if current_namespace == '[':
                     BRACKET_BUFFER[current_indentation_level].append(BRACKET_BUFFER[current_indentation_level+1])
                else:
                    BRACKET_BUFFER[current_indentation_level][current_namespace] = BRACKET_BUFFER[current_indentation_level+1]
                del BRACKET_BUFFER[current_indentation_level+1]
            else:
                if len(namespace) == 0:
                    parsed_data = [el.strip(' ').strip('"')
                                for el in line.strip(',').split(':')]
                    FINAL_DATA[parsed_data[0]] = parsed_data[1]
                else:
                    if tumblers[-1] == 'dict':
                        parsed_data = [el.strip(' ').strip('"')
                                    for el in line.strip(',').split(':')]
                        BRACKET_BUFFER[current_indentation_level][parsed_data[0]
                                                                ] = parsed_data[1]
                    else:
                        parsed_data = line.strip(',').strip('"')
                        BRACKET_BUFFER[current_indentation_level].append(
                            parsed_data)

        return FINAL_DATA
                