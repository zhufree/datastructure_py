# __author__:zhufree

class SeqQueue(object):
    """ Queue """
    def __init__(self, datas=[], max_length=0):
        self.queue_array = datas
        self.max_length = max_length
        self.front = 0
        self.rear = 0

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        reprstr = ''
        for i in self.queue_array:
            reprstr += str(i) + ' | '
        return reprstr

    def is_empty(self):
        if front == rear:
            return True
        else:
            return False

    def is_full(self):
        pass
        #if self.rear == self.max_length - 1

    def insert(self, data):
        self.queue_array[self.rear] = data
        self.rear += 1
        return self

    def delete(self, data):
        del self.queue_array[self.front]
        self.front += 1
        return self

if __name__ == '__main__':
    seqqueue = SeqQueue(range(0, 9, 2))
    print seqqueue
    print seqqueue.insert(3)