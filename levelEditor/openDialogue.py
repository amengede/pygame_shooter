from editorConfig import *
from container import *
from exit_box import *
from open_file_up import *
from open_file_down import *
from open_file import *
from file_entry import *
import pathlib

class OpenDialogue:
    def __init__(self,program,parent):
        self._program = program
        self._parent = parent
        #widgets
        self._container = Container(100,50,750,450,self)
        self._exit_box = ExitBox(818,50,32,32,self)
        self._files_box = Container(150,100,500,250,self)
        self._open_file_up = OpenFileUp(706,296,56,56,self)
        self._open_file_down = OpenFileDown(706,100,56,56,self)
        self._open_file = OpenFile(425,360,200,80,self)

        self._level_count = 0
        self._first_visible_level = 0
        self._max_visible_levels = 10
        self._last_visible_level = 0
        self._level_names = []
        self._currently_selected_level = ''
        self._fileEntries = []
        self.browseFolder()
        self.makeFileEntries()
    
    def browseFolder(self):
        for path in pathlib.Path("../levels/").iterdir():
            if path.is_file():
                if str(path).rsplit('.')[-1]=='json':
                    self._level_names.append(str(path))
                    self._level_count += 1

        if len(self._level_names)>=0:
            self._first_visible_level = 0
            self._last_visible_level = min(len(self._level_names)-1,self._max_visible_levels-1)


    def handleMouse(self):
        self._exit_box.handleMouse()
        self._open_file_up.handleMouse()
        self._open_file_down.handleMouse()
        self._open_file.handleMouse()
        for f in self._fileEntries:
            f.handleMouse()
    
    def getProgram(self):
        return self._program
    
    def getParent(self):
        return self._parent

    def setCurrentLevel(self,level):
        self._currently_selected_level = level

    def getCurrentLevel(self):
        return self._currently_selected_level
    
    def changeFileEntryRange(self,change):
        last = len(self._level_names) - 1
        if ((self._first_visible_level + change)>=0) and ((self._last_visible_level + change)<=last):
            self._first_visible_level += change
            self._last_visible_level += change
            self.makeFileEntries()
    
    def makeFileEntries(self):
        self._fileEntries = []
        a = self._first_visible_level
        b = self._last_visible_level
        for i in range(a,b+1):
            new_entry = FileEntry(150,100+25*(i-a),500,25,self)
            self._fileEntries.append(new_entry)
            new_entry.setName(self._level_names[i])

    def mouseUp(self):
        self._exit_box.mouseUp()
        self._open_file_up.mouseUp()
        self._open_file_down.mouseUp()
        self._open_file.mouseUp()
        for f in self._fileEntries:
            f.mouseUp()

    
    def draw(self):
        self._container.draw()
        self._exit_box.draw()
        self._files_box.draw()
        self._open_file_up.draw()
        self._open_file_down.draw()
        self._open_file.draw()
        for f in self._fileEntries:
            f.draw(f.getName()==self._currently_selected_level)