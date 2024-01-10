from pyamaze import maze, agent

def h_score():
    pass

def a_star_search():
    pass

my_maze = maze()

my_maze.CreateMaze()

my_agent = agent(my_maze, filled=True, footprints=True)

path = {}

my_maze.tracePath({my_agent : path}, delay=300)

my_maze.run()