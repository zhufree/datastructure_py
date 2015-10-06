# __author__: zhufree


class SeqList(object):
    """ SeqList """
    def __init__(self):
        """ create a list to store datas """
        self.datas = []

    def __len__(self):
        """ replace len with length of the list inside """
        return len(self.datas)

    def __repr__(self):
        """
        rewrite print string, format like:
        [x, x, x, ...]
        """
        reprstr = '['
        for i in self.datas:
            reprstr += str(i)
            reprstr += ', '
        reprstr += ']'
        return reprstr

    def addData(self, data):
        """ add data to the end of the list """
        self.datas.append(data)

    def getData(self, index):
        """ get data in list by index """
        if self.datas[index]:
            return self.datas[index]
        else:
            return False

    def insertData(self, data, index):
        """ insert data in list in certain index """
        if self.datas[index]:
            self.datas.insert(index, data)
        else:
            return False

    def deleteData(self, index):
        """ delete data by index """
        if self.datas[index]:
            self.datas.remove(self.datas[index])
        else:
            return False

        
if __name__ == '__main__':
    # create a seqlist
    seqlist = SeqList()
    # add data in list
    for i in range(0, 10, 2):
        seqlist.addData(i)
    print seqlist
    # insert data
    seqlist.insertData(5, 3)
    print seqlist
    # delete data
    seqlist.deleteData(3)
    print seqlist
    print len(seqlist)