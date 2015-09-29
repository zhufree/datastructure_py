# __author__: zhufree


class Node(object):
	"""docstring for Node"""
	def __init__(self, data, p=0):
		self.data = data
		self.next = p

	def __repr__(self):
		return self.data
		

class LinkList(object):
	""" LinkList """
	def __init__(self, datas):
		self.head = Node(0)
		self.create_by_tail(datas)

	def __repr__(self):
		p = self.head
		reprstr = str(p.data) + '->'
		while p.next:
			reprstr += str(p.next.data)
			reprstr += '->'
			p = p.next
		reprstr += ']'
		return reprstr

	def __len__(self):
		length = 1
		p = self.head
		while p.next:
			length += 1
			p = p.next
		return length

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

	def is_empty(self):
		if len(self) == 0:
			return True
		else:
			return False

	def getData_by_index(self, index):
		count = 0
		p = self.head
		while p.next:
			if count == index:
				return p.data
			else:
				p = p.next
				count += 1
		return False

	def getData_by_value(self, value):
		count = 0
		p = self.head
		while p.next:
			if p.data == value:
				return count
			else:
				p = p.next
				count += 1
		return False

	def insertData(self, index, data):
		count = 1
		p = self.head
		while p.next:
			if count == index:
				new_node = Node(data)
				new_node.next = p.next
				p.next = new_node
				p = p.next
				print self
				return True
			else:
				p = p.next
				count += 1
		return False

	def deleteData_by_index(self, index):
		count = 1
		p = self.head
		while p.next:
			if count == index:
				p.next = p.next.next
				p = p.next
				print self
				return True
			else:
				p = p.next
				count += 1
		return False

	def deleteData_by_value(self, value):
		count = 0
		p = self.head
		while p.next:
			if p.next.data == value:
				p.next = p.next.next
				p = p.next
				# print self
				return True
			else:
				p = p.next
				count += 1
		return False

	def delete_repeat(self):
		q = self.head
		while q.next:
			p = q
			while p.next:
				if p.next.data != q.data:
					p = p.next
				else:
					self.deleteData_by_value(q.data)
					print 'delete:' + q.data
					p = p.next
			q = q.next

if __name__ == '__main__':
	datas = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'g', 'd']
	llst = LinkList(datas)
	print llst
	# llst.create_by_head(datas)
	# print llst
	# llst.create_by_tail(datas)
	
	# print len(llst)
	# print llst.getData_by_index(3)
	# llst.insertData(3, 'f')
	# llst.deleteData_by_value('f')
	llst.delete_repeat()
	print llst