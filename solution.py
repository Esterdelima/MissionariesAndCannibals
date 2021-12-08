from state import State


class Solution():
    def __init__(self):
    
        self.queue = [State(3, 0, 3, 0, 'Left')]
        self.resolution = None

    def solution(self):
    
        for element in self.queue:
            if element.finalState():
                
                self.resolution = [element]
                while element.nodeHead:
                    self.resolution.insert(0, element.nodeHead)
                    element = element.nodeHead
                break;
            
            element.newNode()
            self.queue.extend(element.nodeNext)
