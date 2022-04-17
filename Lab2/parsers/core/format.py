
def deserialize(data_list):
    deserialized = {}
    brackets = {
        1: deserialized
    }
    current_indentation_level = 1
    namespace = []
    tumblers = ['dict']

    space_clear_list = [el.strip('\t \n') for el in data_list]

    for line in space_clear_list:
        if '{' in line:
            tumblers.append('dict')
            parsed_data = [el.strip(' ').strip('"')
                        for el in line.strip(',').split(':')][0] 
            current_indentation_level += 1
            brackets[current_indentation_level] = {}
            namespace.append(parsed_data)
        elif '[' in line:
            tumblers.append('list')
            parsed_data = [el.strip(' ').strip('"')
                        for el in line.strip(',').split(':')][0] 
            current_indentation_level += 1
            brackets[current_indentation_level] = []
            namespace.append(parsed_data)
        elif '}' in line or ']' in line:
            tumblers.pop()
            current_indentation_level -= 1
            current_namespace = namespace.pop()
            if current_namespace == '[':
                    brackets[current_indentation_level].append(brackets[current_indentation_level+1])
            else:
                brackets[current_indentation_level][current_namespace] = brackets[current_indentation_level+1]
            del brackets[current_indentation_level+1]
        else:
            if len(namespace) == 0:
                parsed_data = [el.strip(' ').strip('"')
                            for el in line.strip(',').split(':')]
                deserialized[parsed_data[0]] = parsed_data[1]
            else:
                if tumblers[-1] == 'dict':
                    parsed_data = [el.strip(' ').strip('"')
                                for el in line.strip(',').split(':')]
                    brackets[current_indentation_level][parsed_data[0]
                                                            ] = parsed_data[1]
                else:
                    parsed_data = line.strip(',').strip('"')
                    brackets[current_indentation_level].append(
                        parsed_data)

    return deserialized

def tab():
    global TAB_COUNTER
    TAB_COUNTER += 1

def stab():
    global TAB_COUNTER
    TAB_COUNTER -= 1

def set_tabs(string):
    global TAB_COUNTER
    return '\t'*TAB_COUNTER + string

def serialize_list(data):
    string = ''
    string += '[\n'
    tab()

    for element in data:
        if type(element) in (list, tuple):
            string += set_tabs(f'{serialize_list(element)}')
        elif type(element) is dict:
            string += set_tabs(f'{serialize_dict(element)}')
        else:
            string += set_tabs(f'"{str(element)}"'+',\n')

    stab()
    string += set_tabs('],\n')

    return string

def serialize_dict(data):
    string = ''
    string += '{\n'
    tab()

    counter = 0
    max = len(data.items())-1

    for k, v in data.items():
        counter += 1
        if type(v) in (list, tuple):
            string += set_tabs(f'"{str(k)}": {serialize_list(v)}')
        elif type(v) is dict:
            string += set_tabs(f'"{str(k)}": {serialize_dict(v)}')
        else:
            string += set_tabs(f'"{str(k)}": "{str(v)}", \n')

        if(counter == max):
            string.strip(',')
            # string += '\n'


    stab()
    string += set_tabs('},\n')

    return string

TAB_COUNTER = 0
