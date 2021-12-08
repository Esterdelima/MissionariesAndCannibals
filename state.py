class State():

    def __init__(self, missionariesLeft, missionariesRight, cannibalsLef, cannibalsRight, side):
    
        self.missionariesLeft = missionariesLeft
        self.missionariesRight = missionariesRight
        self.cannibalsLef = cannibalsLef
        self.cannibalsRight = cannibalsRight
        self.side = side
        self.nodeHead = None
        self.nodeNext = []

    def __str__(self):
        
        return 'Missionaries: {}\t| Missionaries: {}\nCannibals: {}\t| Cannibals: {}'.format(
            self.missionariesLeft, self.missionariesRight, self.cannibalsLef, self.cannibalsRight
        )

    def startState(self):
        
        if ((self.missionariesLeft < 0) or (self.missionariesRight < 0)
            or (self.cannibalsLef < 0) or (self.cannibalsRight < 0)):
            return False
       
        return ((self.missionariesLeft == 0 or self.missionariesLeft >= self.cannibalsLef) and
                (self.missionariesRight == 0 or self.missionariesRight >= self.cannibalsRight))


    def finalState(self):
        
        solutionLeft = self.missionariesLeft == self.cannibalsLef == 0
        solutionRight = self.missionariesRight == self.cannibalsRight == 3
        return solutionLeft and solutionRight

    def newNode(self):
        newSide = 'Right' if self.side == 'Left' else 'Left'
        actions = [
            {'Missionaries': 2, 'Cannibals': 0},
            {'Missionaries': 1, 'Cannibals': 0},
            {'Missionaries': 1, 'Cannibals': 1},
            {'Missionaries': 0, 'Cannibals': 1},
            {'Missionaries': 0, 'Cannibals': 2},
        ]
        
        for move in actions:
            if self.side == 'Left':
                
                missionariesLeft = self.missionariesLeft - move['Missionaries']
                missionariesRight = self.missionariesRight + move['Missionaries']
                cannibalsLef = self.cannibalsLef - move['Cannibals']
                cannibalsRight = self.cannibalsRight + move['Cannibals']
            else:
                
                missionariesRight = self.missionariesRight - move['Missionaries']
                missionariesLeft = self.missionariesLeft + move['Missionaries']
                cannibalsRight = self.cannibalsRight - move['Cannibals']
                cannibalsLef = self.cannibalsLef + move['Cannibals']
            
            node = State(missionariesLeft, missionariesRight, cannibalsLef,
                           cannibalsRight, newSide)
            node.nodeHead = self
            if node.startState():
                self.nodeNext.append(node)
