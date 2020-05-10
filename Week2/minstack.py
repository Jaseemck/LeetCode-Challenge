class MinStack:
    def __init__(self):
        self.data = []          # Store all the data
        self.minData  = []      # Store the minimum element so far
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.data.append(x)
        # Check if we need to update the minimum value
        if len(self.minData) == 0 or x <= self.minData[-1]:
            self.minData.append(x)
    # @return an integer
    def pop(self):
        if len(self.data) == 0:
            # Empty stack
            return None
        else:
            if self.data[-1] == self.minData[-1]:   self.minData.pop()
            return self.data.pop()
    # @return an integer
    def top(self):
        if len(self.data) == 0: return None             # Empty stack
        else:                   return self.data[-1]
    # @return an integer
    def getMin(self):
        if len(self.minData) == 0:  return None         # Empty stack
        else:                       return self.minData[-1]

