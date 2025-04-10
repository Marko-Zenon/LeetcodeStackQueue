class MyStack(object):

    def __init__(self):
        self.lst = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.lst.append(x) 
        self.size += 1

    def pop(self):
        """
        :rtype: int
        """
        self.size -=1
        return self.lst.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()