# __author__: zhufree

from linklist import Node


class LinkStack (object):
    """ LinkStack """
    def __init__(self, datas=None):
        self.top = Node(0)
        self.top.next = None
        if datas:
            for i in datas:
                self.push(i)

    def __len__(self):
        length = 0 # top is not count inside
        p = self.top
        while p.next:
            length += 1
            p = p.next
        return length

    def __repr__(self):
        reprstr = '-----\n'
        p = self.top
        while p.next:
            reprstr += '| ' + str(p.next.data) + ' |\n-----\n'
            p = p.next
        return reprstr

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top.next
        self.top.next = new_node
        return self

    def pop(self):
        print 'pop out: | ' + str(self.top.next.data) + ' |'
        self.top.next = self.top.next.next
        return self

if __name__ == '__main__':
    lstack = LinkStack([1, 3, 5])
    print lstack.push(7)
    print len(lstack)
    print lstack.pop()