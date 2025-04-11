class FreqStack(object):

    def __init__(self):
        self.lst = []
        self.freq = {}
        self.group = {}           
        self.max_freq = 0

    def push(self, val):
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        friki = self.freq[val]
        if friki > self.max_freq:
            self.max_freq = friki
        if friki not in self.group:
            self.group[friki] = []
        self.group[friki].append(val)
        self.lst.append(val)

    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
