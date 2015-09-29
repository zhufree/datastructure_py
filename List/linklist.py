# __author__: zhufree


class Node(object):
	"""docstring for Node"""
	def __init__(self, data, p=0):
		self.data = data
		self.next = p

	def __repr__(self):
		return self.data
		

class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):
		self.head = Node(0)

	def __repr__(self):
		p = self.head
		reprstr = str(p.data) + '->'
		while p.next:
			reprstr += str(p.next.data)
			reprstr += '->'
			p = p.next
		reprstr += ']'
		return reprstr

	def create_by_head(self, datas):
		self.clear()
		self.head = Node(datas[0])
		for i in datas[1:]:
			cur_node = Node(i)
			cur_node.next = self.head
			self.head = cur_node

	def create_by_tail(self, datas):
		self.clear()
		self.head = Node(datas[0])
		p = self.head
		for i in datas[1:]:
			cur_node = Node(i)
			p.next = cur_node
			p = p.next

	def clear(self):
		self.head = Node(0)

if __name__ == '__main__':
	llst = LinkList()
	datas = [0, 2, 4, 6, 8]
	llst.create_by_head(datas)
	print llst
	llst.create_by_tail(datas)
	print llst