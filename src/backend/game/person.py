from yaml import safe_load, safe_dump
from os.path import isfile

type HistoryLike = list[tuple[int, str]]

NEW_DATA = {
    "name": "",
    "xp": 0,
    "history": [],
}

class Person:
    def __init__(self, name: str):
        self.name = name
        self.xp = 0
        self.__load(name)
    
    def __load(self, name: str): 
        if not isfile(self.__savePath): # Create a new savefile if not exist
            with open(self.__savePath, 'x') as f:
                safe_dump(NEW_DATA, f)
                
        with open(self.__savePath) as f:
            data = safe_load(f)
            
        self.history = History(data['history'])
    
    def save(self):
        with open(self.__savePath, 'w') as f:
            safe_dump(..., f)

    @property
    def __savePath(self) -> str:
        return f'./data/{self.name}.json'
    
class HistoryEntry:
    def __init__(self, _time: int, _type: str):
        self._time = _time
        self._type = _type
    
    def get(self) -> tuple[int, str]:
        return self._time, self._type

class History:
    def __init__(self, history: HistoryLike):
        self.data = []
        self.__load(history)
    
    def __load(self, history: HistoryLike):
        for _time, _type in history:
            self.data.append(_time, _type)
    
    def get(self) -> HistoryLike:
        return self.data
    
    