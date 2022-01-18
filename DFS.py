class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0


    def run(self, target):
        depth = 0

        while True:

            current_node = self.stack.pop()
            self.visited[current_node.UID]=current_node

            if target.is_equal(current_node):
                return True, len(self.stack), depth
            depth+=1
            next_state = self.graph.reveal_neighbors(current_node)
            for node in reversed(next_state):

                if not node.UID in self.visited:
                    self.stack.append(node)




        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
