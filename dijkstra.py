
class Dijkstra:
    def __init__(self, grid, start, goal) -> None:
        self.grid = grid
        self.start = start
        self.goal = goal

        self.stash = {}
        self.visited = set()
        self.stash[self.start] = []
        self.grid[self.start[0]][self.start[1]] = 0
        self.visited.add(self.start)
    
    def run_next(self):
        if len(self.stash) == 0:
            return (None, False, None)
        current, distance, path = self.get_next_on_stash()
        self.grid[current[0]][current[1]] = distance

        if current == self.goal:
            return (self.grid, True, path)
        
        for neighbor_node in self.get_neighbors(current):
            if not self.already_visited(neighbor_node):
                neighbor_distance = self.get_grid_value(neighbor_node)
                if neighbor_distance > distance + 1:
                    self.stash[neighbor_node] = path + [current]
                    self.grid[neighbor_node[0]][neighbor_node[1]] = distance + 1
        
        return (self.grid, False, None)
        

    
    def iterate(self):
        current = self.start

        while len(self.stash)>0:
            # self.print_grid()
            # print("stash", self.stash)
            current, distance, path = self.get_next_on_stash()
            if current == self.goal:
                break
            # print("next", current, distance)
            # input()

            self.grid[current[0]][current[1]] = distance

            for neighbor_node in self.get_neighbors(current):
                if self.grid[neighbor_node[0]][neighbor_node[1]] is None:
                    continue
                # print(neighbor_node)
                # print(neighbor_node, self.already_visited(neighbor_node))
                if not self.already_visited(neighbor_node):
                    neighbor_distance = self.get_grid_value(neighbor_node)
                    if neighbor_distance > distance + 1:
                        self.stash[neighbor_node] = path + [current]
                        self.grid[neighbor_node[0]][neighbor_node[1]] = distance + 1
        # print("RESULT", self.get_grid_value(self.goal))
        # print(path)

    def print_grid(self):
        for row in self.grid:
            print(row)

    def already_visited(self, node):
        return self.get_grid_value(node) != float("inf")
    
    def get_grid_value(self, node):
        return self.grid[node[0]][node[1]]
    
    def get_next_on_stash(self):
        min = float("inf")
        min_node = None
        path = None

        for node in self.stash:
            if self.get_grid_value(node) < min:
                min = self.get_grid_value(node)
                min_node = node
                path = self.stash[node]
        del self.stash[min_node]
        return min_node, min, path
    
    def get_neighbors(self, node):
        neighbors = []
        # has left and right
        if node[0] > 0 and node[0] < len(self.grid) - 1:
            # has up and bottom
            if node[1] > 0 and node[1] < len(self.grid[0]) -1:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]-1])
                neighbors.append([node[0], node[1]+1])
            #edges
            elif node[1] == 0:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]+1])
            else:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]-1])
        # edges
        elif node[0] == 0:
            if node[1] > 0 and node[1] < len(self.grid[0]) -1:
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]-1])
                neighbors.append([node[0], node[1]+1])
            elif node[1] == 0:
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]+1])
            else:
                neighbors.append([node[0]+1, node[1]])
                neighbors.append([node[0], node[1]-1])
        else:
            if node[1] > 0 and node[1] < len(self.grid[0]) -1:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0], node[1]-1])
                neighbors.append([node[0], node[1]+1])
            elif node[1] == 0:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0], node[1]+1])
            else:
                neighbors.append([node[0]-1, node[1]])
                neighbors.append([node[0], node[1]-1])
        neighbors = [(i[0], i[1]) for i in neighbors]
        return neighbors


if __name__ == "__main__":
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    grid  = [ [float("inf") for i in range(4)] for _ in range(4)]

    dijkstra = Dijkstra((4, 4), (1,0), (3,3))

    grid, result, path = dijkstra.run_next()
    while not result:
        dijkstra.print_grid()
        print(dijkstra.stash)
        
        input()
        print()
        grid, result, path = dijkstra.run_next()

    
    print("RESULT:", path)

    # a_star.iterate()
