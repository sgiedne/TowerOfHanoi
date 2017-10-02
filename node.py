class Node:
	def __init__(self):
		self.state = []
		self.children = {}
        self.parent = []

	def get_state(self):
		return self.state

	def get_children(self):
		return self.children

	def get_parent(self):
		return self.parent
