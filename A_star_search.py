from queue import PriorityQueue

destination = (1, 1)

def h_score(current_cell, destination):

    cell_row           = current_cell[0]
    cell_column        = current_cell[1]
    destination_row    = destination[0]
    destination_column = destination[1]

    return abs(cell_row - destination_row) + abs(cell_column - destination_column)

def a_star_search(_maze):

    f_score = {cell: float("inf") for cell in _maze.grid}
    g_score = {}
    initial_cell = (_maze.rows, _maze.cols)
    g_score[initial_cell] = 0
    f_score[initial_cell] = g_score[initial_cell] + h_score(initial_cell, destination)

    queue = PriorityQueue()
    item  = (f_score[initial_cell], h_score(initial_cell, destination), initial_cell)
    queue.put(item)

    path = {}

    while not queue.empty():

        cell = queue.get()[2]

        if cell == destination:
            break

        for direction in "NSEW":

            if _maze.maze_map[cell][direction] == 1:

                cell_row    = cell[0]
                cell_column = cell[1]

                if direction == "N":
                    next_cell = (cell_row - 1, cell_column)  
                elif direction == "S":
                    next_cell = (cell_row + 1, cell_column) 
                elif direction == "W":
                    next_cell = (cell_row, cell_column - 1) 
                elif direction == "E":
                    next_cell = (cell_row, cell_column + 1) 

                new_g_score = g_score[cell] + 1
                new_f_score = new_g_score + h_score(next_cell, destination)

                if new_f_score <= f_score[next_cell]:

                    f_score[next_cell] = new_f_score
                    g_score[next_cell] = new_g_score
                    item = (new_f_score, h_score(next_cell, destination), next_cell)
                    queue.put(item)
                    path[next_cell] = cell

    final_path = {}

    analyzed_cell = destination
    print("Number of analyzed cells:", len(path.keys()))

    while analyzed_cell != initial_cell:

        final_path[path[analyzed_cell]] = analyzed_cell
        analyzed_cell = path[analyzed_cell]

    return final_path