class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isVertical(self):
        return self.start[0] == self.end[0]
    
    def isHorizontal(self):
        return self.start[1] == self.end[1]