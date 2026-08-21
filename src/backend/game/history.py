#! Will be removed
type HistoryLike = list[tuple[int, str]]

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