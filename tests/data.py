import math

A = 12

def func_1(a,b):
    return math.sin(a+b) + A

packed_func_1 = {'Code': {'co_argcount': 2,
          'co_cellvars': (),
          'co_code': '7400a0017c007c011700a101740217005300',
          'co_consts': [('NoneType', None)],
          'co_flags': 67,
          'co_freevars': (),
          'co_kwonlyargcount': 0,
          'co_lnotab': '0001',
          'co_name': 'func_1',
          'co_names': ('math', 'sin', 'A'),
          'co_nlocals': 2,
          'co_posonlyargcount': 0,
          'co_stacksize': 4,
          'co_varnames': ('a', 'b')},
 'Globs': {'A': ('int', 12), 'math': 'module'},
 'Type': 'Function'}

class Baza():

    def defier(self):
        return 'this is Baza'

class Powerful(Baza):

    activity = ('on', 'off')
    list = [1, 2, 3, 4]

    def __init__(self,a, b):
        self.a = a+2
        self.b = b+2
        print('qwe')

    def pull(self,a):
        self.list.append(a) 

packed_powerful = {'Attrs': {'activity': ('tuple', ('on', 'off')),
           'list': ('list', [1, 2, 3, 4])},
 'Bases': {'Baza': {'Attrs': {},
                    'Bases': {},
                    'Methods': {'defier': {'Code': {'co_argcount': 1,
                                                    'co_cellvars': (),
                                                    'co_code': '64015300',
                                                    'co_consts': [('NoneType',
                                                                   None),
                                                                  ('str',
                                                                   'this is '
                                                                   'Baza')],
                                                    'co_flags': 67,
                                                    'co_freevars': (),
                                                    'co_kwonlyargcount': 0,
                                                    'co_lnotab': '0001',
                                                    'co_name': 'defier',
                                                    'co_names': (),
                                                    'co_nlocals': 1,
                                                    'co_posonlyargcount': 0,
                                                    'co_stacksize': 1,
                                                    'co_varnames': ('self',)},
                                           'Globs': {},
                                           'Type': 'Function'}},
                    'Type': 'Class'}},
 'Methods': {'__init__': {'Code': {'co_argcount': 3,
                                   'co_cellvars': (),
                                   'co_code': '7c01640117007c005f007c02640117007c005f01740264028301010064005300',
                                   'co_consts': [('NoneType', None),
                                                 ('int', 2),
                                                 ('str', 'qwe')],
                                   'co_flags': 67,
                                   'co_freevars': (),
                                   'co_kwonlyargcount': 0,
                                   'co_lnotab': '00010a010a01',
                                   'co_name': '__init__',
                                   'co_names': ('a', 'b', 'print'),
                                   'co_nlocals': 3,
                                   'co_posonlyargcount': 0,
                                   'co_stacksize': 2,
                                   'co_varnames': ('self', 'a', 'b')},
                          'Globs': {},
                          'Type': 'Function'},
             'pull': {'Code': {'co_argcount': 2,
                               'co_cellvars': (),
                               'co_code': '7c006a00a0017c01a101010064005300',
                               'co_consts': [('NoneType', None)],
                               'co_flags': 67,
                               'co_freevars': (),
                               'co_kwonlyargcount': 0,
                               'co_lnotab': '0001',
                               'co_name': 'pull',
                               'co_names': ('list', 'append'),
                               'co_nlocals': 2,
                               'co_posonlyargcount': 0,
                               'co_stacksize': 3,
                               'co_varnames': ('self', 'a')},
                      'Globs': {},
                      'Type': 'Function'}},
 'Type': 'Class'}

packed_pwfullobj = {'Attrs': {'__class__': ('type', 'Powerful'),
           'a': ('int', 3),
           'activity': ('tuple', ('on', 'off')),
           'b': ('int', 4),
           'list': ('list', [1, 2, 3, 4])},
 'Methods': {'__init__': {'Code': {'co_argcount': 3,
                                   'co_cellvars': (),
                                   'co_code': '7c01640117007c005f007c02640117007c005f01740264028301010064005300',
                                   'co_consts': [('NoneType', None),
                                                 ('int', 2),
                                                 ('str', 'qwe')],
                                   'co_flags': 67,
                                   'co_freevars': (),
                                   'co_kwonlyargcount': 0,
                                   'co_lnotab': '00010a010a01',
                                   'co_name': '__init__',
                                   'co_names': ('a', 'b', 'print'),
                                   'co_nlocals': 3,
                                   'co_posonlyargcount': 0,
                                   'co_stacksize': 2,
                                   'co_varnames': ('self', 'a', 'b')},
                          'Globs': {},
                          'Type': 'Function'},
             'defier': {'Code': {'co_argcount': 1,
                                 'co_cellvars': (),
                                 'co_code': '64015300',
                                 'co_consts': [('NoneType', None),
                                               ('str', 'this is Baza')],
                                 'co_flags': 67,
                                 'co_freevars': (),
                                 'co_kwonlyargcount': 0,
                                 'co_lnotab': '0001',
                                 'co_name': 'defier',
                                 'co_names': (),
                                 'co_nlocals': 1,
                                 'co_posonlyargcount': 0,
                                 'co_stacksize': 1,
                                 'co_varnames': ('self',)},
                        'Globs': {},
                        'Type': 'Function'},
             'pull': {'Code': {'co_argcount': 2,
                               'co_cellvars': (),
                               'co_code': '7c006a00a0017c01a101010064005300',
                               'co_consts': [('NoneType', None)],
                               'co_flags': 67,
                               'co_freevars': (),
                               'co_kwonlyargcount': 0,
                               'co_lnotab': '0001',
                               'co_name': 'pull',
                               'co_names': ('list', 'append'),
                               'co_nlocals': 2,
                               'co_posonlyargcount': 0,
                               'co_stacksize': 3,
                               'co_varnames': ('self', 'a')},
                      'Globs': {},
                      'Type': 'Function'}},
 'Type': 'Powerful'}