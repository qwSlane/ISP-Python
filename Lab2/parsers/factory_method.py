from abc import ABCMeta, abstractmethod

class ISerializable(metaclass = ABCMeta):

    @abstractmethod
    def dump(self,obj, fp):
        pass

    @abstractmethod
    def dumps(self,obj):
        pass
    
    @abstractmethod
    def load(self,fp):
        pass

    @abstractmethod
    def loads(self,s):
        pass
