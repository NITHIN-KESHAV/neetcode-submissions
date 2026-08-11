class MinStack:

    def __init__(self):

        self.minstack = []
        self.mins = []
        

    def push(self, val: int) -> None:

        self.minstack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

        

    def pop(self) -> None:
        
        val = self.minstack.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:

        return self.minstack[-1]
        

    def getMin(self) -> int:

        return self.mins[-1]