from queue import PriorityQueue
from math import sqrt

'''
A* algorithm implementation for rectangular grid
'''
class AStar():
    def __init__(self, grid):
        self._grid = grid

    '''
    Passing two nodes between which needed to find a path in specified grid
    Node is a tuple of coordinates x and y in grid
    '''
    def get_path(self, start_node, finish_node):
        queue = PriorityQueue()
        queue.put((self._heuristic_distance(start_node, finish_node), start_node, None))

        path = {}
        minimal_distance = {}

        while not queue.empty():
            priority_value, current_node, previous_node = queue.get()
            distance = priority_value - self._heuristic_distance(current_node, finish_node)

            if current_node in path and minimal_distance[current_node] <= distance:
                continue

            path[current_node] = previous_node
            minimal_distance[current_node] = distance

            if current_node == finish_node:
                break

            for x_neighbour, y_neighbour in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                neighbour_node = (current_node[0] + x_neighbour, current_node[1] + y_neighbour)
                
                if not self._is_valid(neighbour_node):
                    continue
                
                queue.put((distance + 1 + self._heuristic_distance(neighbour_node, finish_node), neighbour_node, current_node))
        
        return self._get_path_list(path, finish_node)

    '''
    Using Euclidean metric as heuristics 
    '''
    def _heuristic_distance(self, first_node, second_node):
        return sqrt((first_node[0] - second_node[0]) ** 2 + (first_node[1] - second_node[1]) ** 2)

    '''
    Checks if the node is not out of bounds and not a wall
    '''
    def _is_valid(self, node):
        x, y = node
        return 0 <= y < len(self._grid) and 0 <= x < len(self._grid[0]) and not self._grid[y][x]

    '''
    Returns a list of consecuative nodes that ake up a path to finish node
    '''
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
    algorithm = AStar(grid)
    print(algorithm.get_path((3, 6), (5, 6)))


if __name__ == "__main__":
    main()
