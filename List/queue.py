# __author__:zhufree

class Queue(object):
    """ Queue """
    def __init__(self, datas=[], max_length=0):
        self.max_length = max_length
        if datas == []:
            self.front = 0
            self.rear = 0
            for i in range(max_length):
                datas.insert(0, None)
            self.array = datas
        else:
            self.front = 0
            self.rear = len(datas) - 1
            for i in range(len(datas), max_length):
                datas.insert(0, None)
            self.array = datas

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        reprstr = 'head:'
        for i in self.array:
            reprstr += str(i) + ' | '
        return reprstr

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if self.rear == self.max_length:
            return True
        else:
            return False

    def insert(self, data):
        if self.is_full():
            return False
        else:
            for i in range(self.max_length-1):
                self.array[i] = self.array[i+1]
            self.array[self.max_length-1] = data
            self.rear += 1
            return self

    def delete(self):
        for i in range(self.max_length-1):
            self.array[i] = self.array[i+1]
        self.array[self.max_length-1] = None
        self.front += 1
        return self


class CirQueue(Queue):

    def is_empty(self):
        if self.front + 1 == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if (self.rear + 1) % (self.max_length + 1) == self.front:
            return True
        else:
            return False

    def insert(self, data):
        if self.is_full():
            return False
        else:
            for i in range(self.max_length-1):
                self.array[i] = self.array[i+1]
            self.array[self.max_length-1] = data
            # if self.rear + 1 == self.max_length:
            #     self.rear = 0
            # else:
            #     self.rear += 1
            self.rear = (self.rear + 1) % (self.max_length + 1)
            return self

    def delete(self):
        for i in range(self.max_length-1):
            self.array[i] = self.array[i+1]
        self.array[self.max_length-1] = None
        self.front = (self.front + 1) % (self.max_length + 1)
        return self


if __name__ == '__main__':
    # queue = Queue(range(0, 9, 2))
    queue = CirQueue([2, 4, 8], max_length=10)
    print queue
    for i in range(0, 9):
        print queue.insert(i)
        print queue.rear, queue.front
    for i in range(0, 10):
        print queue.delete()
        print queue.rear, queue.front
    for i in range(0, 10):
        print queue.insert(i)
        print queue.rear, queue.front
