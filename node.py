class Node:
    def __init__(self):
        self.state = []
        self.children = {}
        self.parent = None

    def get_state(self):
        return self.state

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent
