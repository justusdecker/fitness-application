from yaml import safe_load, safe_dump
from os.path import isfile

type HistoryLike = list[tuple[int, str]]

NEW_DATA = {
    "name": "",
    "xp": 0,
    "history": [],
    "coin": 0,
    "ruby": 0
}

class Person:
    def __init__(self, name: str):
        self.name = name
        self.xp = 0
        self.coin = 0
        self.ruby = 0
        self.__load(name)
    
    def __load(self, name: str): 
        if not isfile(self.__savePath): # Create a new savefile if not exist
            with open(self.__savePath, 'x') as f:
                safe_dump(NEW_DATA, f)
                
        with open(self.__savePath) as f:
            data = safe_load(f)
            
        self.history = History(data['history'])
        self.coin = data['coin']
        self.ruby = data['ruby']
        self.xp = data['xp']
        
    def save(self):
        data = {
            'xp': self.xp,
            'coin': self.coin,
            'ruby': self.ruby,
            'history': self.history.get(),
            'name': self.name
        }
        
        with open(self.__savePath, 'w') as f:
            safe_dump(data, f,encoding='utf-8')

    @property
    def __savePath(self) -> str:
        return f'./data/{self.name}.yml'
    
class HistoryEntry:
    def __init__(self, _time: int, _type: str):
        self._time = _time
        self._type = _type
    
    def get(self) -> tuple[int, str]:
        return self._time, self._type

class History:
    def __init__(self, history: HistoryLike):
        self.data: list[HistoryEntry] = []
        self.__load(history)
    
    def add(self, _time: int, _type: str):
        self.data.append(HistoryEntry(_time, _type))
    
    def __load(self, history: HistoryLike):
        for _time, _type in history:
            self.add(_time, _type)
    
    def get(self) -> HistoryLike:
        return [data.get() for data in self.data]
    
    def count(self):
        count = {}
        for key in self.data:
            if key._type in count:
                count[key._type] += 1
            else:
                count[key._type] = 1
        
        return count