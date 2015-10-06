# __author__: zhufree
from linklist import LinkList

class DulNode(object):
     """ DulNode """
     def __init__(self, data):
         self.data = data
         self.next = None
         self.prior = None

     def __repr__(self):
        return self.data


class DulList(LinkList):
    """ DulList """
    def __init__(self, datas=None):
        self.head = DulNode(0)
        if datas:
            self.create_by_tail(datas)

    def __repr__(self):
        """
        rewrite print string, format like:
        x->x->x->...->]
        """
        p = self.head
        reprstr = str(p.data) + '->'
        while p.next:
            reprstr += str(p.next.data)
            reprstr += '->'
            p = p.next
        reprstr += ']\n' + p.data + '->'
        while p.prior:
            reprstr += str(p.prior.data)
            reprstr += '->'
            p = p.prior
        reprstr += ']\n'
        return reprstr

    def __len__(self):
        """
        count the length of the LinkList by go through the list
        """
        length = 1
        p = self.head
        while p.next:
            length += 1
            p = p.next
        return length

    def create_by_head(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the head of the list
        """
        self.clear()
        self.head = DulNode(datas[0])
        for i in datas[1:]:
            cur_node = DulNode(i)
            cur_node.next = self.head
            self.head.prior = cur_node
            self.head = cur_node

    def create_by_tail(self, datas):
        """
        create a LinkList by using data in datas(a list)
        every data will be added at the tail of the list
        """
        self.clear()
        self.head = DulNode(datas[0])
        p = self.head
        for i in datas[1:]:
            cur_node = DulNode(i)
            p.next = cur_node
            cur_node.prior = p
            p = p.next

    def clear(self):
        """ clear the list """
        self.head = DulNode(0)

    def insertData(self, index, data):
        """
        :param index: the position to insert data to.
        :param data: the data to insert into list.
        :return: True or False.
        """
        count = 1
        p = self.head
        while p.next:
            if count == index:
                new_node = DulNode(data)
                new_node.next = p.next
                p.next.prior = new_node
                p.next = new_node
                new_node.prior = p
                p = p.next
                return True
            else:
                p = p.next
                count += 1
        return False

    def deleteData_by_index(self, index):
        """
        :param index: position of the node to delete.
        :return: True or False.
        """
        count = 1
        p = self.head
        while p.next:
            if count == index:
                p.prior.next = p.next
                p.next.prior = p.prior
                print 'delete: ' + p.data
                p = p.next
                return True
            else:
                p = p.next
                count += 1
        return False

    def deleteData_by_value(self, value):
        """
        :param index: value of the node to delete.
        :return: True or False.
        """
        count = 0
        p = self.head
        while p.next:
            if p.data == value:
                p.prior.next = p.next
                p.next.prior = p.prior
                print 'delete: ' + p.data
                p = p.next
                return True
            else:
                p = p.next
                count += 1
        return False

    def delete_repeat(self):
        """
        delete repeat node in list
        """
        p = self.head
        while p:
            q = p
            r = p.next
            while r:
                if r.data == p.data:
                    q.next = r.next
                    if q.next:
                        q.next.prior = q
                    r = q.next
                    print 'delete:' + p.data
                else:
                    q = r
                    r = r.next
            p = p.next

    def delete_one(self, value):
        """
        delete all node of the value in list
        """
        # while self.getData_by_value(value):
        #     self.deleteData_by_value(value)
        p = self.head
        q = p.next
        while q:
            if q.data == value:
                q.prior.next = q.next
                q.next.prior = q.prior
                q = p.next
            else:
                p = q
                q = q.next        


if __name__ == '__main__':
    chardatas = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'c', 'g', 'd']
    dullist = DulList(chardatas)
    dullist.insertData(5, 'k')
    print dullist
    dullist.deleteData_by_index(6)
    print dullist
    dullist.deleteData_by_value('k')
    print dullist
    # dullist.delete_repeat()
    dullist.delete_one('c')
    print dullist
