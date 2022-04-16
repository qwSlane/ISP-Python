from importlib import import_module
import inspect

import types

class Dumper():

    def pack(self, obj):

        if inspect.isfunction(obj):
            return self.__dmp_func(obj)
        elif inspect.isclass(obj):
            return self.__dmp_class(obj)
        else:
            return self.__dmp_object(obj)

    def unpack(self, obj):

        if obj['Type'] == 'Class':
            return self.__unpack_class(obj)
        elif obj['Type'] == 'Function':
            return self.__unpack_func(obj)
        else:
            return self.__unpack_object(obj)

    def __define_type(self, data):

        if type(data) is list:
            consts = []
            for v in data:
                if v[0] == 'int':
                    consts.append(int(v[1]))
                elif v[0] == 'str':
                    consts.append(str(v[1]))
                elif v[0] == 'list':
                    consts.append(list(v[1]))
                elif v[0] == 'dict':
                    consts.append(dict(v[1]))
                elif v[0] == 'tuple':
                    consts.append((v[1]))
                elif v[0] == 'NoneType':
                    consts.append(None)
            return consts
        else:
            unpacked = {}
            for k, v in data.items():
                if v[0] == 'int':
                    unpacked[k] = int(v[1])
                elif v[0] == 'str':
                    unpacked[k] = str(v[1])
                elif v[0] == 'list':
                    unpacked[k] = list(v[1])
                elif v[0] == 'dict':
                    unpacked[k] = dict(v[1])
                elif v == 'module':
                    unpacked[k] = import_module(k)
                elif v[0] == 'tuple':
                    unpacked[k] = tuple(v[1])
                elif v[0] == 'custom_obj':
                    unpacked[k] = self.__unpack_object(v[1])
            return unpacked

    def __dmp_func(self,obj):

        dumped = {}

        dumped['Type'], dumped['Globs'] = 'Function', {}
        temp_code = obj.__code__
        consts = [(type(el).__name__, el) for el in temp_code.co_consts]
        
        dumped['Code'] = {
            'co_argcount' : temp_code.co_argcount,
            'co_posonlyargcount' : temp_code.co_posonlyargcount,
            'co_kwonlyargcount' : temp_code.co_kwonlyargcount,
            'co_nlocals' : temp_code.co_nlocals,
            'co_stacksize' : temp_code.co_stacksize,
            'co_flags' : temp_code.co_flags,
            'co_code' : temp_code.co_code.hex(),
            'co_consts' : consts,
            'co_names' : temp_code.co_names,
            'co_varnames' : temp_code.co_varnames,
            'co_name' : temp_code.co_name,
            'co_lnotab' : temp_code.co_lnotab.hex(),
            'co_freevars' : temp_code.co_freevars,
            'co_cellvars' : temp_code.co_cellvars
        }

        for k, v in obj.__globals__.items():
            if k in temp_code.co_names:
                if not type(v).__name__ == 'module':
                    dumped['Globs'][k] = (type(v).__name__, v)
                else:
                    dumped['Globs'][k] = type(v).__name__

        return dumped

    def __unpack_func(self,packed):

        code = packed['Code']
        consts = self.__define_type(code['co_consts'])

        func_code = types.CodeType(int(code['co_argcount']),
                                   int(code['co_posonlyargcount']),
                                   int(code['co_kwonlyargcount']),
                                   int(code['co_nlocals']),
                                   int(code['co_stacksize']),
                                   int(code['co_flags']),
                                   bytes.fromhex(code['co_code']),
                                   tuple(consts),
                                   tuple(code['co_names']),
                                   tuple(code['co_varnames']),
                                    'filename',
                                   code['co_name'],
                                   int(0),
                                   bytes.fromhex(code['co_lnotab']),
                                   tuple(code['co_freevars']),
                                   tuple(code['co_cellvars'])
                                   )
        globs = self.__define_type(packed['Globs'])
        func = types.FunctionType(func_code, globs)
        return func

    def __dmp_class(self,obj):

        dumped = {}

        dumped['Type'] = 'Class'
        dumped['Methods'], dumped['Attrs'], dumped['Bases'] = {},{},{}

        data = obj.__dict__

        for el in obj.__bases__:
            if not (el).__name__ == 'object':
                dumped['Bases'][(el).__name__] = self.__dmp_class(el)

        for name, value in data.items():
            if inspect.isfunction(value):
                dumped['Methods'][name] = self.__dmp_func(value)
            elif not type(value).__name__ in default_vars and \
            not name in unserialized:
                dumped['Attrs'][name] = ('custom_obj',  self.__dmp_object(value))
            elif type(value).__name__ == 'type':
                dumped['Attrs'][name] = ("Class", self.__dmp_class(value))
            elif not name in unserialized:
                dumped['Attrs'][name] = (type(value).__name__, value)
        
        return dumped
    
    def __getbases(self, obj):

        bases = []
        if not obj['Bases']:
            return (object, )
        else:
            for k, el in obj['Bases'].items():
                bases.append(self.__unpack_class(el))

        return bases

    def __unpack_class(self,obj):
        base = self.__getbases(obj)
        unpacked = self.__define_type(obj['Attrs']) 
        for k, v in obj['Methods'].items():
            unpacked[k] = self.__unpack_func(v)
#            pprint(unpacked)
        n_class = type(('unpacked'), tuple(base) , unpacked)

        return n_class

    def __dmp_object(self, obj):

        dumped = {}

        dumped['Type'] = type(obj).__name__
        dumped['Methods'], dumped['Attrs'] = {}, {}

        data = dict(inspect.getmembers(obj))
        for name, value in data.items():
            if name in unserialized:
                continue
            elif inspect.ismethod(value):
                dumped['Methods'][name] = self.__dmp_func(value)
            else:
                if type(value).__name__ == 'type':
                    dumped['Attrs'][name] = (type(value).__name__, value.__name__)
                else:
                    dumped['Attrs'][name] = (type(value).__name__, value)
#       pprint(dumped)
        return dumped

    def __unpack_object(self, obj):

        methods = {}
        obj_dict  = self.__define_type(obj['Attrs'])

        for k, v in obj['Methods'].items():
            if not k == "__init__":
                methods[k] = self.__unpack_func(v)
        obj_dict.update(methods)
        
        new_class = type(obj['Type'], (object,), obj_dict)
        unpacked_obj = new_class()

        return unpacked_obj


unserialized = ['__doc__', '__eq__', '__format__', '__ge__',
                '__getattribute__', '__gt__', '__hash__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__reduce__', '__reduce_ex__', '__repr__',
                '__setattr__', '__sizeof__', '__subclasshook__',
                '__weakref__', '__delattr__', '__new__',
                '__dict__', '__dir__', '__init_subclass__',
                '__str__']

default_vars = ['int', 'str', 'list', 'tuple', 'NoneType', 
                'dict']

        

        
