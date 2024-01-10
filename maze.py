from pyamaze import maze, agent
from A_star_search import a_star_search

my_maze = maze()
my_maze.CreateMaze()

my_agent = agent(my_maze, filled=True, footprints=True)
path     = a_star_search(my_maze)

my_maze.tracePath({my_agent : path}, delay=300)
my_maze.run()