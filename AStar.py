import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):


        list=[]
        list.append(self.root)
        depth = 1


        while True:
            next_state = self.graph.reveal_neighbors(list[0])

            list += next_state
            for i in range(len(list)):
                self.visited[list[i].UID] = list[i]
                self.queue.put((self.manhattan_distance(list[i], target),list[i]))

            next_item = self.queue.get()


            if target.is_equal(next_item[1]):
                return True,len(self.visited), depth
            else:
                a=self.visited[next_item[1].UID]
                list=[]
                list.append(a)
                depth+=1


        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):

        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
