# __author__: zhufree


class SeqStack(object):
    """docstring for Stack"""
    def __init__(self,datas=[]):
        self.array = datas
        self.bottom = 0
        self.top = len(datas) - 1

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        reprstr = '-----\n'
        self.array.reverse()
        for i in self.array:
            reprstr += '| ' + str(i) + ' |\n-----\n'
        self.array.reverse()
        return reprstr

    def is_empty(self):
        return self.top == self.bottom - 1

    def push(self, data):
        self.array.append(data)
        self.top += 1
        return self

    def pop(self):
        try:
            e = self.array[self.top]
            print 'pop out: | ' + str(e) + ' |'
            self.top -= 1
            return self
        except Exception, e:
            return False
        
def conversion(number, div):
    stack = SeqStack()
    while number > 0:
        t = number % div
        stack.push(t)
        number = number/div
    while not stack.is_empty():
        stack.pop()

if __name__ == '__main__':
    conversion(1348, 8)