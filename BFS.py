class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root

        self.queue.append(root)

    def run(self, target):


        depth = 0

        while True:
            for i in range(len(self.queue)):
                next_state = self.graph.reveal_neighbors(self.queue[i])

                self.queue += next_state
                self.visited[self.queue[i].UID] = self.queue[i]

            depth += 1
            for i in range(len(self.visited)):
                if target.is_equal (list(self.visited.values())[i]):

                    return True, i+1, depth


        return False, 0, 0
