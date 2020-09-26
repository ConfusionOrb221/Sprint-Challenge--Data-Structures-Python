class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(self.current)
            self.storage.insert(self.current, item)
            if self.current + 1 == self.capacity:
                self.current = 0
            else:
                self.current += 1
        elif len(self.storage) == 0:
            self.oldest = item
            self.storage.append(item)
        else:
            self.storage.append(item)

    def get(self):
        return self.storage