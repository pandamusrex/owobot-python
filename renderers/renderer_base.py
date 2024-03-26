# An abstract base class from which all renderers should inherit

from abc import ABC, abstractmethod 

class Renderer(ABC):
    @abstractmethod
    def draw(self, matrix): 
        pass
