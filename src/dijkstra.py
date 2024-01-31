from queue import PriorityQueue

class Dijkstra():
    def __init__(self, grid):
        self._grid = grid 
        self._amount_of_nodes = 0
        for line in grid:
            for node in line:
                self._amount_of_nodes += 1 if node == 0 else 0

    def get_path(self, start_node, finish_node):
        path = {start_node: None}
        minimal_distance = {start_node: 0}
        processed_nodes = set() 
        
        while len(processed_nodes) != self._amount_of_nodes:
            current_node = self._pick_node(minimal_distance, processed_nodes)

            processed_nodes.add(current_node)

            neighbour_distance = minimal_distance[current_node] + 1
            for x_neighbour, y_neighbour in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                neighbour_node = (current_node[0] + x_neighbour, current_node[1] + y_neighbour)
                
                if not self._is_valid(neighbour_node) or \
                    neighbour_node in path and minimal_distance[neighbour_node] <= neighbour_distance:
                    continue

                path[neighbour_node] = current_node
                minimal_distance[neighbour_node] = neighbour_distance

        return self._get_path_list(path, finish_node)

    def _pick_node(self, nodes_distances, processed_nodes):
        picked_node = None
        picked_distance = float("inf") 

        for node in nodes_distances:
            distance = nodes_distances[node]
            if node in processed_nodes or distance >= picked_distance:
                continue

            picked_node = node
            picked_distance = distance

        return picked_node

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

