import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.step, root, int(root.UID)))



    def run(self, target):


        depth = 0

        while True:

            f,next_item,UID= self.queue.get()
            self.visited[UID] = next_item

            if target.is_equal(next_item):
                return True, len(self.visited), depth

            next_state = self.graph.reveal_neighbors(next_item)


            depth += 1
            for node in next_state:
                if not node.UID in self.visited:
                    self.queue.put((f+node.step, node, int(node.UID)))


        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
