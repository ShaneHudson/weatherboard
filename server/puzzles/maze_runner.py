from puzzles.kruskal_maze.kruskal_maze import KruskalMaze
from puzzles.maze_display import MazePlot

class MazeRunner:
	def __init__(self,width,height):
		"""
        https://github.com/lvngd/mazes/
        input: matrix width and height"""
		self.width = width
		self.height = height
		self.maze = KruskalMaze(self.width,self.height)
		self.graph = [[0 for x in range(self.width)]for y in range(self.height)]
		self.visualization = MazePlot(self.width,self.height,self.maze)
		#save initial maze layout as a png
		self.visualization.save_as_image()