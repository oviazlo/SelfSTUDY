class EmptyQueue(Exception):
    pass

from collections import deque

class PriorityQueue_byTeacher():
    
    def __init__(self):
        #self._qs = ([],[],[],[],[])
        self._qs = (deque(),deque(),deque(),deque(),deque())
    
    def add(self, item, priority=2):
        if not (0 <= priority <= 4):
            raise ValueError
        self._qs[priority].append(item)
        
    def pop(self):
        for q in self._qs:
            if q:
                #return q.pop(0)
                return q.popleft()
        else:
            raise EmptyQueue
                        
    def __len__(self):
        return sum(map(len, self._qs))


class PriorityQueue_myImpl():
    
    def __init__(self):
        self._body = {}
        #self._body = ([],[],[],[],[])
        self._pList = []
    
    def add(self, item, priority=2):
        if priority not in self._pList:
            #if type(priority)!=int:
            if not isinstance(priority, int):
                raise TypeError
            #if priority<0 or priority>4:
            if not (0 <= priority <= 4):
                raise ValueError
            self._pList.append(priority)
            self._pList.sort()
            self._body[priority] = []
        self._body[priority].append(item)
        
    def pop(self):
        #if len(self._pList)>0:
        if self._pList:    
            index = self._pList[0]
            if len(self._body[self._pList[0]])==1:
                self._pList.remove(index)
            return self._body[index].pop(0)
        else:
            raise EmptyQueue
        
    def __len__(self):
        counter = 0
        for priority in self._pList:
            counter += len(self._body[priority])
        return counter
    
    
PriorityQueue = PriorityQueue_byTeacher