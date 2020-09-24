from fileSelector import *
from mapEditor import *

class Editor():
    def __init__(self):
        #self._active_element = mapEditor(self)
        self._active_element = fileSelector(self)
    
    def getActiveElement(self):
        return self._active_element
    
    def setActiveElement(self,element):
        self._active_element = element