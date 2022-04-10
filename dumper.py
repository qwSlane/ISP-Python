from asyncio.windows_events import NULL
from email.policy import default
from importlib import import_module
import inspect
from pprint import pprint
from struct import pack
import types

unserialized = ['__doc__', '__eq__', '__format__', '__ge__',
                '__getattribute__', '__gt__', '__hash__',
                '__le__', '__lt__', '__module__', '__ne__',
                '__reduce__', '__reduce_ex__', '__repr__',
                '__setattr__', '__sizeof__', '__subclasshook__',
                '__weakref__', '__delattr__', '__new__',
                '__dict__', '__dir__', '__init_subclass__',
                '__str__']

default_vars = ['int', 'str', 'list', 'tuple', 'NoneType', 
                'dict', 'getset_descriptor']

class Dumper():

    def dump(self, obj):
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

    def __dmp_func(self,obj):
        temp_code = obj.__code__
        dumped = {'Type' : 'Function'}
        temp = []
        for el in temp_code.co_consts:
            temp.append((type(el).__name__, el))
        data = {
            'co_argcount' : temp_code.co_argcount,
            'co_posonlyargcount' : temp_code.co_posonlyargcount,
            'co_kwonlyargcount' : temp_code.co_kwonlyargcount,
            'co_nlocals' : temp_code.co_nlocals,
            'co_stacksize' : temp_code.co_stacksize,
            'co_flags' : temp_code.co_flags,
            'co_code' : temp_code.co_code.hex(),
            'co_consts' : temp,
            'co_names' : temp_code.co_names,
            'co_varnames' : temp_code.co_varnames,
            'co_filename' : temp_code.co_filename.encode('utf-8').hex(),
            'co_name' : temp_code.co_name,
            'co_firstlineno' : temp_code.co_firstlineno,
            'co_lnotab' : temp_code.co_lnotab.hex(),
            'co_freevars' : temp_code.co_freevars,
            'co_cellvars' : temp_code.co_cellvars
        }
        dumped['Code'] = data

        glob = {}
        for k, v in obj.__globals__.items():
            if k in temp_code.co_names:
                glob[k] = (type(v).__name__, v)
        dumped['Globs'] = glob                  
        return dumped

    def __dmp_class(self,obj):
        data = obj.__dict__
        methods = {}
        vars = {}
        bases = {}
        for el in obj.__bases__:
            if not (el).__name__ == 'object':
                bases[(el).__name__] = (self.__dmp_class(el))

        for name, value in data.items():
            if inspect.isfunction(value):
                methods[name] = self.__dmp_func(value)
            elif not type(value).__name__ in default_vars:
                vars[name] = ('custom_obj',  self.__dmp_object(value))
            elif type(value).__name__ == 'type':
                vars[name] = ("Class", self.__dmp_class(value))
            elif not name in unserialized:
                vars[name] = (type(value).__name__, value)

        return {'Type' : 'Class', 'Methods': methods,
         'Attrs' : vars, 'Bases': bases}

    def __unpack_func(self,packed):
        code = packed['Code']
        consts = []
        for v in code['co_consts']:
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
                                   bytes.fromhex(
                                       code['co_filename']).decode('utf-8'),
                                   code['co_name'],
                                   int(code['co_firstlineno']),
                                   bytes.fromhex(code['co_lnotab']),
                                   tuple(code['co_freevars']),
                                   tuple(code['co_cellvars'])
                                   )
        
        func = types.FunctionType(func_code, self.__get_globs(packed))
        return func

    def __get_globs(self, globs):
        unpacked = {}

        for k, v in globs['Globs'].items():
            if v[0] == 'int':
                unpacked[k] = int(v[1])
            elif v[0] == 'str':
                unpacked[k] = str(v[1])
            elif v[0] == 'list':
                unpacked[k] = list(v[1])
            elif v[0] == 'dict':
                unpacked[k] = dict(v[1])
            elif v[0] == 'module':
                unpacked[k] = import_module(k)
            elif v[0] == 'tuple':
                unpacked[k] = tuple(v[1])
            elif v[0] == 'custom_obj':
                unpacked[k] = self.__unpack_object(v[1])
        return unpacked

    def __get_dict(self, obj):
        unpacked = {}

        for k, v in obj['Methods'].items():
            unpacked[k] = self.__unpack_func(v)
        
        for k, v in obj['Attrs'].items():
            if v[0] == 'int':
                unpacked[k] = int(v[1])
            elif v[0] == 'str':
                unpacked[k] = str(v[1])
            elif v[0] == 'list':
                unpacked[k] = list(v[1])
            elif v[0] == 'dict':
                unpacked[k] = dict(v[1])
            elif v[0] == 'tuple':
                unpacked[k] = tuple(v[1])
            elif v[0] == 'custom_obj':
                unpacked[k] = self.__unpack_object(v[1])
        return unpacked

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
        unpacked = self.__get_dict(obj) 
        n_class = type(('unpacked'), tuple(base) , unpacked)
        return n_class

    def __dmp_object(self, obj):
        data = dict(inspect.getmembers(obj))
        methods = {}
        vars = {}
        for name, value in data.items():
            if name in unserialized:
                continue
            elif inspect.ismethod(value):
                methods[name] = self.__dmp_func(value)
            else:
                vars[name] = (type(value).__name__, value)
        return {'Type' : name, 'Methods': methods, 'Attrs' : vars}

    def __unpack_object(self, obj):
        obj_dict = self.__get_dict(obj)
        new_class = type(obj['Type'], (object,), obj_dict)
        unpacked_obj = new_class()
        return unpacked_obj

