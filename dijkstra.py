
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
    
    # run one itteration of the alogrithm as opposed to one-shot
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
        

    # one shot algorithm
    def iterate(self):
        current = self.start

        # while there are items on the edges
        while len(self.stash)>0:
            current, distance, path = self.get_next_on_stash()
            if current == self.goal:
                break
            self.grid[current[0]][current[1]] = distance

            # check the neighbors and add them to the edges stash if they were not checked yet and are not walls
            for neighbor_node in self.get_neighbors(current):
                if self.grid[neighbor_node[0]][neighbor_node[1]] is None:
                    continue
                if not self.already_visited(neighbor_node):
                    neighbor_distance = self.get_grid_value(neighbor_node)
                    if neighbor_distance > distance + 1:
                        self.stash[neighbor_node] = path + [current]
                        self.grid[neighbor_node[0]][neighbor_node[1]] = distance + 1

    def print_grid(self):
        for row in self.grid:
            print(row)

    def already_visited(self, node):
        return self.get_grid_value(node) != float("inf")
    
    def get_grid_value(self, node):
        return self.grid[node[0]][node[1]]
    
    # get closest point on the edge
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
    
    # get neighboring cells
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
