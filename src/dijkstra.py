from queue import PriorityQueue

class Dijkstra():
    def __init__(self, grid):
        self._grid = grid 

    def get_path(self, start_node, finish_node):
        queue = PriorityQueue()
        queue.put((0, start_node, None))

        path = {}
        
        while not queue.empty():
            distance, current_node, previous_node = queue.get()
            
            if current_node in path:
                continue

            path[current_node] = previous_node

            if current_node == finish_node:
                break

            for x_neighbour, y_neighbour in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                neighbour_node = (current_node[0] + x_neighbour, current_node[1] + y_neighbour)
                
                if not self._is_valid(neighbour_node):
                    continue
                
                queue.put((distance + 1, neighbour_node, current_node))

        return self._get_path_list(path, finish_node)

    def _is_valid(self, node):
        x, y = node
        return 0 <= y < len(self._grid) and 0 <= x < len(self._grid[0]) and not self._grid[y][x]

    def _get_path_list(self, path_dictionary, finish_node):
        if finish_node not in path_dictionary:
            return None

        path_list = []
        current_node = finish_node
        while current_node is not None:
            path_list.insert(0, current_node)
            current_node = path_dictionary[current_node]

        return path_list


def main():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0]
    ]
    algorithm = Dijkstra(grid)
    print(algorithm.get_path((0, 0), (8, 8)))

if __name__ == "__main__":
    main()

